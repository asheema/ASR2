from gtts import gTTS
from pydub import AudioSegment

# Step 1: Hindi text long enough to last ~6 seconds
hindi_text = "नमस्ते, यह एक छह सेकंड का परीक्षण ऑडियो है जो हिंदी भाषा में है। कृपया इसे सुने और पहचानें।"

# Step 2: Generate Hindi TTS audio
tts = gTTS(text=hindi_text, lang='hi')
tts.save("hindi_tts.mp3")

# Step 3: Convert MP3 to WAV and set sample rate to 16kHz, mono
audio = AudioSegment.from_mp3("hindi_tts.mp3")
audio = audio.set_frame_rate(16000).set_channels(1)

# Optional: Trim or pad to exactly 6 seconds
target_duration_ms = 6000
if len(audio) < target_duration_ms:
    silence = AudioSegment.silent(duration=target_duration_ms - len(audio))
    audio = audio + silence
else:
    audio = audio[:target_duration_ms]

# Step 4: Export final WAV
audio.export("hindi_test_6sec_16k.wav", format="wav")
print("✅ Hindi 6-sec WAV saved as 'hindi_test_6sec_16k.wav'")

