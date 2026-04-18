from app.config import (
    WEIGHT_DURABILITY, 
    WEIGHT_IMPACT, 
    WEIGHT_FREQUENCY, 
    WEIGHT_CONFIDENCE,
    MEMORY_SCORE_THRESHOLD
)

def calculate_importance_score(durability: float, impact: float, frequency: int, confidence: float) -> float:
    """
    Calculate the baseline importance of a memory for long-term storage validation.
    """
    norm_freq = min(frequency / 5.0, 1.0)
    score = (
        (WEIGHT_DURABILITY * durability) +
        (WEIGHT_IMPACT * impact) +
        (WEIGHT_FREQUENCY * norm_freq) +
        (WEIGHT_CONFIDENCE * confidence)
    )
    return score

def should_store_memory(durability: float, impact: float, frequency: int, confidence: float) -> bool:
    """
    Determines if a memory crosses the threshold to be saved in long-term storage.
    """
    score = calculate_importance_score(durability, impact, frequency, confidence)
    return score >= MEMORY_SCORE_THRESHOLD
