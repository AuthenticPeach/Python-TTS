# Text-to-Speech (TTS) Application

## Overview

This Text-to-Speech (TTS) application is built using Python. It leverages Google Text-to-Speech (`gTTS`) for generating speech from text and `pydub` for audio manipulation, including speed adjustments. The application can generate speech in different languages and accents and allows for advanced voice customization using Amazon Polly.

## Features

- Convert text to speech using `gTTS`.
- Adjust the playback speed of the generated speech.
- Support for multiple languages and accents.
- Advanced voice customization with Amazon Polly.

## Requirements

- Python 3.x
- `gTTS` library
- `pydub` library
- `ffmpeg` and `ffprobe` executables

## Installation

1. **Install Python 3.x**

   Download and install Python from the official [Python website](https://www.python.org/downloads/).

2. **Install Required Libraries**

   Use `pip` to install the required libraries:
   ```bash
   pip install gtts pydub boto3

3. **Download FFmpeg**

Download FFmpeg from the FFmpeg website and extract it to a known directory (e.g., C:\ffmpeg).

4. **Add FFmpeg to System PATH**

Add the bin directory of FFmpeg to your system's PATH environment variable.