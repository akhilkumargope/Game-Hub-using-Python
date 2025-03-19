import streamlit as st
import random

def play_game():
    st.title("Number Guessing Game 🔢")

    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 100)

    user_guess = st.number_input("Guess a number between 1 and 100", min_value=1, max_value=100, step=1)

    if st.button("Check Guess"):
        if user_guess == st.session_state.number:
            st.success("🎉 Correct! You guessed the number!")
            st.session_state.number = random.randint(1, 100)
        elif user_guess > st.session_state.number:
            st.warning("Too high! Try again.")
        else:
            st.warning("Too low! Try again.")
