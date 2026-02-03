import streamlit as st
import json
import pandas as pd
from datetime import datetime
import os

# ---------- Page Config ----------
st.set_page_config(
    page_title="Just For You ❤️",
    page_icon="💍",
    layout="centered"
)
st.markdown("""
<style>
/* Hide Streamlit header layer that blocks clicks */
[data-testid="stHeader"] {
    display: none;
}
 
/* Ensure app container allows clicks */
[data-testid="stAppViewContainer"] {
    pointer-events: auto;
}
 
/* Position download button */
[data-testid="stDownloadButton"] {
    position: fixed;
    top: 16px;
    right: 16px;
    z-index: 99999;
    pointer-events: auto;
}
 
/* Style the button */
[data-testid="stDownloadButton"] button {
    background-color: #c9184a !important;
    color: white !important;
    font-size: 11px !important;
    padding: 6px 10px !important;
    border-radius: 999px !important;
    border: none !important;
    cursor: pointer !important;
    pointer-events: auto !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}
 
/* Remove white container */
[data-testid="stDownloadButton"] > div {
    background: transparent !important;
    padding: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- Custom Pink Theme CSS ----------
st.markdown("""
<style>
/* Main app background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        135deg,
        #f7c5cc,
        #f2a1b3,
        #e6b2c6,
        #f5d0d8
    );
}

/* Remove white blocks */
[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stToolbar"] {
    right: 2rem;
}

/* Content container */
.block-container {
    padding-top: 2rem;
}

/* Text styling */
h1 {
    text-align: center;
    color: #7a1f3d;
}

h3 {
    text-align: center;
    color: #8f2d56;
}

.question {
    font-size: 20px;
    font-weight: 500;
    color: #5a0f2e;
    margin-top: 30px;
}

/* Button styling */
.stButton > button {
    background-color: #c9184a;
    color: white;
    border-radius: 16px;
    padding: 10px 24px;
    font-size: 16px;
    border: none;
}

.stRadio > div {
    padding: 6px;
}
            
</style>
""", unsafe_allow_html=True)



# ---------- App State ----------
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# ---------- Title ----------
if not st.session_state.submitted:
    st.markdown("<h1>💖 A Little Quiz for You 💖</h1>", unsafe_allow_html=True)
    st.markdown("<h2>My Laqt-e-Jigar Husband Rayees Ahmed</h2>", unsafe_allow_html=True)
    st.markdown("<h3>Just answer honestly 😊</h3>", unsafe_allow_html=True)

# ---------- Questions ----------
if not st.session_state.submitted:

    q1 = st.radio(
        "📍 Where did we first meet?",
        ["At work", "Through friends", "At Mall", "Destiny planned it ✨"]
    )

    q2 = st.radio(
        "💬 What did you notice about me first?",
        ["My smile 😊", "My confidence 😌", "My kindness ❤️", "Everything ✨"]
    )

    q3 = st.radio(
        "💭 What do you like most about me?",
        ["My support", "My care", "My craziness 😜", "All of it 💕"]
    )

    q4 = st.radio(
        "🌙 How do you see us?",
        ["Best friends", "Soulmates", "Life partners", "Forever 💍"]
    )

    q5 = st.radio(
        "❤️ Pick the line that feels right:",
        [
            "You are my happiness",
            "You are my forever",
            "You are everything",
            "All of the above"
        ]
    )

    if st.button("Submit 💌"):
        # ---------- Save Answers ----------
        response = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Where did we first meet?": q1,
            "What did you notice first?": q2,
            "What do you like most?": q3,
            "How do you see us?": q4,
            "Chosen line": q5
        }

        # Save to JSON
        json_file = "responses.json"
        if os.path.exists(json_file):
            with open(json_file, "r") as f:
                data = json.load(f)
        else:
            data = []

        data.append(response)

        with open(json_file, "w") as f:
            json.dump(data, f, indent=4)

        # Save to Excel
        excel_file = "responses.xlsx"
        df_new = pd.DataFrame([response])

        if os.path.exists(excel_file):
            df_existing = pd.read_excel(excel_file)
            df_final = pd.concat([df_existing, df_new], ignore_index=True)
        else:
            df_final = df_new

        df_final.to_excel(excel_file, index=False)

        st.session_state.submitted = True
        st.rerun()

# ---------- Final Screen ----------
else:
    st.download_button(
        label="⬇",
        data=open("responses.xlsx", "rb"),
        file_name="responses.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
 
    st.markdown("<h2>💞 Thank You for Answering Honey 💞</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='footer'>
        No matter what you chose…<br><br>
        <b>You are my forever.</b><br><br>
        I choose you — today, tomorrow, always. 💍❤️
    </div>
    """, unsafe_allow_html=True)
 
    st.balloons()