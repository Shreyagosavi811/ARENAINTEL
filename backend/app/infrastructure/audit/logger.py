import logging
from uuid import UUID

logger = logging.getLogger("stadiumops.audit")

class AuditLogger:
    async def log_event(self, action: str, actor_id: str, details: str):
        logger.info(f"AUDIT_EVENT | action={action} | actor={actor_id} | details={details}")
