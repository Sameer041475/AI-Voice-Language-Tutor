# 🎙️ AI Voice Language Tutor

An AI-powered voice language learning application that helps users improve their **speaking, grammar, vocabulary, pronunciation, and overall language skills**.

The user speaks a sentence using the microphone. The application converts the speech into text using **Faster-Whisper**, analyzes the sentence using **Llama 3 through Ollama**, provides detailed grammar and vocabulary feedback, generates a corrected sentence, converts the corrected sentence back into speech using **gTTS**, and stores the practice session for progress tracking.

---
# 🎯DEMO
URL :- https://sameer041475-ai-voice-language-tutor-app-frh7qv.streamlit.app/
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

# ✨ Features

## 🎤 1. Voice Recording

Users can record their voice directly from the browser.

Features:

* Browser microphone support
* Start/stop recording
* Audio playback
* WAV audio processing

Example:

```text
🎤 Click to Record

"What is artificial intelligence and machine learning?"
```

---

## 📝 2. Speech-to-Text

The application uses **Faster-Whisper** to convert spoken audio into text.

Supported languages:

| Language | Whisper Code |
| -------- | ------------ |
| English  | `en`         |
| Hindi    | `hi`         |
| Spanish  | `es`         |
| French   | `fr`         |
| German   | `de`         |

Example:

```text
🎤 Audio
     ↓
Faster-Whisper
     ↓
"What is AI and ML?"
```

---

## 🤖 3. AI-Powered Language Analysis

The transcribed sentence is analyzed using an LLM.

The AI checks:

* Grammar
* Vocabulary
* Sentence structure
* Language quality
* Difficulty
* Overall performance

The current local setup uses:

```text
Ollama
   ↓
Llama 3
```

---

## ✍️ 4. Corrected Sentence

The AI generates a corrected version of the user's sentence.

Example:

```text
You said:

Yesterday I go to college.

Corrected:

Yesterday I went to college.
```

The correction attempts to preserve the original meaning while improving grammatical accuracy.

---

## 📚 5. Grammar Mistake Detection

The application identifies grammar mistakes and explains them.

Example:

```text
❌ I go

✅ I went

💡 "Yesterday" refers to a past event,
so the past-tense form "went" should be used.
```

This helps learners understand **why** a sentence is incorrect instead of simply showing the correct answer.

---

## 📖 6. Vocabulary Feedback

The AI provides feedback about vocabulary usage.

It can suggest:

* Better word choices
* More natural expressions
* Alternative vocabulary
* Improvements in sentence quality

---

## 📊 7. Performance Scoring

Each practice session receives scores from **0 to 10**.

The application tracks:

```text
Grammar Score
Vocabulary Score
Overall Score
```

Example:

```text
Grammar      8/10
Vocabulary   7/10
Overall      7.5/10
```

---

## 🎯 8. Difficulty Levels

Users can select:

```text
Beginner
Intermediate
Advanced
```

The AI also evaluates the difficulty of the sentence.

---

## 🔊 9. Text-to-Speech

The corrected sentence is converted into speech using **gTTS**.

Workflow:

```text
Corrected Sentence
       ↓
      gTTS
       ↓
   Audio Output
       ↓
      🔊
```

This allows the learner to listen to the corrected sentence.

---

## 📈 10. Progress Tracking

The application calculates the learner's average performance.

The Progress page displays:

```text
Grammar Average
Vocabulary Average
Overall Average
```

Example:

```text
Grammar      8.2/10
Vocabulary   7.6/10
Overall      7.9/10
```

---

## 🏆 11. Automatic Level Detection

The application determines the learner's current level based on their average overall score.

```text
Overall Score < 5
       ↓
   Beginner

5 ≤ Overall Score < 7.5
       ↓
 Intermediate

Overall Score ≥ 7.5
       ↓
   Advanced
```

---

## 📚 12. Practice History

Every completed practice session can be stored in the SQLite database.

History contains:

