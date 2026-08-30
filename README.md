# 🎙️ AI Voice Language Tutor

An AI-powered voice language learning application that helps users improve their **speaking, grammar, vocabulary, pronunciation, and overall language skills**.

The user speaks a sentence using the microphone. The application converts the speech into text using **Faster-Whisper**, analyzes the sentence using **Llama 3 through Ollama**, provides detailed grammar and vocabulary feedback, generates a corrected sentence, converts the corrected sentence back into speech using **gTTS**, and stores the practice session for progress tracking.

---

## 📌 Project Overview

Learning a new language requires continuous speaking practice and immediate feedback.

Traditional language-learning applications often provide exercises, but they may not give personalized feedback on every sentence a learner speaks.

This project solves that problem by combining:

- 🎤 Voice recording
- 📝 Speech recognition
- 🤖 Generative AI
- 📚 Grammar analysis
- 📖 Vocabulary analysis
- 📊 Performance scoring
- 🔊 Text-to-speech
- 💾 Progress tracking

The application creates a complete learning loop:

```text
🎤 Speak
   ↓
📝 Speech-to-Text
   ↓
🤖 AI Analysis
   ↓
✍️ Correction
   ↓
📊 Score & Feedback
   ↓
🔊 Correct Pronunciation
   ↓
💾 Save Progress
