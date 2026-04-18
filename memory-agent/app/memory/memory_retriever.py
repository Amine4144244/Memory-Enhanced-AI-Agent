from typing import List, Dict, Any
from datetime import datetime
import os

from app.config import (
    RETRIEVAL_WEIGHT_SIMILARITY,
    RETRIEVAL_WEIGHT_IMPORTANCE,
    RETRIEVAL_WEIGHT_RECENCY,
    RETRIEVAL_WEIGHT_FREQUENCY
)
from app.memory.memory_scorer import calculate_importance_score

def calculate_time_decay(timestamp_str: str) -> float:
    """Calculate recency score (1.0 = brand new, approaching 0.0 for very old)."""
    try:
        mem_time = datetime.fromisoformat(timestamp_str)
        now = datetime.utcnow()
        delta_days = max(0.1, (now - mem_time).days + (now - mem_time).seconds / 86400.0)
        # Decay function: drops off smoothly
        # Recency score is 1 / (1 + log(1 + delta_days))
        import math
        return 1.0 / (1.0 + math.log(1.0 + delta_days))
    except (ValueError, TypeError):
        return 0.5

def score_and_rank_memories(retrieved_memories: List[Dict[str, Any]], top_k: int = 5) -> List[Dict[str, Any]]:
    """
    Implements the Hybrid Memory Recall formula:
        0.5 * similarity + 
        0.2 * importance + 
        0.2 * recency + 
        0.1 * frequency
    """
    scored_memories = []
    
    for mem in retrieved_memories:
        meta = mem["metadata"]
        
        sim_score = mem["similarity"]
        
        # Recalculate baseline importance
        importance_score = calculate_importance_score(
            durability=meta.get("durability", 0.5),
            impact=meta.get("impact", 0.5),
            frequency=meta.get("frequency", 1),
            confidence=meta.get("confidence", 0.8)
        )
        
        recency_score = calculate_time_decay(meta.get("timestamp", datetime.utcnow().isoformat()))
        
        # Normalize freq for retrieval
        freq = meta.get("frequency", 1)
        norm_freq = min(freq / 5.0, 1.0)
        
        final_score = (
            (RETRIEVAL_WEIGHT_SIMILARITY * sim_score) +
            (RETRIEVAL_WEIGHT_IMPORTANCE * importance_score) +
            (RETRIEVAL_WEIGHT_RECENCY * recency_score) +
            (RETRIEVAL_WEIGHT_FREQUENCY * norm_freq)
        )
        
        mem["hybrid_score"] = final_score
        scored_memories.append(mem)
        
    # Sort descending by hybrid_score
    scored_memories.sort(key=lambda x: x["hybrid_score"], reverse=True)
    return scored_memories[:top_k]