* Language
* Original sentence
* Corrected sentence
* Grammar score
* Vocabulary score
* Overall score
* Difficulty
* Date/time

Example:

```text
English | Score: 8.0/10 | 30-08-2026

You said:
I go to college yesterday.

Corrected:
I went to college yesterday.

Grammar: 8/10
Vocabulary: 8/10
Overall: 8/10
```

---

# 🏗️ System Architecture

```text
                       👤 USER
                         │
                         ▼
                  🎤 MICROPHONE
                         │
                         ▼
                ┌─────────────────┐
                │    Streamlit    │
                │      app.py     │
                └────────┬────────┘
                         │
                         ▼
                🎙️ Audio Recorder
                         │
                         ▼
              ┌─────────────────────┐
              │   Faster-Whisper    │
              │    Speech → Text    │
              └──────────┬──────────┘
                         │
                         ▼
                    📝 Transcript
                         │
                         ▼
              ┌─────────────────────┐
              │       Ollama        │
              │      Llama 3        │
              └──────────┬──────────┘
                         │
                         ▼
                  🤖 AI ANALYSIS
                         │
             ┌───────────┼───────────┐
             │           │           │
             ▼           ▼           ▼
          Grammar    Vocabulary    Overall
           Score       Score        Score
             │           │           │
             └───────────┼───────────┘
                         │
                         ▼
                  ✍️ CORRECTION
                         │
                         ▼
                  🔊 gTTS
                         │
                         ▼
                 Correct Pronunciation
                         │
                         ▼
                  💾 SQLite Database
                         │
                         ▼
                  📊 Progress/History
```

---

# 🛠️ Technologies Used

| Technology     | Purpose                   |
| -------------- | ------------------------- |
| Python         | Main programming language |
| Streamlit      | Web application UI        |
| Faster-Whisper | Speech-to-text            |
| Ollama         | Local LLM runtime         |
| Llama 3        | AI language analysis      |
| gTTS           | Text-to-speech            |
| SQLite         | Database                  |
| Requests       | API communication         |
| Git            | Version control           |
| GitHub         | Code hosting              |

---

# 📂 Project Structure

```text
AI-Voice-Language-Tutor/
│
├── app.py
├── ai_tutor.py
├── speech_to_text.py
├── text_to_speech.py
├── database.py
│
├── database/
│   └── ...
│
├── audio/
│   └── ...
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📄 File Description

## `app.py`

Main application file.

Responsible for:

* Streamlit interface
* Navigation
* Language selection
* Difficulty selection
* Audio recording
* Speech-to-text
* AI feedback
* Score display
* Progress page
* History page

---

## `speech_to_text.py`

Responsible for speech recognition.

```text
Audio File
    ↓
Faster-Whisper
    ↓
Transcribed Text
```

---

## `ai_tutor.py`

Responsible for AI analysis.

```text
User Sentence
      ↓
Ollama
      ↓
Llama 3
      ↓
AI Feedback
```

The response includes:

```text
Corrected Sentence
Grammar Score
Vocabulary Score
Overall Score
Grammar Mistakes
Vocabulary Feedback
Overall Feedback
Difficulty
```

---

## `text_to_speech.py`

Converts corrected text into audio.

```text
Text
 ↓
gTTS
 ↓
MP3 Audio
```

---

## `database.py`

Handles SQLite database operations.

Responsibilities:

* Create database
* Create tables
* Save practice sessions
* Retrieve practice history
* Calculate average scores

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/Sameer041475/AI-Voice-Language-Tutor.git
```

Move into the project:

```bash
cd AI-Voice-Language-Tutor
```

---

# 🐍 2. Create Virtual Environment

On Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

You should see:

```text
(.venv)
```

in your terminal.

---

# 📦 3. Install Dependencies

Make sure the file is named:

```text
requirements.txt
```

NOT:

```text
requirement.txt
```

Then run:

```powershell
python -m pip install -r requirements.txt
```

Example `requirements.txt`:

```text
streamlit
audio-recorder-streamlit
faster-whisper
gtts
requests
```

