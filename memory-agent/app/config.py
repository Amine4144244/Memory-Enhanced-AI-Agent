from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# --- Configuration Values ---
# Threshold for a memory to be saved in long-term storage
MEMORY_SCORE_THRESHOLD = 0.6

# Weightings for memory scoring
WEIGHT_DURABILITY = 0.4
WEIGHT_IMPACT = 0.3
WEIGHT_FREQUENCY = 0.2
WEIGHT_CONFIDENCE = 0.1

# Weightings for memory retrieval
RETRIEVAL_WEIGHT_SIMILARITY = 0.5
RETRIEVAL_WEIGHT_IMPORTANCE = 0.2
RETRIEVAL_WEIGHT_RECENCY = 0.2
RETRIEVAL_WEIGHT_FREQUENCY = 0.1

# ChromaDB persistence directory
CHROMA_PERSIST_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "chroma_db")

# LLM Config
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"

# --- Models ---
class MemoryItem(BaseModel):
    id: Optional[str] = None  # Will be assigned by ChromaDB
    type: str = Field(..., description="The type of memory: preference, goal, skill, decision, constraint, etc.")
    content: str = Field(..., description="The highly valuable extracted fact or knowledge.")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="When the memory was last updated/recorded.")
    
    # Metrics
    confidence: float = Field(default=0.8, ge=0.0, le=1.0, description="Confidence in this memory's accuracy.")
    frequency: int = Field(default=1, ge=1, description="How many times this information was mentioned/confirmed.")
    durability: float = Field(default=0.5, ge=0.0, le=1.0, description="How relevant is this across sessions (1.0 = highly durable).")
    impact: float = Field(default=0.5, ge=0.0, le=1.0, description="How much this affects future responses (1.0 = high impact).")
    
    def get_importance_score(self) -> float:
        """Calculate importance score based on the formula."""
        # Normalize frequency for scoring, cap at e.g., 5 to avoid overpowering
        norm_freq = min(self.frequency / 5.0, 1.0)
        return (
            (WEIGHT_DURABILITY * self.durability) +
            (WEIGHT_IMPACT * self.impact) +
            (WEIGHT_FREQUENCY * norm_freq) +
            (WEIGHT_CONFIDENCE * self.confidence)
        )
