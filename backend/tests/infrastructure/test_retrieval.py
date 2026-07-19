import pytest
import os
from app.infrastructure.retrieval.provider import TfIdfRetriever, MockRetriever

@pytest.fixture
def retriever():
    # Will point to the actual knowledge base since it's lightweight
    data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'knowledge')
    return TfIdfRetriever(data_dir=data_dir)

@pytest.mark.asyncio
async def test_relevant_retrieval(retriever):
    results = await retriever.retrieve("child is lost", top_k=1)
    assert len(results) == 1
    assert "SOP_Lost_Child.md" in results[0].id
    assert "Code Amber" in results[0].content
    assert results[0].metadata["source"] == "local_file"

@pytest.mark.asyncio
async def test_no_relevant_results(retriever):
    # Query with non-existent words
    results = await retriever.retrieve("alien invasion spaceship ufo", top_k=3)
    assert len(results) == 0

@pytest.mark.asyncio
async def test_multiple_relevant_results(retriever):
    # 'gate' and 'emergency' appear in multiple docs (Evacuation and Facility Outage)
    results = await retriever.retrieve("gate emergency close", top_k=5)
    assert len(results) > 1

@pytest.mark.asyncio
async def test_retrieval_failure():
    mock = MockRetriever(should_fail=True)
    with pytest.raises(Exception, match="Mock Retrieval Failure"):
        await mock.retrieve("anything")

@pytest.mark.asyncio
async def test_context_size_limits(retriever):
    # Force a very tiny max_chars limit to ensure truncation kicks in
    results = await retriever.retrieve("child is lost", top_k=1, max_chars=10)
    assert len(results) == 1
    assert "[TRUNCATED]" in results[0].content
    assert len(results[0].content) <= 10 + len("... [TRUNCATED]")
