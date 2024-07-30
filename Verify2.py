import os
import subprocess

# Set the correct path to ffmpeg and ffprobe
ffmpeg_path = r"C:\Users\travi\Downloads\ffmpeg-7.0.1\ffmpeg-7.0.1\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_path

# Explicitly setting the path to ffmpeg and ffprobe
ffmpeg_executable = os.path.join(ffmpeg_path, "ffmpeg.exe")
ffprobe_executable = os.path.join(ffmpeg_path, "ffprobe.exe")

# Check if ffmpeg is accessible
try:
    subprocess.run([ffmpeg_executable, "-version"], check=True)
    print("ffmpeg is accessible.")
except subprocess.CalledProcessError as e:
    print("ffmpeg is not accessible:", e)
except FileNotFoundError:
    print("ffmpeg executable not found.")

# Check if ffprobe is accessible
try:
    subprocess.run([ffprobe_executable, "-version"], check=True)
    print("ffprobe is accessible.")
except subprocess.CalledProcessError as e:
    print("ffprobe is not accessible:", e)
except FileNotFoundError:
    print("ffprobe executable not found.")
