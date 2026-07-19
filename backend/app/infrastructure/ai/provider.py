from typing import TypeVar, Type, Any
from pydantic import BaseModel, ValidationError
import asyncio
import logging
import httpx
from app.core.exceptions import AIProviderUnavailableError

logger = logging.getLogger("stadiumops.ai")

T = TypeVar("T", bound=BaseModel)

class IAIProvider:
    """
    Abstract interface for AI Providers.
    The rest of the application must depend strictly on this interface.
    """
    async def generate_text(self, prompt: str) -> str:
        raise NotImplementedError
        
    async def generate_structured_output(self, prompt: str, schema: Type[T]) -> T:
        raise NotImplementedError
        
    async def generate_translated_communication(self, message: str, target_language: str) -> str:
        raise NotImplementedError
        
    async def generate_operational_analysis(self, context: str, schema: Type[T]) -> T:
        raise NotImplementedError


class MockAIProvider(IAIProvider):
    """
    Mock provider for blazing fast, deterministic unit tests.
    """
    def __init__(self, should_timeout: bool = False, should_return_malformed: bool = False):
        self.should_timeout = should_timeout
        self.should_return_malformed = should_return_malformed

    async def generate_text(self, prompt: str) -> str:
        return "Mocked AI response text."

    async def generate_structured_output(self, prompt: str, schema: Type[T]) -> T:
        if self.should_timeout:
            await asyncio.sleep(0.5) # simulate latency
            raise AIProviderUnavailableError("AI Provider timed out.")
            
        if self.should_return_malformed:
            raise ValidationError.from_exception_data(title="MockError", line_errors=[])
            
        # Return a valid mock for CopilotAIResponse specifically for local demo testing
        from app.application.copilot.schemas import CopilotAIResponse, AIRecommendationAction, OperationalImpact
        if schema.__name__ == "CopilotAIResponse":
            return CopilotAIResponse(
                summary="[MOCK AI] Crowd surge detected at Gate C.",
                risk_level="high",
                risks=["Crush risk", "Delayed entry"],
                recommendations=[
                    AIRecommendationAction(action="Open overflow gates", priority="high", reason="Alleviate pressure", requires_approval=True)
                ],
                uncertainties=["Exact crowd size unknown"],
                impact_estimate=OperationalImpact(
                    potential_outcome="Risk averted",
                    estimated_response_time_saved="10m",
                    affected_zones=["Gate C"],
                    risk_trajectory="High -> Low",
                    confidence="High",
                    basis="SOP Match"
                )
            )
        
        # Fallback for other schemas
        return schema()
        
    async def generate_translated_communication(self, message: str, target_language: str) -> str:
        return f"[Translated to {target_language}]: {message}"
        
    async def generate_operational_analysis(self, context: str, schema: Type[T]) -> T:
        return await self.generate_structured_output(context, schema)


class BaseRealAIProvider(IAIProvider):
    """
    A base class for real SDK implementations (OpenAI, Gemini) that provides
    standardized resilience: timeouts, safe retries, and schema validation.
    """
    def __init__(self, timeout_seconds: int = 15, max_retries: int = 3):
        self.timeout_seconds = timeout_seconds
        self.max_retries = max_retries


    async def _safe_execute(self, func, *args, **kwargs) -> Any:
        """Executes a function with timeout and safe retry handling."""
        attempt = 0
        while attempt < self.max_retries:
            try:
                attempt += 1
                return await asyncio.wait_for(func(*args, **kwargs), timeout=self.timeout_seconds)
            except asyncio.TimeoutError:
                logger.error(f"AI_PROVIDER_TIMEOUT - Attempt {attempt}/{self.max_retries} exceeded {self.timeout_seconds}s limit.")
                if attempt >= self.max_retries:
                    raise AIProviderUnavailableError("AI Provider timed out after max retries.")
            except (httpx.RequestError, httpx.HTTPStatusError) as e:
                # Log metadata, NEVER log the prompt itself as it may contain sensitive data
                logger.error(f"AI Provider network error on attempt {attempt}: {str(e)}")
                if attempt >= self.max_retries:
                    raise AIProviderUnavailableError(f"AI Provider failed: {str(e)}")
                await asyncio.sleep(2 ** attempt) # Exponential backoff

    async def generate_structured_output(self, prompt: str, schema: Type[T]) -> T:
        # 1. Call the actual SDK inside _safe_execute
        # raw_json_string = await self._safe_execute(self._call_sdk, prompt)
        
        # 2. Strict Schema Validation
        # try:
        #     validated_obj = schema.model_validate_json(raw_json_string)
        #     return validated_obj
        # except ValidationError as e:
        #     logger.error("AI returned malformed output.")
        #     raise
        pass
