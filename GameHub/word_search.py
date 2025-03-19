import streamlit as st
import numpy as np
import random

def generate_word_search(words, size=10):
    grid = np.full((size, size), " ")

    def place_word(word):
        word_len = len(word)
        direction = random.choice(["horizontal", "vertical", "diagonal"])
        if direction == "horizontal":
            x, y = random.randint(0, size - 1), random.randint(0, size - word_len)
        elif direction == "vertical":
            x, y = random.randint(0, size - word_len), random.randint(0, size - 1)
        else:
            x, y = random.randint(0, size - word_len), random.randint(0, size - word_len)
        
        for i in range(word_len):
            if direction == "horizontal":
                grid[x, y + i] = word[i]
            elif direction == "vertical":
                grid[x + i, y] = word[i]
            else:
                grid[x + i, y + i] = word[i]
    
    for word in words:
        place_word(word.upper())

    # Fill empty spaces with random letters
    for i in range(size):
        for j in range(size):
            if grid[i, j] == " ":
                grid[i, j] = chr(random.randint(65, 90))
    
    return grid

def play_game():
    st.title("Word Search Puzzle 🧩")
    words = st.text_input("Enter words separated by commas (e.g., cat, dog, tree)").split(',')
    if st.button("Generate Puzzle"):
        grid = generate_word_search([word.strip() for word in words])
        st.write("Find these words:", words)
        st.dataframe(grid)
