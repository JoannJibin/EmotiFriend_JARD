"""
GPT client module for EmotiFriend.
Handles interactions with OpenAI's GPT-3.5-turbo API.
"""

import os
from typing import Optional
import openai
from dotenv import load_dotenv

class GPTClient:
    def __init__(self):
        """Initialize the GPT client with API key from environment."""
        load_dotenv()  # Load environment variables from .env file
        openai.api_key = os.getenv("OPENAI_API_KEY")
        if not openai.api_key:
            raise ValueError("OpenAI API key not found in environment variables")
        
        # Default system prompt for EmotiFriend
        self.default_system_prompt = """
        You are EmotiFriend, a helpful assistant that converts emoji and short text inputs 
        into natural, expressive sentences. Your responses should be:
        1. Respectful and empathetic
        2. Clear and grammatically correct
        3. Appropriate for the context
        4. Concise (1-2 sentences)
        
        If you receive emoji, interpret their meaning and create a natural sentence.
        If you receive text, enhance it into a complete, natural sentence while 
        maintaining the original meaning.
        """
    
    def process_input(self, user_input: str, system_prompt: Optional[str] = None) -> str:
        """
        Process user input through GPT-3.5-turbo and return a natural sentence.
        
        Args:
            user_input (str): User's emoji or text input
            system_prompt (str, optional): Custom system prompt to override default
            
        Returns:
            str: Generated natural sentence
        """
        messages = [
            {"role": "system", "content": system_prompt or self.default_system_prompt},
            {"role": "user", "content": user_input}
        ]
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=100,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            # Log the error and return a user-friendly message
            print(f"Error processing input: {e}")
            return "I'm having trouble understanding that right now. Could you try again?" 