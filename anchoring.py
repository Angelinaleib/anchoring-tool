import streamlit as st

st.title("Anchoring-Effekt")

st.markdown(
    """
    <style>
    [data-testid="stSlider"] .rc-slider-track {
        background-color: #93c5fd !important;
    }
    [data-testid="stSlider"] .rc-slider-handle {
        border-color: #93c5fd !important;
    }
    [data-testid="stSlider"] .rc-slider-handle:focus,
    [data-testid="stSlider"] .rc-slider-handle:hover {
        box-shadow: 0 0 0 0.3rem rgba(59, 130, 246, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "step" not in st.session_state:
    st.session_state.step = 1
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

questions = [
    {
        "page1": "Do you think people rely on AI chatbots for decision-making **more or less than 40%** of the time?",
        "page2": "How much do you think people rely on AI chatbots for decision-making?",
        "answer": 35,
    },
    {
        "page1": (
            "Do you think people can focus on a new piece of information without distraction **more or less than 50%** of the time?"
        ),
        "page2": (
            "What percentage of the time do you think people can **focus** on a new piece of information without getting distracted?"
        ),
        "answer": 30,
    },
    {
        "page1": (
            "When people estimate unfamiliar quantities, do they usually deviate by "
            "**less or more than 40 %** from the true value?"
        ),
        "page2": "How much do you think people's estimates of unfamiliar quantities deviate?",
        "answer": 30,
    },
]

question = questions[st.session_state.question_index]
col_left, col_right = st.columns([5, 1])
with col_right:
    if st.button("Next"):
        st.session_state.question_index = (st.session_state.question_index + 1) % len(
            questions
        )
        st.session_state.step = 1
        st.session_state.pop(
            f"antwort_{st.session_state.question_index}",
            None,
        )
        st.rerun()

if st.session_state.step == 1:
    st.subheader("Question")
    st.write(question["page1"])
    if st.button("Continue"):
        st.session_state.step = 2
        st.rerun()
else:
    st.subheader("Answer")
    st.write(question["page2"])
    antwort = st.slider(
        "Answer in Percent",
        min_value=0,
        max_value=100,
        step=10,
        key=f"antwort_{st.session_state.question_index}",
    )

    if st.button("Check Answer"):
        st.subheader("Result")
        st.write(f"Your answer: **{antwort}%**")
        st.write(f"Correct answer: **{question['answer']}%**")
