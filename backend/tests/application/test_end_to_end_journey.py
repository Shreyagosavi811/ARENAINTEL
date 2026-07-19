import pytest
from app.application.copilot.schemas import AnalyzeSituationRequest, MatchdayContext
from app.application.copilot.analyze_situation import CopilotUseCase
from app.application.copilot.context_service import ContextService
from app.application.copilot.prompt_builder import PromptBuilder
from app.infrastructure.retrieval.provider import TfIdfRetriever
from app.infrastructure.ai.provider import MockAIProvider
import os

@pytest.mark.asyncio
async def test_end_to_end_operational_journey():
    """
    Simulates the complete user journey:
    Submit -> Retrieve SOP -> AI Gen -> Schema Validate
    """
    # 1. Initialize dependencies
    data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "knowledge")
    retriever = TfIdfRetriever(data_dir=data_dir)
    context_service = ContextService()
    prompt_builder = PromptBuilder()
    
    # We use a Mock AI Provider but assume it adheres to the pipeline
    # We must patch generate_structured_output to return a valid CopilotAIResponse 
    from app.application.copilot.schemas import CopilotAIResponse, AIRecommendationAction, OperationalImpact
    from app.infrastructure.ai.provider import IAIProvider
    
    class CustomMockAI(IAIProvider):
        async def generate_structured_output(self, prompt, schema):
            return CopilotAIResponse(
                summary="Test summary",
                risk_level="high",
                risks=["Risk A"],
                recommendations=[AIRecommendationAction(action="Evac", priority="high", reason="Safe", requires_approval=True)],
                uncertainties=["Missing weather data"],
                impact_estimate=OperationalImpact(
                    potential_outcome="Reduced risk",
                    estimated_response_time_saved="5 min",
                    affected_zones=["Zone A"],
                    risk_trajectory="High -> Low",
                    confidence="High",
                    basis="Test Basis"
                )
            )
        async def generate_text(self, p): return ""
        async def generate_translated_communication(self, p, t): return ""
        async def generate_operational_analysis(self, c, s): return await self.generate_structured_output(c, s)

    custom_ai = CustomMockAI()
    
    use_case = CopilotUseCase(
        ai_provider=custom_ai,
        retriever=retriever,
        context_service=context_service,
        prompt_builder=prompt_builder
    )
    
    # 2. Setup the request with Matchday Context
    req = AnalyzeSituationRequest(
        text="A large group of spectators is crowding Gate B and someone appears to have slipped.",
        matchday_context=MatchdayContext(phase="Pre-Match")
    )
    
    # 3. Execute the pipeline
    response = await use_case.execute(req, user_role="supervisor")
    
    # 4. Assertions verifying the end-to-end data flow
    assert response.summary == "Test summary"
    assert response.impact_estimate.confidence == "High"
    assert "SOP" in response.retrieval_confidence or "relevant" in response.retrieval_confidence
    assert response.capabilities.can_approve is True # Since user_role is supervisor
