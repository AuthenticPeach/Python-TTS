from gtts import gTTS
from pydub import AudioSegment
import os

# Explicitly setting the path to ffmpeg and ffprobe
ffmpeg_path = r"C:\Users\travi\Downloads\ffmpeg-7.0.1\ffmpeg-7.0.1\bin"
AudioSegment.converter = os.path.join(ffmpeg_path, "ffmpeg.exe")
AudioSegment.ffprobe = os.path.join(ffmpeg_path, "ffprobe.exe")

def text_to_speech(text, speed=1.0, lang='en', tld='com'):
    try:
        # Generate speech
        tts = gTTS(text=text, lang=lang, tld=tld)
        temp_file = "temp_audio.mp3"
        tts.save(temp_file)
        print(f"Temporary audio file '{temp_file}' created.")
        
        # Load audio file
        audio = AudioSegment.from_file(temp_file)
        
        # Adjust speed
        if speed != 1.0:
            audio = audio.speedup(playback_speed=speed)
        
        # Save adjusted audio
        output_file = "output_audio.mp3"
        audio.export(output_file, format="mp3")
        
        # Clean up temporary file
        os.remove(temp_file)
        print(f"Temporary audio file '{temp_file}' removed.")
        
        return output_file

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    text = "Hello, this is a text-to-speech test."
    speed = 1.0  # Normal speed

    # Different languages and accents
    languages = [
        ('en', 'com'),  # English (US)
        ('en', 'co.uk'),  # English (UK)
    ]

    for lang, tld in languages:
        print(f"Generating speech for language: {lang}, tld: {tld}")
        output_file = text_to_speech(text, speed, lang, tld)
        if output_file:
            print(f"Generated speech saved as {output_file}")
        else:
            print("Failed to generate speech.")
