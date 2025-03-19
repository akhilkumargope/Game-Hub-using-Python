import streamlit as st
import numpy as np

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    block_x, block_y = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[block_x + i][block_y + j] == num:
                return False
    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def play_game():
    st.title("Sudoku Solver 🧩")
    st.write("Enter the Sudoku puzzle (use 0 for empty cells)")

    input_data = []
    for i in range(9):
        row = st.text_input(f"Row {i+1} (9 digits, use spaces or commas)", key=i)
        input_data.append([int(num) for num in row.replace(",", " ").split()])

    if st.button("Solve Puzzle"):
        if solve_sudoku(input_data):
            st.success("Sudoku Solved!")
            st.write(np.array(input_data))
        else:
            st.error("No solution exists.")
