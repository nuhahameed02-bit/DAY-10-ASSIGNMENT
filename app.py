import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# 1. Load environment variables from the .env file
load_dotenv()

# 2. Get the Groq API Key from the environment
# (Make sure to put GROQ_API_KEY="your_key" in your .env file)
api_key = os.getenv("GROQ_API_KEY")

# Initialize the Groq client if the key exists
if api_key:
    client = Groq(api_key=api_key)
else:
    client = None

# 3. Web App UI Layout (Matches your design)
st.title("Study Notes Generator")
st.write("Type in a topic you want to learn, and let the AI break it down for you.")

# User Input Field
topic = st.text_input("What subject or topic are you studying?", placeholder="e.g., photosynthesis")

# 4. Generate Button Logic
if st.button("Generate Notes"):
    # Check if the user actually typed something
    if not topic.strip():
        st.warning("Please enter a topic or subject first!")
    
    # Check if the API key is missing
    elif not api_key:
        st.error("API Key missing! Please add GROQ_API_KEY to your .env file.")
        
    else:
        # Show a loading spinner while fetching the response
        with st.spinner("Generating your study notes... Please wait."):
            try:
                # System prompt to make sure the AI formats the output cleanly
                system_instruction = (
                    "You are an expert academic tutor. Create clear, detailed, and structured "
                    "study notes for a university student on the given topic. Use headings, "
                    "bullet points, and bold text for important definitions."
                )
                
                # Making the API Call to Groq using the free Llama 3 model
                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",  # Fast, highly accurate, and free tier model
                    messages=[
                        {"role": "system", "content": system_instruction},
                        {"role": "user", "content": f"Generate study notes for: {topic}"}
                    ],
                    temperature=0.7
                )
                
                # Extract the text response from the API result
                ai_response = completion.choices[0].message.content
                
                # Display the response on the Streamlit interface
                st.success("Notes Generated Successfully!")
                st.markdown("---")
                st.markdown(ai_response)
                
            except Exception as e:
                # Catch any unexpected API errors and display them cleanly
                st.error(f"Something went wrong with the API: {e}")
                
                