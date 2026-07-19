import pytest
import asyncio
from pydantic import BaseModel, ValidationError
from app.infrastructure.ai.provider import MockAIProvider, BaseRealAIProvider
from app.core.exceptions import AIProviderUnavailableError

class DummySchema(BaseModel):
    risk_level: str
    confidence: str

@pytest.mark.asyncio
async def test_mock_provider_success():
    provider = MockAIProvider()
    # Mock behavior for success text
    text = await provider.generate_text("Test prompt")
    assert text == "Mocked AI response text."

@pytest.mark.asyncio
async def test_mock_provider_translation():
    provider = MockAIProvider()
    text = await provider.generate_translated_communication("Evacuate", "es")
    assert "es" in text
    assert "Evacuate" in text

@pytest.mark.asyncio
async def test_mock_provider_timeout_simulation():
    provider = MockAIProvider(should_timeout=True)
    with pytest.raises(AIProviderUnavailableError):
        await provider.generate_structured_output("Prompt", DummySchema)

@pytest.mark.asyncio
async def test_base_real_provider_timeout_handling():
    # We create a dummy implementation of the BaseRealAIProvider to test its retry logic
    class DummyProvider(BaseRealAIProvider):
        def __init__(self):
            super().__init__(timeout_seconds=0.1, max_retries=2)
            self.attempts = 0
            
        async def _fake_slow_sdk_call(self):
            self.attempts += 1
            await asyncio.sleep(0.5) # Slower than the 0.1 timeout
            return "{}"

        async def generate_text(self, prompt: str) -> str:
            return await self._safe_execute(self._fake_slow_sdk_call)
            
    provider = DummyProvider()
    
    with pytest.raises(AIProviderUnavailableError, match="timed out"):
        await provider.generate_text("Prompt")
        
    # Verify it retried exactly twice
    assert provider.attempts == 2

@pytest.mark.asyncio
async def test_base_real_provider_validation_failure():
    # Test that invalid JSON strictly raises a ValidationError
    class DummyValidationProvider(BaseRealAIProvider):
        async def _fake_bad_sdk_call(self):
            return '{"risk_level": "high"}' # Missing 'confidence' field
            
        async def generate_structured_output(self, prompt: str, schema) -> DummySchema:
            raw = await self._safe_execute(self._fake_bad_sdk_call)
            # Simulate the pydantic parsing
            return schema.model_validate_json(raw)

    provider = DummyValidationProvider()
    with pytest.raises(ValidationError):
        await provider.generate_structured_output("Prompt", DummySchema)
