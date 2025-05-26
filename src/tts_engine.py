"""
Text-to-speech engine module for EmotiFriend.
Supports both offline (pyttsx3) and online (gTTS) speech synthesis.
"""

import os
import tempfile
from typing import Optional
import pyttsx3
from gtts import gTTS

class TTSEngine:
    def __init__(self, use_offline: bool = True):
        """
        Initialize the TTS engine.
        
        Args:
            use_offline (bool): Whether to use offline TTS (True) or online gTTS (False)
        """
        self.use_offline = use_offline
        if use_offline:
            self.engine = pyttsx3.init()
            # Configure default properties
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 1.0)
        
    def set_voice_properties(self, rate: Optional[int] = None, volume: Optional[float] = None):
        """
        Set voice properties for offline TTS.
        
        Args:
            rate (int, optional): Speech rate (words per minute)
            volume (float, optional): Volume level (0.0 to 1.0)
        """
        if not self.use_offline:
            return
            
        if rate is not None:
            self.engine.setProperty('rate', rate)
        if volume is not None:
            self.engine.setProperty('volume', volume)
    
    def speak(self, text: str, lang: str = 'en') -> str:
        """
        Convert text to speech and return the path to the audio file.
        
        Args:
            text (str): Text to convert to speech
            lang (str): Language code (for gTTS)
            
        Returns:
            str: Path to the generated audio file
        """
        # Create a temporary file for the audio
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        temp_file.close()
        
        if self.use_offline:
            # For offline TTS, we need to save as wav first
            wav_path = temp_file.name.replace('.mp3', '.wav')
            self.engine.save_to_file(text, wav_path)
            self.engine.runAndWait()
            # TODO: Convert wav to mp3 if needed
            return wav_path
        else:
            # Use gTTS for online TTS
            tts = gTTS(text=text, lang=lang)
            tts.save(temp_file.name)
            return temp_file.name
    
    def cleanup(self, file_path: str):
        """
        Clean up temporary audio files.
        
        Args:
            file_path (str): Path to the audio file to delete
        """
        try:
            os.remove(file_path)
        except (OSError, FileNotFoundError):
            pass 