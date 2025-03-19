import streamlit as st
import tic_tac_toe
import rps
import number_guess
import quiz
import word_search
import memory_card
import sudoku_solver

# Sidebar Navigation
st.sidebar.title("🎮 Game Hub")
game_choice = st.sidebar.radio("Select a game:", [
    "Home", 
    "Tic-Tac-Toe", 
    "Rock Paper Scissors", 
    "Number Guessing", 
    "Trivia Quiz", 
    "Word Search", 
    "Memory Card Game", 
    "Sudoku Solver"
])

# Home Page
if game_choice == "Home":
    st.title("🎲 Welcome to Game Hub! 🎲")
    st.write("Choose a game from the sidebar and start playing!")

# Load Selected Game
elif game_choice == "Tic-Tac-Toe":
    tic_tac_toe.play_game()

elif game_choice == "Rock Paper Scissors":
    rps.play_game()

elif game_choice == "Number Guessing":
    number_guess.play_game()

elif game_choice == "Trivia Quiz":
    quiz.play_game()

elif game_choice == "Word Search":
    word_search.play_game()

elif game_choice == "Memory Card Game":
    memory_card.play_game()

elif game_choice == "Sudoku Solver":
    sudoku_solver.play_game()