---

# 🧠 4. Install Ollama

The current version of the application uses Ollama for local AI inference.

Install Ollama on your computer.

Check the installation:

```powershell
ollama --version
```

Check installed models:

```powershell
ollama list
```

Download Llama 3 if necessary:

```powershell
ollama pull llama3
```

Run the model:

```powershell
ollama run llama3
```

You can test it with:

```text
Correct this sentence:

Yesterday I go to college.
```

Expected:

```text
Yesterday I went to college.
```

---

# ▶️ Running the Application

Activate your virtual environment:

```powershell
.venv\Scripts\activate
```

Run Streamlit:

```powershell
python -m streamlit run app.py
```

The application will open in your browser.

Usually:

```text
http://localhost:8501
```

---

# 🔄 Complete Application Workflow

## Step 1 — Select Language

Example:

```text
English
```

---

## Step 2 — Select Difficulty

Example:

```text
Intermediate
```

---

## Step 3 — Record Voice

Click:

```text
🎤 Click to Record
```

Speak:

```text
What is artificial intelligence and machine learning?
```

---

## Step 4 — Speech Recognition

Faster-Whisper converts the audio:

```text
Audio
 ↓
Whisper
 ↓
"What is artificial intelligence and machine learning?"
```

---

## Step 5 — AI Analysis

The sentence is sent to Llama 3 through Ollama.

The AI analyzes:

```text
Grammar
Vocabulary
Sentence structure
Difficulty
Overall quality
```

---

## Step 6 — Corrected Sentence

Example:

```text
You said:

I am learn machine learning.

Corrected:

I am learning machine learning.
```

---

## Step 7 — Feedback

The user receives:

```text
Grammar: 8/10
Vocabulary: 7/10
Overall: 8/10
```

and explanations for mistakes.

---

## Step 8 — Pronunciation

The corrected sentence is converted to speech:

```text
Corrected Sentence
       ↓
      gTTS
       ↓
      🔊 Audio
```

---

## Step 9 — Save Session

The session is saved into SQLite.

---

# 🗄️ Database Design

The application uses SQLite for local storage.

A practice session contains:

```text
ID
Language
Sentence
Corrected Sentence
Grammar Score
Vocabulary Score
Overall Score
Difficulty
Created At
```

Conceptually:

```text
Practice Session
│
├── Language
├── Original Sentence
├── Corrected Sentence
├── Grammar Score
├── Vocabulary Score
├── Overall Score
├── Difficulty
└── Created At
```

---

# 📊 Progress Calculation

The application calculates the average scores of completed sessions.

Example:

```text
Session 1 → 7/10
Session 2 → 8/10
Session 3 → 9/10
```

Average:

```text
(7 + 8 + 9) / 3 = 8
```

The progress page displays:

```text
Grammar      8.0/10
Vocabulary   7.6/10
Overall      8.0/10
```

---

# 🎯 Supported Languages

Currently supported:

```text
🇬🇧 English
🇮🇳 Hindi
🇪🇸 Spanish
🇫🇷 French
🇩🇪 German
```

More languages can be added later.

---

# 🎤 Speech-to-Text Accuracy

Speech recognition accuracy depends on:

* Microphone quality
* Background noise
* Internet/audio environment
* Speaking speed
* Pronunciation
* Whisper model size
* Selected language

For better accuracy, use a good microphone and speak clearly.

For faster CPU inference:

```python
WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)
```

For better accuracy:

```python
WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)
```

If a compatible NVIDIA GPU is available, Faster-Whisper can also use CUDA.

---

# ⚡ CPU vs GPU

The application can run on CPU.

CPU:

```python
device="cpu"
```

GPU:

```python
device="cuda"
```

Example:

```python
WhisperModel(
    "small",
    device="cuda",
    compute_type="float16"
)
```

A GPU can significantly improve Whisper inference speed when compatible NVIDIA CUDA hardware is available.

---

# 🔐 Security

Do not upload sensitive information to GitHub.

Never commit:

