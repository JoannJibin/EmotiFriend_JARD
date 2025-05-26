# EmotiFriend 🗣️

EmotiFriend is an AI-powered voice companion app designed to help non-verbal and speech-delayed individuals communicate through emoji or short text inputs. The app converts these into expressive, respectful sentences and reads them aloud using text-to-speech (TTS) technology.

## Features 🌟

- Emoji/text to speech conversion
- AI-powered sentence generation using GPT-3.5-turbo
- Offline and online text-to-speech capabilities
- Simple, accessible user interface
- Responsive design for mobile and desktop

## Installation 🔧

1. Clone this repository:
```bash
git clone https://github.com/yourusername/EmotiFriend.git
cd EmotiFriend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage 🚀

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:7860)

3. Enter emoji or text in the input field and click "Speak" to generate and hear the response

## Project Structure 📁

```
EmotiFriend/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── .env               # Environment variables (create this)
├── src/
│   ├── tts_engine.py  # Text-to-speech functionality
│   ├── gpt_client.py  # OpenAI GPT integration
│   └── ui.py          # Gradio UI components
└── README.md
```

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- OpenAI for GPT-3.5-turbo
- Gradio team for the UI framework
- pyttsx3 and gTTS for speech synthesis capabilities 