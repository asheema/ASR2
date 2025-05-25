import pyttsx3
import torchaudio

def generate_tts_wav(text, filename):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"TTS audio saved to {filename}")

def resample_to_16k(input_path, output_path):
    waveform, sr = torchaudio.load(input_path)
    if sr != 16000:
        print(f"Resampling from {sr}Hz to 16000Hz")
        waveform = torchaudio.transforms.Resample(orig_freq=sr, new_freq=16000)(waveform)
        torchaudio.save(output_path, waveform, 16000)
        print(f"Resampled audio saved to {output_path}")
    else:
        print(f"Audio already at 16kHz, copying file to {output_path}")
        torchaudio.save(output_path, waveform, sr)

if __name__ == "__main__":
    # Repeat text to get approx 6 seconds speech duration
    tts_text = "Hello, this is a test audio generated for six seconds duration. " * 3

    raw_wav = "test_speech_6sec_raw.wav"
    final_wav = "test_speech_6sec_16k.wav"

    generate_tts_wav(tts_text, raw_wav)
    resample_to_16k(raw_wav, final_wav)

