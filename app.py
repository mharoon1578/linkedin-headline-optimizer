import streamlit as st
import json
from groq import Groq

# --- Page Config ---
st.set_page_config(page_title="LinkedIn Headline Optimizer", page_icon="🚀")
st.title("🚀 LinkedIn Headline Optimizer")

# --- Groq API Key ---
api_key = st.text_input("🔑 Enter your Groq API Key", type="password")

if api_key:
    client = Groq(api_key=api_key)

    # --- User Input ---
    user_title = st.text_area("✍️ Enter your current LinkedIn title/headline:")

    if st.button("✨ Generate Headlines"):
        if not user_title.strip():
            st.warning("Please enter your current LinkedIn title first.")
        else:
            # Prompt for Groq
            prompt = f"""
You are a LinkedIn branding and positioning expert. 
Your task is to take a user's current LinkedIn title or headline 
and rewrite it into a modern, results-driven, impact-oriented headline 
that clearly shows what they build/do and the tangible value it provides. 

### Input:
{user_title}

### Instructions:
1. Rewrite the headline so it starts with a strong **action phrase** like:
   - "Building..."
   - "Creating..."
   - "Designing..."
   - "Developing..."
   - "Driving..."

2. Instead of just listing roles/skills, frame it as **solutions + outcomes**.  
3. Make it **concise but powerful** (max 120 characters).  
4. Use **metrics or outcome phrases** like "cut manual work by 40%+", "boost efficiency by 50%+", etc.  
5. Keep it professional, human-sounding, and **attention-grabbing**.  

### Output:
Give 5 different versions of the rewritten LinkedIn headline 
in **valid JSON** format like this:

{{
  "headlines": [
    "Headline 1",
    "Headline 2",
    "Headline 3",
    "Headline 4",
    "Headline 5"
  ]
}}
"""

            try:
                # Groq API Call
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                )

                raw_output = response.choices[0].message.content.strip()

                # Extract JSON safely
                if "```json" in raw_output:
                    raw_output = raw_output.split("```json")[1].split("```")[0].strip()
                elif "```" in raw_output:
                    raw_output = raw_output.split("```")[1].strip()

                data = json.loads(raw_output)

                # --- Display Results in code blocks with copy ---
                st.subheader("✅ Optimized LinkedIn Headlines")
                for i, headline in enumerate(data["headlines"], start=1):
                    st.code(headline, language="text")

            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")

else:
    st.info("👆 Please enter your Groq API Key to start.")
