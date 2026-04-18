from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

from app.config import GROQ_API_KEY, MODEL_NAME
from app.memory.short_term import ShortTermMemory
from app.memory.long_term import LongTermMemory
from app.extraction.extractor import MemoryExtractor
from app.update.memory_updater import MemoryUpdater
from app.extraction.prompts import AGENT_REASONING_PROMPT

class MemoryEnhancedAgent:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=MODEL_NAME,
            temperature=0.7
        )
        
        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory()
        self.extractor = MemoryExtractor()
        self.updater = MemoryUpdater(self.long_term)
        
        self.reasoning_prompt = PromptTemplate(
            template=AGENT_REASONING_PROMPT,
            input_variables=["long_term_memory", "short_term_memory", "query"]
        )
        
    def chat(self, user_input: str) -> str:
        """
        Core Pipeline:
        1. Query -> Retrieve Long-Term
        2. Combine with Short-Term Context
        3. Generate Response
        4. Extract New Memories
        5. Update/Store Long-Term Context
        """
        
        # 1. Retrieve related long-term memories
        retrieved_memories = self.long_term.retrieve_relevant(user_input, top_k=5)
        formatted_ltm = self.long_term.format_for_prompt(retrieved_memories)
        
        # 2. Get short-term context
        formatted_stm = self.short_term.get_context()
        
        # 3. Generate response
        chain = self.reasoning_prompt | self.llm
        try:
            response = chain.invoke({
                "long_term_memory": formatted_ltm,
                "short_term_memory": formatted_stm,
                "query": user_input
            })
            assistant_reply = response.content
            
            # Update short term immediately
            self.short_term.add_message("user", user_input)
            self.short_term.add_message("assistant", assistant_reply)
            
            # 4 & 5. Extract and update memories in the background (synchronous here for simplicity)
            # Send latest chunk of conversation to extractor (e.g. last 4 messages to provide context)
            recent_context = self.short_term.get_context()
            extracted = self.extractor.extract_from_conversation(recent_context)
            if extracted:
                self.updater.resolve_and_update(extracted)
                
            return assistant_reply
            
        except Exception as e:
            return f"Error connecting to agent reasoning engine: {e}"
