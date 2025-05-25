
# Real-time Hindi ASR API

This project provides a **real-time Automatic Speech Recognition (ASR) system** that can transcribe spoken Hindi audio using an optimized ONNX model. It includes:
- Async-compatible FastAPI-based transcription API
- Streaming transcription capability (for future extension)
- ONNX model optimization for fast inference
- Real-time audio file handling and transcription

## ✅ Features Implemented

- ✅ **ONNX Model Inference**: Transcribes audio files using an optimized ONNX model for improved performance.
- ✅ **Async API Endpoints**: FastAPI endpoints are asynchronous for concurrent request handling.
- ✅ **Real-time Transcription**: Allows .wav files to be transcribed on-the-fly.
- ✅ **CORS Support**: Allows cross-origin access for web frontend clients.
- ✅ **Audio Format Support**: Converts any sample rate to 16kHz.
- ✅ **Error Handling**: Catches and reports incorrect file formats and invalid model outputs.

## 🚫 Issues Encountered

- ❌ Inconsistent outputs due to missing or incorrect vocab mapping.
- ❌ ONNXRuntime optimization tooling issues: `onnxruntime-tools` is deprecated.
- ❌ FastAPI internal errors when writing audio files using async I/O incorrectly.

## 🔧 How it is Solved

- Used a manual greedy decoder with controlled vocab fallback.
- Replaced `onnxruntime-tools` with manual optimization setup.
- Used correct async-compatible file writing using `aiofiles.open()` in `async with` context.

## ⚠️ Known Limitations

- Currently supports only `.wav` audio sampled at or convertible to **16kHz**.
- Streaming transcription is partially implemented but not fully tested in production.
- Vocabulary for decoding is dummy (a-z + space), should be replaced with actual Hindi tokens.
- No GPU acceleration in ONNX inference for now.

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/hindi-asr-api.git
cd hindi-asr-api
```

### 2. Install Dependencies

Make sure you have Python 3.8+ and pip installed.

```bash
pip install -r requirements.txt
```

Example packages include:
```txt
fastapi
uvicorn
aiofiles
librosa
matplotlib
onnxruntime
```

### 3. Place Your ONNX Model

Put your model as `models/asr_model_optimized.onnx` in the `models/` directory.

### 4. Start the API Server

```bash
uvicorn main:app --reload
```

### 5. Test the API

#### Transcription Endpoint:

```bash
POST /transcribe/
File Upload: .wav file (16kHz preferred)
```

Returns:
```json
{ "transcription": "your transcribed text" }
```


## 🤔 Future Plans

- Add real-time streaming WebSocket endpoint.
- Support Hindi tokenization and CTC decoding.
- Add speaker diarization and emotion detection modules.
- GPU and mobile (ONNX Lite) deployment support.

