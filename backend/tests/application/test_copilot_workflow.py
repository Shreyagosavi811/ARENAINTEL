import pytest
from app.application.copilot.schemas import AnalyzeSituationRequest, CopilotAIResponse, AIRecommendationAction, OperationalImpact
from app.application.copilot.analyze_situation import CopilotUseCase
from app.application.copilot.context_service import ContextService
from app.application.copilot.prompt_builder import PromptBuilder
from app.infrastructure.retrieval.provider import MockRetriever
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

@pytest.mark.asyncio
async def test_full_copilot_workflow():
    use_case = CopilotUseCase(
        ai_provider=CustomMockAI(),
        retriever=MockRetriever(),
        context_service=ContextService(),
        prompt_builder=PromptBuilder()
    )
    req = AnalyzeSituationRequest(text="Elevator is broken and heavy rain is coming.")
    res = await use_case.execute(req, user_role="operator")
    
    assert res.summary == "Test summary"
    assert len(res.recommendations) == 1
    assert res.capabilities.can_approve is False
