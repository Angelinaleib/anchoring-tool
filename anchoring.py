import streamlit as st

st.title("Anchoring-Effect")

# Inject styling so the slider visually matches Tailwind's blue-300 palette.
st.markdown(
    """
    <style>
    [data-testid="stSlider"] .rc-slider-track,
    [data-testid="stSlider"] .rc-slider-track-1,
    [data-testid="stSlider"] .rc-slider-track-0,
    [data-testid="stSlider"] .rc-slider-track-0::after {
        background-color: #93c5fd !important;
        background-image: none !important;
    }
    [data-testid="stSlider"] .rc-slider-rail,
    [data-testid="stSlider"] .rc-slider-rail-1 {
        background-color: #93c5fd !important;
        background-image: none !important;
    }
    [data-testid="stSlider"] .rc-slider-handle {
        border-color: #fff !important;
        background-color: #93c5fd !important;
        border-width: 2px !important;
        box-shadow: none !important;
    }
    [data-testid="stSlider"] .rc-slider-handle::after,
    [data-testid="stSlider"] .rc-slider-handle::before {
        background-color: #93c5fd !important;
        border-color: #93c5fd !important;
    }
    [data-testid="stSlider"] .rc-slider-handle:focus,
    [data-testid="stSlider"] .rc-slider-handle:hover,
    [data-testid="stSlider"] .rc-slider-handle-dragging {
        box-shadow: 0 0 0 0.3rem rgba(59, 130, 246, 0.5);
    }
    .anchoring-tooltip {
        position: relative;
        cursor: pointer;
        color: #1e293b;
        font-weight: 600;
        display: inline-block;
    }
    .anchoring-tooltip span {
        visibility: hidden;
        width: 240px;
        background-color: #93c5fd;
        color: #fff;
        text-align: center;
        border-radius: 12px;
        padding: 20px;
        position: absolute;
        z-index: 10;
        top: -210px;
        right: 0;
        transform: translate(75px, -28px);
        box-shadow: 0 15px 30px rgba(15, 23, 42, 0.15);
        font-size: 13px;
        font-weight: 400;
        line-height: 1.5;
        font-family: "Geist Mono", "SFMono-Regular", Menlo, Consolas, monospace;
    }
    .anchoring-tooltip:hover span {
        visibility: visible;
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
        st.write(
            "Did you notice? The first number you encountered may have shaped your "
            "estimate more than you expected."
        )
        st.markdown(
            "<span class='anchoring-tooltip'>This is called the <u>anchoring-effect</u>! "
            "<span>"
            "The anchoring effect (or anchoring bias) is a cognitive "
            "bias where individuals rely too heavily on the first piece of "
            "information received (the “anchor”) when making decisions, judgments, "
            "or estimates."
            "</span>"
            "</span>",
            unsafe_allow_html=True,
        )
