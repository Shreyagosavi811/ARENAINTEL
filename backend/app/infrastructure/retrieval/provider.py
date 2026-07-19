from typing import List, Protocol
from pydantic import BaseModel
import math
import re
from collections import defaultdict, Counter
import os
import logging

logger = logging.getLogger("stadiumops.retrieval")

class RetrievedDocument(BaseModel):
    id: str
    title: str
    content: str
    metadata: dict

class IRetriever(Protocol):
    async def retrieve(self, query: str, top_k: int = 3, max_chars: int = 2000) -> List[RetrievedDocument]:
        ...

class MockRetriever(IRetriever):
    def __init__(self, should_fail: bool = False):
        self.should_fail = should_fail
        
    async def retrieve(self, query: str, top_k: int = 3, max_chars: int = 2000) -> List[RetrievedDocument]:
        if self.should_fail or "fail" in query.lower():
            raise Exception("Mock Retrieval Failure")
        if "empty" in query.lower():
            return []
            
        doc = RetrievedDocument(
            id="mock1", title="Mock Doc", content="This is mock content.", metadata={"source": "test"}
        )
        return [doc]

class TfIdfRetriever(IRetriever):
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        self.documents: List[RetrievedDocument] = []
        self.df = defaultdict(int)
        self.idf = {}
        self.doc_tf = []
        self._load_documents()
        self._compute_idf()

    def _tokenize(self, text: str) -> List[str]:
        return re.findall(r'\b\w+\b', text.lower())

    def _load_documents(self):
        if not os.path.exists(self.data_dir):
            logger.warning(f"Knowledge directory {self.data_dir} not found.")
            return

        for filename in os.listdir(self.data_dir):
            if filename.endswith(".md") or filename.endswith(".txt"):
                path = os.path.join(self.data_dir, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                lines = content.split('\n')
                title = lines[0].replace('#', '').strip() if lines else filename
                
                doc = RetrievedDocument(
                    id=filename, title=title, content=content, metadata={"source": "local_file", "path": path}
                )
                self.documents.append(doc)
                
                tokens = self._tokenize(content)
                tf = Counter(tokens)
                self.doc_tf.append(tf)
                
                for token in set(tokens):
                    self.df[token] += 1

    def _compute_idf(self):
        N = len(self.documents)
        for token, count in self.df.items():
            self.idf[token] = math.log((N + 1) / (count + 1)) + 1

    async def retrieve(self, query: str, top_k: int = 3, max_chars: int = 2000) -> List[RetrievedDocument]:
        if not self.documents:
            return []

        query_tokens = self._tokenize(query)
        scores = []
        
        for idx, doc_tf in enumerate(self.doc_tf):
            score = 0.0
            for token in query_tokens:
                if token in doc_tf:
                    score += doc_tf[token] * self.idf.get(token, 0)
            scores.append((score, self.documents[idx]))

        # Sort by score descending
        scores.sort(key=lambda x: x[0], reverse=True)
        
        results = []
        total_chars = 0
        for score, doc in scores:
            if score == 0: 
                continue
            
            # Context size limit handling
            if total_chars + len(doc.content) > max_chars:
                if not results:
                    truncated = doc.model_copy()
                    truncated.content = doc.content[:max_chars] + "... [TRUNCATED]"
                    results.append(truncated)
                break
                
            results.append(doc)
            total_chars += len(doc.content)
            
            if len(results) >= top_k:
                break
                
        return results
