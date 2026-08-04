import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


api_key = os.getenv("GROQ_API_KEY")


if api_key:
    client = Groq(api_key=api_key)
else:
    client = None


st.title("Study Notes Generator")
st.write("Type in a topic you want to learn, and let the AI break it down for you.")


topic = st.text_input("What subject or topic are you studying?", placeholder="e.g., photosynthesis")


if st.button("Generate Notes"):
    
    if not topic.strip():
        st.warning("Please enter a topic or subject first!")
    
    
    elif not api_key:
        st.error("API Key missing! Please add GROQ_API_KEY to your .env file.")
        
    else:
        
        with st.spinner("Generating your study notes... Please wait."):
            try:
                
                system_instruction = (
                    "You are an expert academic tutor. Create clear, detailed, and structured "
                    "study notes for a university student on the given topic. Use headings, "
                    "bullet points, and bold text for important definitions."
                )
                
                
                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",   
                    messages=[
                        {"role": "system", "content": system_instruction},
                        {"role": "user", "content": f"Generate study notes for: {topic}"}
                    ],
                    temperature=0.7
                )
                
                
                ai_response = completion.choices[0].message.content
                
                
                st.success("Notes Generated Successfully!")
                st.markdown("---")
                st.markdown(ai_response)
                
            except Exception as e:
            
                st.error(f"Something went wrong with the API: {e}")
                
                