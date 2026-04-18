import chromadb
from chromadb.config import Settings
import uuid
from typing import List, Dict, Any, Optional
from app.config import CHROMA_PERSIST_DIR, MemoryItem

from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

class MemoryStore:
    def __init__(self, collection_name: str = "long_term_memory"):
        self.client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
        
        # Use sentence-transformers explicitly instead of Chroma's slow ONNX fallback
        # This resolves the ReadTimeout during initial ONNX download
        embedding_func = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_func,
            metadata={"hnsw:space": "cosine"} # Use cosine similarity
        )
        
    def add_memory(self, memory: MemoryItem) -> str:
        """Add a new memory item to the store."""
        memory_id = str(uuid.uuid4())
        
        # We store scalars in metadata to allow filtering and retrieval weighting
        self.collection.add(
            ids=[memory_id],
            documents=[memory.content],
            metadatas=[{
                "type": memory.type,
                "confidence": memory.confidence,
                "frequency": memory.frequency,
                "durability": memory.durability,
                "impact": memory.impact,
                "timestamp": memory.timestamp.isoformat()
            }]
        )
        return memory_id
        
    def update_memory(self, memory_id: str, memory: MemoryItem):
        """Update an existing memory."""
        self.collection.update(
            ids=[memory_id],
            documents=[memory.content],
            metadatas=[{
                "type": memory.type,
                "confidence": memory.confidence,
                "frequency": memory.frequency,
                "durability": memory.durability,
                "impact": memory.impact,
                "timestamp": memory.timestamp.isoformat()
            }]
        )
        
    def query_similar(self, query: str, n_results: int = 10, memory_type: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Naive semantic search. 
        Returns documents, metadatas, and distances (converted to similarity).
        """
        where = {"type": memory_type} if memory_type else None
        
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where
        )
        
        retrieved_memories = []
        if not results["ids"] or not results["ids"][0]:
            return retrieved_memories
            
        for i in range(len(results["ids"][0])):
            mem_id = results["ids"][0][i]
            document = results["documents"][0][i]
            metadata = results["metadatas"][0][i]
            distance = results["distances"][0][i]
            
            # Convert cosine distance to similarity score (1 - distance)
            # Chroma returns distance where 0 is exact match
            similarity = max(0.0, 1.0 - distance)
            
            retrieved_memories.append({
                "id": mem_id,
                "content": document,
                "metadata": metadata,
                "similarity": similarity
            })
            
        return retrieved_memories
        
    def get_all(self) -> List[Dict[str, Any]]:
        """Retrieve all memories (for evaluation and summarization)."""
        results = self.collection.get()
        memories = []
        if not results["ids"]:
            return memories
            
        for i in range(len(results["ids"])):
            memories.append({
                "id": results["ids"][i],
                "content": results["documents"][i],
                "metadata": results["metadatas"][i]
            })
        return memories
