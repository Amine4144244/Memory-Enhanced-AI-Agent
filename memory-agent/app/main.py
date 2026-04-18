import sys
import os

# Ensure the root project directory is in the PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.agent.agent_core import MemoryEnhancedAgent
from app.config import GROQ_API_KEY

def main():
    if not GROQ_API_KEY:
        print("ERROR: GROQ_API_KEY could not be found.")
        print("Please ensure it is set in your environment or in a .env file.")
        return

    print("========================================")
    print("🧠 Memory-Enhanced AI Agent Starting...")
    print("========================================")
    
    try:
        agent = MemoryEnhancedAgent()
    except Exception as e:
        print(f"Failed to initialize agent: {e}")
        return

    print("Agent ready. Type 'exit' or 'quit' to stop.")
    print("----------------------------------------")
    
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.strip().lower() in ['exit', 'quit']:
                print("Ending session. Goodbye!")
                break
                
            if not user_input.strip():
                continue
                
            response = agent.chat(user_input)
            print(f"\nAgent: {response}")
            
        except KeyboardInterrupt:
            print("\nEnding session. Goodbye!")
            break

if __name__ == "__main__":
    main()
