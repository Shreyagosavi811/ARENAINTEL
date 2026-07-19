from .schemas import ReportIncidentRequest, ReportIncidentResponse, IncidentAIResponse
from .prompt_builder import IncidentPromptBuilder
from ...infrastructure.ai.provider import IAIProvider
from ...infrastructure.retrieval.provider import IRetriever
from ...infrastructure.audit.logger import AuditLogger

class ReportIncidentUseCase:
    def __init__(self, ai_provider: IAIProvider, retriever: IRetriever, prompt_builder: IncidentPromptBuilder, audit_logger: AuditLogger):
        self.ai_provider = ai_provider
        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.audit_logger = audit_logger
    
    async def execute(self, request: ReportIncidentRequest, actor_id: str) -> ReportIncidentResponse:
        # 1. Audit Log the raw input submission
        await self.audit_logger.log_event("SUBMIT_INCIDENT_REPORT", actor_id, f"Raw text: {request.text[:50]}...")
        
        # 2. Retrieve SOPs
        docs = await self.retriever.retrieve(request.text, top_k=2)
        
        # 3. Build Prompt safely
        prompt = self.prompt_builder.build_incident_prompt(request.text, docs)
        
        # 4. Ask GenAI
        ai_response = await self.ai_provider.generate_structured_output(prompt, IncidentAIResponse)
        
        # 5. Domain safety checks (Ensure human approval is requested)
        ai_response.requires_human_approval = True
        
        # 6. Check if AI made a medical diagnosis accidentally
        is_medical = "medical diagnosis" in " ".join(ai_response.recommended_steps).lower() or "medical diagnosis" in ai_response.severity_assessment.lower()
        
        return ReportIncidentResponse(
            is_medical_diagnosis=is_medical,
            ai_analysis=ai_response
        )
