import streamlit as st
import random

def play_game():
    st.title("Memory Card Game 🃏")
    cards = ["🐶", "🐱", "🦄", "🐸", "🐼", "🐶", "🐱", "🦄", "🐸", "🐼"]
    random.shuffle(cards)
    if "flipped_cards" not in st.session_state:
        st.session_state.flipped_cards = ["❓"] * 10
        st.session_state.selected = []
    
    cols = st.columns(5)
    for i in range(10):
        with cols[i % 5]:
            if st.button(st.session_state.flipped_cards[i], key=i):
                if i not in st.session_state.selected:
                    st.session_state.flipped_cards[i] = cards[i]
                    st.session_state.selected.append(i)
                
                if len(st.session_state.selected) == 2:
                    idx1, idx2 = st.session_state.selected
                    if cards[idx1] != cards[idx2]:
                        st.warning("No Match! Try Again.")
                        st.session_state.flipped_cards[idx1] = "❓"
                        st.session_state.flipped_cards[idx2] = "❓"
                    else:
                        st.success("Match Found! 🎉")
                    st.session_state.selected = []
