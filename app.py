import os
import streamlit as st
from mistralai import Mistral
# from dotenv import load_dotenv

# load_dotenv()

# --- Mistral Setup ---
api_key = st.secrets["MISTRAL_API_KEY"] # Best practice: store your key in .streamlit/secrets.toml
model = "mistral-large-latest"

# Initialize Mistral Client
client = Mistral(api_key=api_key)
print(api_key)

# --- Character Generation Function ---
def generate_character_description(name, role, traits, setting, age, specific_details):
    prompt = f"""
You are a creative assistant helping generate fictional characters for novels or games.
Generate a concise but vivid character description with the following attributes:

- Name: {name}
- Role: {role}
- Personality Traits: {traits}
- Setting: {setting}
- Age: {age}
- Additional Details: {specific_details}

Provide a description that highlights their appearance, behavior, backstory, and what makes them unique.
"""

    response = client.chat.complete(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()

# --- Streamlit UI ---
st.title("🧬 AI-Powered Character Description Generator")
st.markdown("Generate unique, creative character descriptions using Mistral AI.")

name = st.text_input("🧍 Character Name")
role = st.text_input("🎭 Role / Occupation")
traits = st.text_input("💡 Personality Traits (comma separated)")
setting = st.text_input("🌍 Story Setting / World")
age = st.text_input("📅 Age")
specific_details = st.text_area("📝 Additional Details")

if st.button("Generate Description"):
    if not name or not role:
        st.warning("Please fill in at least a name and role.")
    else:
        with st.spinner("Generating character..."):
            result = generate_character_description(name, role, traits, setting, age, specific_details)
            st.subheader("🎨 Generated Character")
            st.write(result)
