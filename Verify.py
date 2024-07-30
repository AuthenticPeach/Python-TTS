from gtts import gTTS
from pydub import AudioSegment


try:
    from gtts import gTTS
    from pydub import AudioSegment
    print("Libraries imported successfully.")
except ModuleNotFoundError as e:
    print(f"Error: {e}")
