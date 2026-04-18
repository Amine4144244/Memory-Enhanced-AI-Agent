import sys
import os

# Ensure the root project directory is in the PYTHONPATH (memory-agent)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.agent.agent_core import MemoryEnhancedAgent
from app.config import GROQ_API_KEY
import time

def evaluate():
    if not GROQ_API_KEY:
        print("ERROR: GROQ_API_KEY could not be found.")
        return
        
    agent = MemoryEnhancedAgent()
    
    # Simple Conversation Simulation
    test_conversation = [
        "Hi, I'm Bob and I'm a machine learning engineer.",
        "I mostly work with PyTorch, but I want to learn more about JAX.",
        "Can you recommend a good tutorial for JAX?",
        "Actually, I just switched to a new team doing web development, so I need to learn React first.",
        "I'm setting up a Next.js project on Windows.",
        "What was my name again?",
        "Do you remember what my main goal is right now?"
    ]
    
    print("Evaluating Memory-Enhanced Agent...\n")
    for msg in test_conversation:
        print(f"User: {msg}")
        response = agent.chat(msg)
        print(f"Agent: {response}\n")
        # Give LTM some time to process synchronously though we did it sequentially
        time.sleep(1)
        
    print("\n--- Final Memory State ---")
    memories = agent.long_term.store.get_all()
    for mem in memories:
        print(f"[{mem['id']}] {mem['metadata']['type']} (Freq: {mem['metadata']['frequency']}, Conf: {mem['metadata']['confidence']}): {mem['content']}")
        
    print("\nEvaluation completed.")
    print("Metrics to observe manually:")
    print("1. Memory Recall: Did the agent remember the name 'Bob'?")
    print("2. Memory Update: Did the agent acknowledge the switch from ML/JAX to React/Next.js without contradiction?")

if __name__ == "__main__":
    evaluate()
