# 🧬 AI Character Description Generator

Generate creative, vivid character profiles using Streamlit and Mistral AI.

## 🧠 Features
- 🔠 Input name, role, traits, setting, age, and custom details
- 🧠 Powered by Mistral LLM (`mistral-large-latest`)
- 🖼️ Real-time, AI-generated character descriptions
- 🪄 Clean and responsive UI built with Streamlit
- 🔒 Secure API key management with `.env` or `secrets.toml`

## 📦 Requirements

### ✅ Python Version
Make sure you have **Python 3.8+** installed.

---

### ✅ Required Python Packages
  add all required packages in requirements.txt

 `streamlit`    
 `mistralai`    
 `python-dotenv`
---

## 🛠️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/KushalAgrawal30/LLAMA_char.git

# (Optional) create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

## ▶️ How to run
After setting up the API key:

```bash
streamlit run app.py
```