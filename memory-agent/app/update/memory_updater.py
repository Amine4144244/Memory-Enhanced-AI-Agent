from typing import List, Tuple
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

from app.config import MemoryItem, GROQ_API_KEY, MODEL_NAME
from app.memory.long_term import LongTermMemory

CONTRADICTION_PROMPT = """
You are a memory resolution engine.
You are given an EXISTING memory and a NEW memory.
Determine if the NEW memory contradicts or supersedes the EXISTING memory.

EXISTING MEMORY:
{existing_memory}

NEW MEMORY:
{new_memory}

Answer with a JSON indicating if there is a contradiction, and if so, what the updated confidence of the EXISTING memory should be (typically lower, e.g., 0.1 or 0.0), or if it should be completely replaced.
"""

class ContradictionResolution(BaseModel):
    is_contradiction: bool = Field(..., description="True if the new memory contradicts or supersedes the existing one.")
    new_confidence_for_existing: float = Field(..., description="If contradiction, the new confidence score for the existing memory (0.0 to 1.0).")

class MemoryUpdater:
    def __init__(self, long_term_memory: LongTermMemory):
        self.ltm = long_term_memory
        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=MODEL_NAME,
            temperature=0.0
        ).with_structured_output(ContradictionResolution)
        self.prompt = PromptTemplate(template=CONTRADICTION_PROMPT, input_variables=["existing_memory", "new_memory"])
        
    def resolve_and_update(self, new_memories: List[MemoryItem]) -> None:
        """
        Check new memories against existing ones. If a contradiction is found, decay old memory.
        Then insert new memories.
        """
        for new_mem in new_memories:
            # Find semantically similar existing memories (high similarity thresholds)
            # We fetch top 3 to detect contradictions
            similar_mems = self.ltm.retrieve_relevant(new_mem.content, top_k=3, memory_type=new_mem.type)
            
            for sim_mem in similar_mems:
                if sim_mem["similarity"] < 0.7:  # Only check fairly similar items
                    continue
                    
                existing_content = sim_mem["content"]
                
                try:
                    chain = self.prompt | self.llm
                    resolution = chain.invoke({
                        "existing_memory": existing_content,
                        "new_memory": new_mem.content
                    })
                    
                    if resolution and resolution.is_contradiction:
                        # Decay existing memory
                        mem_id = sim_mem["id"]
                        
                        # Re-instantiate as MemoryItem to update
                        updated_old_mem = MemoryItem(
                            id=mem_id,
                            type=sim_mem["metadata"]["type"],
                            content=sim_mem["content"],
                            timestamp=sim_mem["metadata"]["timestamp"],
                            confidence=resolution.new_confidence_for_existing,
                            frequency=sim_mem["metadata"]["frequency"],
                            durability=sim_mem["metadata"]["durability"],
                            impact=sim_mem["metadata"]["impact"]
                        )
                        self.ltm.update_memory(mem_id, updated_old_mem)
                except Exception as e:
                    print(f"Error during memory contradiction check: {e}")
            
            # Finally, store the new memory (it will go through scoring threshold)
            self.ltm.process_and_store([new_mem])
