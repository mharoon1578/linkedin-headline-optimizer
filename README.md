# 🚀 LinkedIn Headline Optimizer

A simple **Streamlit app** that takes your current LinkedIn title/headline and rewrites it into **modern, impact-driven, results-oriented headlines** with the help of **Groq LLMs**.

Each optimized headline appears in a **text box with a native copy button**, so you can copy and paste directly into your LinkedIn profile.

---

## ✨ Features
- 🔑 Secure **Groq API key** input
- 📝 Input your current LinkedIn headline
- 🤖 Uses **Groq LLM (`llama-3.1-8b-instant`)** to rewrite your title
- 📊 Generates **5 optimized, outcome-driven headlines**
- 📋 Each headline comes with a **Streamlit-native copy button**
- 🎯 Headlines emphasize **solutions + outcomes**, not just buzzwords

---

## 🛠️ Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/mharoon1578/linkedin-headline-optimizer.git
   cd linkedin-headline-optimizer
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate    # Mac/Linux
   venv\Scripts\activate       # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚡ Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser (usually at `http://localhost:8501`).

3. Enter:
   - Your **Groq API key**
   - Your **current LinkedIn headline**

4. Click **Generate Headlines** to get 5 new optimized versions.  
   Each version will appear in a box with a **📋 Copy button**.

---

## 🔑 Example

### Input:
```
AI Developer | Agentic AI Developer | NLP, Prompt Engineering & Model Optimization | OpenAI, Gemini, Hugging Face, Groq | Automation Tools | LLM Applications
```

### Output (sample):
- `Building Agentic AI & LLM Systems that cut manual work by 40%+`
- `Designing AI Automation Tools that boost team efficiency by 2x`
- `Creating NLP-Powered Solutions that reduce support costs by 35%`
- `Developing AI Applications that drive faster automation`
- `Driving AI-Powered Innovation that boosts productivity 50%+`

---

## 📦 Requirements

- Python 3.9+
- [Streamlit](https://streamlit.io)
- [groq Python client](https://pypi.org/project/groq/)

Install with:
```bash
pip install streamlit groq
```

---

## 🚀 Deployment

You can deploy this app on:
- [Streamlit Cloud](https://streamlit.io/cloud)
- [Render](https://render.com)
- [Hugging Face Spaces](https://huggingface.co/spaces)  


---

## 🧑‍💻 Author

Built with ❤️ by Muhammad Haroon  
💼 Helping professionals create **impact-driven LinkedIn brands**
