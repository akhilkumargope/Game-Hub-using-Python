import streamlit as st
import random

def play_game():
    st.title("Trivia Quiz 🧠")

    questions = {
        "What is the capital of France?": "Paris",
        "Who developed Python?": "Guido van Rossum",
        "Which planet is known as the Red Planet?": "Mars"
    }

    question, answer = random.choice(list(questions.items()))

    user_answer = st.text_input(f"❓ {question}")

    if st.button("Submit Answer"):
        if user_answer.strip().lower() == answer.lower():
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Wrong! The correct answer is {answer}.")
