import streamlit as st
import subprocess
import random

st.title("Insightful: Explainable Mental Health Chatbot")
st.write("Ask your question or share how you're feeling:")

user_input = st.text_input("You:", "")

negative_keywords = [
    "feeling down", "sad", "depressed", "unhappy", "hopeless",
    "tired", "overwhelmed", "scared", "afraid", "panic",
    "alone", "worthless", "numb", "frustrated", "angry", "anxiety", "stress",
    "i can't do this anymore", "down", "exhausted", "broken", "lost", "self-doubt", "burnout"
]

positive_keywords = [
    "happy", "joyful", "excited", "content", "grateful",
    "hopeful", "relieved", "optimistic", "motivated", "peaceful",
    "great", "awesome", "amazing", "thankful", "proud", "blessed", "energized"
]

def run_ollama(prompt):
    command = ['ollama', 'run', 'tinyllama']
    result = subprocess.run(command, input=prompt, capture_output=True, text=True)
    if result.returncode != 0:
        return "Error: " + result.stderr
    return result.stdout.strip()

if user_input:
    lower_input = user_input.lower()

    base_prompt = (
        "You are a warm, empathetic peer support coach, trained to provide concise, practical, and psychologically sound mental health support. "
        "Do NOT repeat or echo the user's input. Instead, respond directly and naturally with: \n"
        "- Validation and emotional understanding\n"
        "- Clear, simple, evidence-based advice (e.g., CBT, mindfulness)\n"
        "- Motivational encouragement\n"
        "- Transparent explanation of suggestions\n"
        "- A friendly, conversational tone\n"
        "- A supportive closing question or encouragement to continue sharing\n"
        "- A gentle reminder that you are not a therapist and professional help is encouraged when needed.\n\n"
    )

    if any(phrase in lower_input for phrase in negative_keywords):
        tone_instruction = (
            "The user is struggling or feeling down. Respond with genuine warmth and compassion. "
            "Offer tailored psychological tools like thought-challenging, mindfulness, or breathing exercises, and explain why they help. "
            "Encourage their strength and willingness to share. Invite them to explore techniques or share more feelings.\n\n"
        )
    elif any(phrase in lower_input for phrase in positive_keywords):
        tone_instruction = (
            "The user is expressing positive feelings. Respond with enthusiasm and affirmations that celebrate their progress. "
            "Encourage continuation of positive habits and offer ongoing support.\n\n"
        )
    else:
        tone_instruction = (
            "The user's emotional tone is neutral or unclear. Respond with warmth and curiosity to encourage them to share more about how they're feeling.\n\n"
        )

    ethical_note = (
        "Always include a reminder that you are not a professional therapist, and encourage seeking professional help if needed.\n\n"
    )

    instruction_to_respond = (
        "Now respond directly to the user's input in a concise, empathetic, practical, and supportive way following the above guidelines.\n\n"
    )

    final_prompt = (
        base_prompt
        + tone_instruction
        + instruction_to_respond
        + f"User input: {user_input}\n"
        + ethical_note
    )

    response = run_ollama(final_prompt)

    st.markdown(f"**Chatbot:**\n\n> {response}")
