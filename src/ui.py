"""
UI module for EmotiFriend.
Creates a Gradio interface with a Pinterest-inspired design.
"""

import gradio as gr
from typing import Tuple
import os
from pathlib import Path

class EmotiFriendUI:
    def __init__(self, gpt_client, tts_engine):
        """
        Initialize the UI with GPT and TTS components.
        
        Args:
            gpt_client: Instance of GPTClient
            tts_engine: Instance of TTSEngine
        """
        self.gpt_client = gpt_client
        self.tts_engine = tts_engine
        self.current_audio_file = None
        
    def process_input(self, text: str, use_offline_tts: bool) -> Tuple[str, str]:
        """
        Process user input and generate text and speech output.
        
        Args:
            text (str): User's emoji or text input
            use_offline_tts (bool): Whether to use offline TTS
            
        Returns:
            Tuple[str, str]: Generated text and path to audio file
        """
        # Clean up previous audio file if it exists
        if self.current_audio_file:
            self.tts_engine.cleanup(self.current_audio_file)
        
        # Process input through GPT
        generated_text = self.gpt_client.process_input(text)
        
        # Generate speech
        self.tts_engine.use_offline = use_offline_tts
        audio_path = self.tts_engine.speak(generated_text)
        self.current_audio_file = audio_path
        
        return generated_text, audio_path
    
    def create_interface(self) -> gr.Blocks:
        """
        Create and configure the Gradio interface with Pinterest-inspired design.
        
        Returns:
            gr.Blocks: Configured Gradio interface
        """
        # Custom CSS for Pinterest-like styling
        custom_css = """
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .gr-button { border-radius: 20px !important; }
        .gr-box { border-radius: 15px !important; box-shadow: 0 4px 8px rgba(0,0,0,0.1) !important; }
        .gr-input { border-radius: 10px !important; }
        .gr-form { background-color: #fff !important; }
        .gr-padded { padding: 20px !important; }
        """
        
        with gr.Blocks(title="EmotiFriend", theme=gr.themes.Soft(), css=custom_css) as interface:
            with gr.Row():
                gr.Markdown("""
                # ✨ EmotiFriend
                Your AI-powered voice companion that brings communication to life!
                """)
            
            with gr.Row():
                with gr.Column(scale=1):
                    input_text = gr.Textbox(
                        label="Express Yourself",
                        placeholder="Type emoji or text here... (e.g., 😊 or 'happy')",
                        lines=3
                    )
                    use_offline = gr.Checkbox(
                        label="Use Offline Voice (Faster)",
                        value=True
                    )
                    speak_btn = gr.Button("🎙️ Speak!", variant="primary")
                
                with gr.Column(scale=1):
                    output_text = gr.Textbox(
                        label="Generated Message",
                        lines=3,
                        interactive=False
                    )
                    audio_output = gr.Audio(
                        label="Voice Output",
                        type="filepath"
                    )
            
            with gr.Row():
                gr.Examples(
                    examples=[
                        ["😊 feeling good", True],
                        ["😢 need help", True],
                        ["🎮 want to play", True],
                        ["🍕 hungry", True]
                    ],
                    inputs=[input_text, use_offline],
                    label="Quick Expressions"
                )
            
            # Set up event handlers
            speak_btn.click(
                fn=self.process_input,
                inputs=[input_text, use_offline],
                outputs=[output_text, audio_output]
            )
        
        return interface 