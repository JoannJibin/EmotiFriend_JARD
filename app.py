"""
EmotiFriend - Main Application
An AI-powered voice companion app with PDF Q&A capabilities.
"""

import os
from src.gpt_client import GPTClient
from src.tts_engine import TTSEngine
from src.ui import EmotiFriendUI

def main():
    """Initialize and launch the EmotiFriend application."""
    try:
        # Initialize components
        gpt_client = GPTClient()
        tts_engine = TTSEngine(use_offline=True)
        
        # Create UI
        ui = EmotiFriendUI(gpt_client, tts_engine)
        interface = ui.create_interface()
        
        # Launch the interface with custom configuration
        interface.launch(
            share=False,  # Set to True to create a public URL
            server_name="0.0.0.0",  # Listen on all network interfaces
            server_port=7860,  # Default Gradio port
            show_error=True,
            height=800,  # Set a fixed height for the interface
            width="100%"  # Use full width
        )
        
    except Exception as e:
        print(f"Error starting EmotiFriend: {e}")
        if "OPENAI_API_KEY" not in os.environ:
            print("\nMake sure to set your OpenAI API key!")
            print("The API key should be provided in the environment or in a .env file.")

if __name__ == "__main__":
    main() 