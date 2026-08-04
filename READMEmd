# Epochs '26 - Assignment 10: AI Application Build

# AI Study Assistant

# Student Details
* Name:Nuha c
* MUID:nuha-2@mulearn

# AI Study Assistant

---

## Proof of Implementation
* **Live Deployment Link:** [https://day-10-assignment-ewwdhwyqeja65ydm4jbyyb.streamlit.app/](https://day-10-assignment-ewwdhwyqeja65ydm4jbyyb.streamlit.app/)

---

## Project Overview
This project is a simple web app built to help students study more efficiently. When you type in any topic you're trying to learn (like "photosynthesis"), the app generates organized study notes with clear definitions, key concepts, and bullet points.

---

## Chosen Use Case
**AI Study Assistant / Note Generator**  
Turning textbook chapters or complex subjects into quick revision notes takes a lot of time. This app automates that breakdown so students can review key points fast during exam prep.

---

## AI Platform & Model Used
* **Frontend:** Streamlit  
* **API Provider:** Groq Cloud API  
* **LLM Model:** `llama-3.1-8b-instant`  
* **Python Libraries:** `streamlit`, `python-dotenv`, `groq`

---

## Key Observations
* **Speed:** The `llama-3.1-8b-instant` model on Groq is really fast. The study notes generate almost instantly without long waiting times.
* **Prompting:** Prompt structure mattered a lot. Without clear instructions on output formatting, the AI response was plain text. Telling it to use Markdown gave consistent headers, bold terms, and bullet points.

---

## Challenges Faced
1. **API Key Management:** Learning how to hide the `.env` file locally with `.gitignore` so the Groq key wasn't publicly exposed on GitHub, and setting up Streamlit Secrets for cloud deployment.
2. **Missing Dependencies:** The app threw a `ModuleNotFoundError` on Streamlit Cloud initially because `python-dotenv` wasn't added to `requirements.txt`. Adding it fixed the deployment.
3. **File Directory Setup:** Resolving minor tracking issues in Git caused by files sitting in different parent/child folders.

---

## Future Improvements
* Allow users to upload PDFs or lecture slides so notes are generated directly from custom class material.
* Add a button to download the generated notes as a PDF or Markdown file.
* Add a flashcard generator feature for self-testing.

---



