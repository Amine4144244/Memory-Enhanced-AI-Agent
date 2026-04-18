from typing import List, Dict
import tiktoken

class ShortTermMemory:
    """
    A token-based sliding window for short-term conversation context.
    Unlike a naive message-count window, this ensures we never exceed
    the context window without arbitrarily cutting off long messages.
    """
    
    def __init__(self, max_tokens: int = 1500, model_name: str = "cl100k_base"):
        self.max_tokens = max_tokens
        # Using tiktoken for standard OpenAI-like token counting
        # For LLaMA it might differ slightly, but this is a good proxy.
        try:
            self.tokenizer = tiktoken.get_encoding(model_name)
        except ValueError:
            self.tokenizer = tiktoken.get_encoding("cl100k_base")
            
        self.messages: List[Dict[str, str]] = []
        
    def _count_tokens(self, text: str) -> int:
        return len(self.tokenizer.encode(text))
        
    def add_message(self, role: str, content: str):
        """Add a new message and slide window if necessary."""
        self.messages.append({"role": role, "content": content})
        self._slide_window()
        
    def _slide_window(self):
        """Remove oldest messages until total tokens <= max_tokens."""
        total_tokens = sum(self._count_tokens(m["content"]) for m in self.messages)
        
        while total_tokens > self.max_tokens and len(self.messages) > 1:
            # We never remove the very last message if it alone exceeds the window,
            # though ideally we would chunk it. Here we just pop the oldest.
            removed_msg = self.messages.pop(0)
            total_tokens -= self._count_tokens(removed_msg["content"])
            
    def get_context(self) -> str:
        """Returns the formatted conversation context."""
        formatted_msgs = []
        for msg in self.messages:
            role = "User" if msg["role"] == "user" else "Assistant"
            formatted_msgs.append(f"{role}: {msg['content']}")
        return "\n".join(formatted_msgs)
        
    def clear(self):
        self.messages = []
