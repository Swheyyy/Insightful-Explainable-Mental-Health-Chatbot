# 🤖 Insightful: Explainable Mental Health Chatbot

> An open-source AI chatbot offering 24/7 anonymous emotional support with explainable, evidence-based guidance.

---

## 🌟 Overview

**Insightful** is an explainable mental health chatbot designed to provide warm, supportive, and anonymous emotional assistance anytime. It helps users process their thoughts, cope with emotional challenges, and explore helpful tools grounded in proven therapies like:

- 🧠 Cognitive Behavioral Therapy (CBT)
- 🧘 Mindfulness and breathing techniques
- 💪 Motivational coaching and thought reframing

Unlike generic chatbots, **Insightful** explains *why* it gives advice, helping users build trust and learn to support themselves better. It's a helpful companion for managing anxiety, stress, self-doubt, burnout, and emotional lows.

---

## 💡 Features

- 🧠 **Emotion Detection**: Understands the emotional tone of user messages (e.g., sad, happy, stressed).
- 🧰 **Evidence-Based Tools**: Recommends CBT, mindfulness, journaling, grounding, etc., with explanations.
- ❤️ **Supportive Tone**: Responds with empathy, encouragement, and a conversational coaching style.
- 🔍 **Explainability**: Clearly states *why* a certain technique is being suggested.
- ⚖️ **Ethically Grounded**: Reminds users it’s not a replacement for professional therapy and encourages real-world support when needed.
- 🔐 **Anonymous & Private**: No user login, no tracking.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — frontend interface
- [Ollama](https://ollama.com/) — local LLM backend (e.g., TinyLLaMA)
- Python subprocess integration
- Custom prompt engineering for empathy, psychology, and coaching

---

## 🚀 Setup Instructions

### 1. Install Dependencies

```bash
pip install streamlit
```
### 2. Install Ollama & TinyLLaMA

Follow instructions at: https://ollama.com

```bash
ollama pull tinyllama
```
### 3. Run the App

```bash
streamlit run app.py
```

Make sure Ollama is running in the background.
