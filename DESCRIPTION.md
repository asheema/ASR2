
# Hindi ASR API Project – Detailed Description

## 📌 Project Overview

This project implements a **real-time Hindi Automatic Speech Recognition (ASR) API** using FastAPI, an ONNX-optimized model, and various powerful features including audio visualization and async-compatible inference. The goal is to provide an efficient, responsive, and accurate speech transcription service with enhancements for performance and usability.

---

## ✅ Features Implemented

1. **Real-time Transcription via FastAPI**:
   - Users can upload `.wav` audio files and receive Hindi text transcriptions.
   - Supports async inference for scalability and responsiveness.

2. **ONNX Model Optimization**:
   - Optimized the trained ASR model using ONNX to reduce inference latency.
   - Improved inference speed using `onnxruntime` CPU execution provider.
   - To improve inference speed and reduce latency, we optimized our speech recognition model using ONNX (Open Neural Network    Exchange). - This enables efficient deployment without requiring a heavy deep learning framework at runtime.

✅ What I Did:
Exported a pre-trained ASR model to the ONNX format using torch.onnx.export.

Removed the need for onnxruntime-tools by manually ensuring input shapes, opset versions, and data types are compatible with ONNX Runtime.

Loaded the ONNX model via onnxruntime.InferenceSession with CPUExecutionProvider, ensuring compatibility even in minimal Docker environments.

 Benefits:
✅ Faster inference with lower memory footprint.

✅ Avoids PyTorch/TensorFlow overhead in production.

✅ Portable model format that works across environments.

🔄 Async-Compatible Inference
To allow non-blocking, real-time transcriptions in our FastAPI application, the model inference was wrapped in an asynchronous-compatible format.

✅ What I
 Did:
Used Python’s asyncio and sloop.run_in_executor to run the blocking ONNX model inference (session.run(...)) without freezing the FastAPI server.

This enables the server to handle multiple concurrent requests efficiently, especially useful for web-scale or batch processing workloads.

python
Copy
Edit
async def transcribe_audio_async(audio_array, sample_rate=16000):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, transcribe_audio, audio_array, sample_rate)
🔍 Benefits:
⚡️ Real-time, concurrent audio transcription.

🚀 Improved responsiveness for simultaneous users.

🧠 Scales well with FastAPI’s async-first architecture.



3. **Streaming ASR Compatibility (Partial Result Ready)**:
   - Basic architecture supports integration with streaming inference for live transcriptions.

4. **CORS Support**:
   - Fully CORS-enabled backend for frontend integration.

5. **Support for 16kHz WAV Files**:
   - Validates audio to match expected format and resamples if needed.

6. **Async-compatible Model Inference Pipeline**:
   - Offloads model inference to executor for non-blocking async integration.

7. **Custom Greedy Decoder**:
   - Converts model logits into human-readable transcription.

---

## ⚠️ Issues Encountered During Development

- `onnxruntime-tools` dependency led to errors (fixed by manually optimizing model).
- Input shape mismatches between the model and ONNX runtime required consistent tensor formatting.
- Limited support for streaming inference via ONNX without complex model restructuring.
- Corrupted or incorrectly sampled audio (non-16kHz) often caused decoding errors or poor results.
- FastAPI returned `?` when vocabulary tokens were not mapped correctly.

---

## 🚫 Limitations Faced

- Real-time **partial streaming transcription** is conceptually implemented but requires server-sent events (SSE) or WebSockets for actual deployment.
- Vocabulary is manually mapped and may not match actual model tokenizer.
- Accuracy may vary if the model is not trained specifically on high-quality Hindi datasets.
- Large audio files (>30 seconds) can impact memory and inference speed.

---

## 🔧 How Addressed the Challenges

- Replaced broken dependencies (`onnxruntime-tools`) with native ONNX export and runtime logic.
- Added async wrappers using `loop.run_in_executor()` to enable concurrency.
- Ensured strict audio pre-processing using `librosa` and sample rate validation (16kHz).
- Added robust error messages and fallbacks for malformed input.

---

## 🚫 Known Limitations and Assumptions

- Assumes `.wav` input is mono-channel, 16-bit PCM, and sampled at 16kHz.
- The vocabulary is manually constructed – should be replaced with model’s tokenizer for full coverage.
- Streaming ASR with partial results is still under enhancement; current version transcribes after full upload.
- ONNX optimization may not support all model architectures without fine-tuning export ops.

---
 Docker Integration
To ensure consistent deployment across environments, a Dockerfile can be added to containerize the FastAPI-based Hindi ASR service. This makes it easier to run the application without worrying about system-level dependencies.

🔧 Key Components of the Dockerfile:
Base Image: Uses a lightweight Python 3.10+ image.

Dependencies: Installs FastAPI, uvicorn, onnxruntime, librosa, matplotlib, aiofiles, and other required packages via requirements.txt.

Working Directory: Sets up the app directory and copies necessary files like model weights, Python scripts, and .wav inputs (if applicable).

Port Exposure: Typically exposes port 8000 to serve the FastAPI application.

Entrypoint: Uses uvicorn main:app --host 0.0.0.0 --port 8000 to start the API server.


asr_project/
├──
│   ├── main.py                  # FastAPI entrypoint with endpoints for ASR and visualization
│   ├── asr_infer.py             # Async-capable ASR inference pipeline with ONNX optimization
│   ├── model.py                 # Model definition and helper functions (if used in non-ONNX mode)
│   └── optimization.py          # ONNX model optimization utility
│
├── models/
│   └── asr_model_optimized.onnx # Optimized ONNX model for inference
│
├
│
│
├── requirements.txt             # List of Python dependencies
├── Dockerfile                   # Dockerfile to containerize the application
├── README.md                    # Setup and usage instructions
├── DESCRIPTION.md               # Project overview, challenges, features
└── .gitignore                   # Files/folders to exclude from Git
🔍 Key Descriptions:
main.py: Hosts FastAPI endpoints like /transcribe/ and /visualize/. Handles CORS and async I/O.

asr_infer.py: Loads the ONNX model, transcribes audio with optimized inference, and performs greedy decoding.

optimization.py: Provides ONNX model conversion and optimization (without onnxruntime-tools).

models/: Stores the exported and optimized .onnx speech recognition model.

static/: Stores output images or audio for visualization endpoints.

Dockerfile: Allows containerized deployment using Docker.

requirements.txt: All the required packages for local or containerized environments.

.md files: Documentation for setup, usage, features, and known issues.


## 📈 Future Enhancements

- Integrate WebSocket-based real-time streaming ASR.
- Add model tokenizer-aware decoding (beam search/CTC prefix decoding).
- Improve language model integration for post-processing predictions.
- Host on scalable cloud platforms with GPU/TPU inference options.

---

##  How It Works

1. A `.wav` file is uploaded via a FastAPI endpoint.
2. The backend verifies format and reads audio using `librosa`.
3. The audio array is passed to the async ONNX inference pipeline.
4. Greedy decoder converts logits to human-readable Hindi transcription.
5. A JSON response returns the transcription.
6. Optional endpoint provides a waveform PNG visualization of the audio.

---

Built with  using Python, FastAPI, ONNX, and Librosa.