```text
.env
API keys
Passwords
Access tokens
Private credentials
```

Use `.gitignore` to prevent accidental uploads.

---

# 📄 `.gitignore`

Recommended:

```gitignore
# Virtual environment
.venv/
venv/
env/

# Python
__pycache__/
*.pyc
*.pyo

# Environment variables
.env

# Database
*.db
*.sqlite
*.sqlite3

# Generated audio
audio/

# IDE
.idea/
.vscode/
```

---

# 🚀 Deployment

The current application uses:

```text
Ollama → localhost:11434
```

This works when the application and Ollama are running on the same computer.

For example:

```text
Your Computer
│
├── Streamlit
│
└── Ollama
      │
      └── Llama 3
```

However, if Streamlit is deployed to a cloud server, that cloud server cannot access the Ollama instance running on your personal computer.

Therefore, the current local Ollama architecture is intended primarily for:

* Local development
* Demonstrations
* Educational use
* Portfolio development

For cloud deployment, the architecture should be changed to use a remotely accessible LLM service or separately hosted inference server.

Recommended production architecture:

```text
                 👤 USER
                    │
                    ▼
              Streamlit Cloud
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
     Faster-Whisper       Cloud LLM
          │                   │
          └─────────┬─────────┘
                    ▼
               AI Feedback
                    │
                    ▼
                  gTTS
                    │
                    ▼
              🔊 Audio Output
```

---

# 🌐 GitHub Setup

After creating the project:

```powershell
git init
```

Add the files:

```powershell
git add .
```

Commit:

```powershell
git commit -m "Initial AI Voice Language Tutor"
```

Rename the branch:

```powershell
git branch -M main
```

Add the GitHub repository:

```powershell
git remote add origin https://github.com/Sameer041475/AI-Voice-Language-Tutor.git
```

Push:

```powershell
git push -u origin main
```

For future changes:

```powershell
git add .
git commit -m "Update application"
git push
```

---

# 🐛 Troubleshooting

## `requirements.txt` not found

Make sure you are in the project directory:

```powershell
cd "C:\Users\Sameer kampa\voice assistent"
```

Check:

```powershell
dir
```

You should see:

```text
requirements.txt
```

Then:

```powershell
python -m pip install -r requirements.txt
```

---

## Streamlit command not found

Instead of:

```powershell
streamlit run app.py
```

use:

```powershell
python -m streamlit run app.py
```

---

## Ollama connection error

Check:

```powershell
ollama list
```

Then:

```powershell
ollama serve
```

Check that Llama 3 exists:

```powershell
ollama list
```

---

## Whisper transcription is incorrect

Try:

* Speaking slowly
* Reducing background noise
* Using a better microphone
* Selecting the correct language
* Using the `small` model instead of `base`
* Using a GPU if available

---

## Whisper is too slow

Use:

```python
WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)
```

A smaller model generally provides faster inference.

---

# 🔮 Future Improvements

## Version 1.0

* [x] Voice recording
* [x] Speech-to-text
* [x] AI grammar correction
* [x] Vocabulary feedback
* [x] Performance scoring
* [x] Text-to-speech
* [x] SQLite database
* [x] Progress tracking
* [x] Practice history
* [x] Multiple language selection

---

## Version 2.0

Planned features:

* [ ] User authentication
* [ ] User profiles
* [ ] Daily learning goals
* [ ] Learning streak
* [ ] Pronunciation scoring
* [ ] More languages
* [ ] Advanced progress charts
* [ ] Vocabulary history
* [ ] Personalized recommendations

---

## Version 3.0

Advanced features:

* [ ] Real-time AI conversation
* [ ] AI conversation partner
* [ ] Adaptive difficulty
* [ ] Personalized lessons
* [ ] AI-generated exercises
* [ ] Pronunciation analysis
* [ ] Speaking speed analysis
* [ ] Cloud database
* [ ] Cloud LLM
* [ ] Mobile-friendly interface

---

# 💡 Future Architecture

