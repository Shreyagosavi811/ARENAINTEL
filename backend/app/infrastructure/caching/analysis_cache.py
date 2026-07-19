import hashlib
import time
from typing import Optional, Dict, Tuple
import json

class AnalysisCache:
    def __init__(self, ttl_seconds: int = 60):
        self.ttl = ttl_seconds
        # stores hash -> (timestamp, response_data)
        self._store: Dict[str, Tuple[float, dict]] = {}
        
    def _hash_context(self, text: str, matchday_context: dict) -> str:
        # Create a deterministic string representation
        # We sort keys in matchday_context to ensure stable hashing
        context_str = json.dumps(matchday_context, sort_keys=True)
        raw = f"{text}|{context_str}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()
        
    def get(self, text: str, matchday_context: dict) -> Optional[dict]:
        key = self._hash_context(text, matchday_context)
        if key in self._store:
            timestamp, data = self._store[key]
            if time.time() - timestamp <= self.ttl:
                return data
            else:
                # Expired
                del self._store[key]
        return None
        
    def set(self, text: str, matchday_context: dict, data: dict) -> None:
        key = self._hash_context(text, matchday_context)
        self._store[key] = (time.time(), data)

# Singleton cache for the application
analysis_cache = AnalysisCache()
