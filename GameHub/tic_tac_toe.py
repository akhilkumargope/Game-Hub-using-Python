import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    .button {
        width: 80px;
        height: 80px;
        font-size: 30px;
        font-weight: bold;
        color: #fff;
        background-color: #0078d4;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        margin: 5px;
    }
    .button:hover {
        background-color: #005a9e;
    }
    .winner {
        color: #28a745;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Game Logic
def play_game():
    st.title("Tic-Tac-Toe 🏆")
    st.write("Player **X** and **O** take turns. Click a square to make your move.")

    # ✅ Initialize Session State Variables
    if "board" not in st.session_state:
        st.session_state.board = [" "] * 9
    if "current_player" not in st.session_state:
        st.session_state.current_player = "X"
    if "winner" not in st.session_state:
        st.session_state.winner = None

    # Check for Winner
    def check_winner(board):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in winning_combinations:
            if board[a] == board[b] == board[c] and board[a] != " ":
                return board[a]
        return None

    # Reset the Game
    def reset_game():
        st.session_state.board = [" "] * 9
        st.session_state.current_player = "X"
        st.session_state.winner = None

    # Determine Winner
    if st.session_state.winner is None:
        st.session_state.winner = check_winner(st.session_state.board)

    # Display Turn or Winner
    if st.session_state.winner:
        st.markdown(f"<p class='winner'>🎉 Player {st.session_state.winner} wins!</p>", unsafe_allow_html=True)
        st.balloons()
        if st.button("🔄 Play Again"):
            reset_game()
        return
    elif " " not in st.session_state.board:
        st.warning("It's a draw! 😬")
        if st.button("🔄 Play Again"):
            reset_game()
        return
    else:
        st.info(f"Player **{st.session_state.current_player}**'s Turn")

    # Display the Board
    cols = st.columns(3)
    for i in range(9):
        with cols[i % 3]:
            if st.session_state.board[i] == " " and not st.session_state.winner:
                if st.button(" ", key=i, help=f"Player {st.session_state.current_player} click here"):
                    st.session_state.board[i] = st.session_state.current_player
                    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
            else:
                # Display with dynamic color
                color = "#0078d4" if st.session_state.board[i] == "X" else "#ff5733" if st.session_state.board[i] == "O" else "#ccc"
                st.markdown(f"<button class='button' style='background-color: {color};'>{st.session_state.board[i]}</button>", unsafe_allow_html=True)


