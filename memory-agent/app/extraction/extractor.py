from typing import List
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from app.config import MemoryItem, GROQ_API_KEY, MODEL_NAME
from app.extraction.prompts import EXTRACTION_PROMPT_TEMPLATE
import os

class MemoryExtractor:
    def __init__(self):
        # We enforce structured output using Pydantic
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is missing from environment/config.")
            
        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=MODEL_NAME,
            temperature=0.0 # Strict extraction
        )
        
        # Pydantic structured output binding requires Pydantic v2
        # We instruct the model to return a list of MemoryItem
        self.structured_llm = self.llm.with_structured_output(MemoryExtractionResult)
        
        self.prompt = PromptTemplate(
            template=EXTRACTION_PROMPT_TEMPLATE,
            input_variables=["conversation"]
        )

    def extract_from_conversation(self, conversation_text: str) -> List[MemoryItem]:
        """
        Analyze conversation and extract high-value memories.
        """
        if not conversation_text.strip():
            return []
            
        chain = self.prompt | self.structured_llm
        try:
            result = chain.invoke({"conversation": conversation_text})
            if result and hasattr(result, "memories"):
                return result.memories
            return []
        except Exception as e:
            print(f"Extraction error: {e}")
            return []

# Wrapper model because LangChain structured output works better with a single root model
from pydantic import BaseModel, Field
class MemoryExtractionResult(BaseModel):
    memories: List[MemoryItem] = Field(default_factory=list, description="List of extracted long-term memories.")
