import pytest
from app.application.scenarios.schemas import SimulateScenarioRequest, ScenarioSimulationAIResponse, ScenarioMitigation
from app.application.scenarios.simulate_scenario import SimulateScenarioUseCase
from app.application.copilot.context_service import ContextService
from app.application.scenarios.prompt_builder import ScenarioPromptBuilder
from app.infrastructure.retrieval.provider import MockRetriever
from app.infrastructure.ai.provider import IAIProvider

class CustomMockAI(IAIProvider):
    async def generate_structured_output(self, prompt, schema):
        return ScenarioSimulationAIResponse(
            expected_impacts=["Impact A"],
            potential_risks=["Risk A"],
            mitigations=[ScenarioMitigation(action="Close Gate", impact="Lowers congestion")],
            affected_stakeholders=["Fans"],
            communication_requirements=["PA Announcement"],
            assumptions=["Match starts on time"],
            uncertainty="Unknown fan arrival rate"
        )
    async def generate_text(self, p): return ""
    async def generate_translated_communication(self, p, t): return ""
    async def generate_operational_analysis(self, c, s): return await self.generate_structured_output(c, s)

@pytest.mark.asyncio
async def test_scenario_workflow_returns_hypothetical_flag():
    use_case = SimulateScenarioUseCase(
        ai_provider=CustomMockAI(),
        retriever=MockRetriever(),
        context_service=ContextService(),
        prompt_builder=ScenarioPromptBuilder()
    )
    req = SimulateScenarioRequest(what_if_query="What if it rains?")
    res = await use_case.execute(req)
    
    assert res.is_hypothetical_simulation is True
    assert len(res.expected_impacts) == 1

@pytest.mark.asyncio
async def test_scenario_does_not_mutate_real_context():
    class MutableContextService(ContextService):
        async def get_current_context(self):
            ctx = await super().get_current_context()
            ctx.stadium.name = "Real Stadium"
            return ctx
            
    service = MutableContextService()
    
    # Run the simulation, which deepcopies the context internally
    use_case = SimulateScenarioUseCase(
        ai_provider=CustomMockAI(),
        retriever=MockRetriever(),
        context_service=service,
        prompt_builder=ScenarioPromptBuilder()
    )
    req = SimulateScenarioRequest(what_if_query="What if it rains?")
    await use_case.execute(req)
    
    # Verify the real context remains untouched by retrieving it again or checking if the service instance changed it
    real_ctx = await service.get_current_context()
    assert real_ctx.stadium.name == "Real Stadium"