The long-term goal is to transform this project into a complete AI language-learning platform.

```text
                         👤 USER
                           │
                           ▼
                    🎙️ Voice Input
                           │
                           ▼
                  📝 Speech Recognition
                           │
                           ▼
                     🤖 AI Tutor
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               ▼               ▼
       Grammar         Vocabulary      Pronunciation
           │               │               │
           └───────────────┼───────────────┘
                           │
                           ▼
                    📊 Performance
                           │
                           ▼
                    🎯 Personalized
                       Learning
                           │
                           ▼
                     🔊 AI Voice
                           │
                           ▼
                       👤 USER
```

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

## Python

* Functions
* Modules
* File handling
* Exception handling
* JSON
* APIs
* Virtual environments

## Artificial Intelligence

* Large Language Models
* Generative AI
* Prompt engineering
* AI-based feedback
* Local LLM inference

## NLP

* Speech recognition
* Text processing
* Grammar analysis
* Vocabulary analysis
* Language correction

## Machine Learning

* Whisper models
* Model inference
* CPU/GPU inference

## Web Development

* Streamlit
* Interactive UI
* Audio input
* Application navigation

## Database

* SQLite
* SQL
* CRUD operations
* Persistent data

## Software Development

* Git
* GitHub
* Virtual environments
* Dependency management
* Application deployment

---

# 🌟 Why This Project?

This project combines multiple technologies into one practical AI application:

```text
Python
   +
Speech Recognition
   +
Generative AI
   +
Natural Language Processing
   +
Text-to-Speech
   +
Database
   +
Web Application
```

Instead of building only an AI model, this project demonstrates how to integrate AI into a complete user-facing application.

---

# 📸 Application Preview

Add screenshots of your application here.

Example:

```markdown
![Practice Page](screenshots/practice.png)

![Progress Page](screenshots/progress.png)

![History Page](screenshots/history.png)
```

Recommended folder:

```text
screenshots/
├── practice.png
├── progress.png
└── history.png
```

---

# 🎥 Demo

Add a demo video or GIF here when available.

```markdown
[▶️ Watch Project Demo](YOUR_DEMO_LINK)
```

---

# 📌 Project Status

```text
🟢 Active Development
```

Current version:

```text
v1.0
```

The project is currently focused on local development using:

```text
Streamlit
Faster-Whisper
Ollama
Llama 3
gTTS
SQLite
```

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Create a Pull Request

Example:

```bash
git checkout -b feature/new-feature
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

---

# 📜 License

This project is created for **educational, learning, and portfolio purposes**.

You are free to modify and improve the project according to your requirements.

---

# 👨‍💻 Author

## Sameer Kampa

CSE – Artificial Intelligence

Interested in:

* Artificial Intelligence
* Machine Learning
* Generative AI
* Python
* Full Stack Development
* Natural Language Processing

---

# ⭐ Support

If you find this project useful or interesting:

⭐ Star the repository

🍴 Fork the repository

🐛 Report bugs

💡 Suggest improvements

🤝 Contribute

---

# 📞 Project Summary

**AI Voice Language Tutor** is an AI-powered language-learning application that combines speech recognition, Generative AI, text-to-speech, and database technologies.

The application allows users to:

```text
🎤 Speak
   ↓
📝 Convert Speech to Text
   ↓
🤖 Analyze with AI
   ↓
✍️ Correct Grammar
   ↓
📚 Improve Vocabulary
   ↓
📊 Get Score
   ↓
🔊 Hear Correct Pronunciation
   ↓
💾 Track Progress
```

The goal of the project is to provide learners with an interactive AI tutor that gives **instant, personalized feedback through voice**.

````

### One correction before you paste it

Your actual file is currently named **`requirement.txt`**, according to the folder listing you showed me. Rename it first:

```powershell
Rename-Item requirement.txt requirements.txt
````

Then paste the README above into `README.md`.

After that:

```powershell
git add README.md requirements.txt .gitignore
git commit -m "Update project documentation"
git push
```
# THANK YOU👍
