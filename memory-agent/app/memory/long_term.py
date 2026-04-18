from typing import List, Dict, Any, Optional
from app.config import MemoryItem
from app.memory.memory_store import MemoryStore
from app.memory.memory_scorer import should_store_memory
from app.memory.memory_retriever import score_and_rank_memories

class LongTermMemory:
    """
    Orchestrates the long-term memory process:
    - Checking if a memory meets the threshold.
    - Storing in ChromaDB.
    - Retrieving and scoring based on hybrid logic.
    """
    
    def __init__(self):
        self.store = MemoryStore()
        
    def process_and_store(self, candidate_memories: List[MemoryItem]) -> List[str]:
        """
        Evaluate candidate memories, store those that pass the threshold.
        Returns the list of stored IDs.
        """
        stored_ids = []
        for memory in candidate_memories:
            if should_store_memory(
                memory.durability, 
                memory.impact, 
                memory.frequency, 
                memory.confidence
            ):
                mem_id = self.store.add_memory(memory)
                stored_ids.append(mem_id)
        return stored_ids
        
    def retrieve_relevant(self, query: str, top_k: int = 5, memory_type: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retrieve context for the current query using hybrid scoring.
        """
        # Fetch a broader set first (e.g. 15) to allow ranking
        raw_results = self.store.query_similar(query, n_results=15, memory_type=memory_type)
        
        if not raw_results:
            return []
            
        ranked_results = score_and_rank_memories(raw_results, top_k=top_k)
        return ranked_results
        
    def update_memory(self, memory_id: str, new_memory: MemoryItem):
        """Update an existing memory directly."""
        self.store.update_memory(memory_id, new_memory)
        
    def format_for_prompt(self, memories: List[Dict[str, Any]]) -> str:
        """Format retrieved memories cleanly for the LLM prompt."""
        if not memories:
            return "No relevant long-term memory found."
            
        formatted = []
        for m in memories:
            m_type = m['metadata'].get('type', 'fact')
            content = m['content']
            formatted.append(f"- [{m_type.upper()}] {content}")
            
        return "\n".join(formatted)
