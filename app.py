import streamlit as st
import random

st.title("Anchoring Effect Demo")

st.write(
    "This short experiment shows how an initial number (an *anchor*) "
    "can influence your estimation."
)

# Question bank: each entry pairs a leading question with a follow-up prompt and slider settings.
QUESTIONS = [
    {
        "page1": "Do you think people typically trust AI recommendations more or less than 60% of the time when they lack strong domain knowledge?",
        "page2": "How much do people typically trust AI recommendations?",
        "min": 0,
        "max": 100,
        "step": 10,
        "example_solution": 65,
        "unit": "%",
    },
    {
        "page1": "Do you think people can focus on a new piece of information for less or more than 15 seconds without distraction?",
        "page2": "How much can people usually focus without getting distracted?",
        "min": 0,
        "max": 100,
        "step": 10,
        "example_solution": 25,
        "unit": "%",
    },
    {
        "page1": "When people estimate unfamiliar quantities, do they usually deviate by less or more than 40% from the true value?",
        "page2": "How much do people usually deviate from the true value?",
        "min": 0,
        "max": 100,
        "step": 10,
        "example_solution": 30,
        "unit": "%",
    },
]


def format_value(value: int, unit: str) -> str:
    if unit == "%":
        return f"{value}%"
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.0f}B"
    if value >= 1_000_000:
        return f"{value / 1_000_000:.0f}M"
    if value >= 1_000:
        return f"{value / 1_000:.0f}K"
    return f"{value} {unit}".strip()


# Initialize session state so navigation, answers, and submissions persist across reruns.
if "step" not in st.session_state:
    st.session_state.step = 1
if "answer" not in st.session_state:
    st.session_state.answer = None
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "question_index" not in st.session_state:
    st.session_state.question_index = None


if st.session_state.step == 1:
    if st.session_state.question_index is None:
        st.session_state.question_index = random.randrange(len(QUESTIONS))
    question = QUESTIONS[st.session_state.question_index]
    st.subheader("First question")
    st.write(question["page1"])
    if st.button("Answer"):
        st.session_state.step = 2
        st.session_state.submitted = False
        st.rerun()

if st.session_state.step == 2:
    if st.session_state.question_index is None:
        st.session_state.question_index = random.randrange(len(QUESTIONS))
    question = QUESTIONS[st.session_state.question_index]
    st.subheader("Second question")
    st.write(question["page2"])

    st.caption(
        f"Scale: {format_value(question['min'], question['unit'])} – {format_value(question['max'], question['unit'])}"
    )
    # Slider lets the participant place their estimate along the configured range.
    answer = st.slider(
        "Select your estimate",
        min_value=question["min"],
        max_value=question["max"],
        step=question["step"],
        value=question["max"] // 2,
        format="%d",
    )

    # Display the min/max bounds beside the slider for orientation.
    col_left, col_right = st.columns(2)
    with col_left:
        st.write(f"Min: {format_value(question['min'], question['unit'])}")
    with col_right:
        st.write(f"Max: {format_value(question['max'], question['unit'])}")

    # Store the chosen value and show feedback once the user submits.
    if st.button("Submit Answer"):
        st.session_state.answer = answer
        st.session_state.submitted = True
        st.rerun()

    if st.session_state.submitted:
        st.write("### Result")
        st.write(
            f"Your answer: **{format_value(st.session_state.answer, question['unit'])}**"
        )
        st.write(
            f"Example solution (for demo): **{format_value(question['example_solution'], question['unit'])}**"
        )
        # Explanation reinforcing why the demo exists.
        st.write(
            "People who see higher anchors tend to give higher estimates, "
            "even when the anchor is random."
        )

    # Reset the experiment to rerun with a new random question.
    if st.button("Start Over"):
        st.session_state.step = 1
        st.session_state.answer = None
        st.session_state.submitted = False
        st.session_state.question_index = None
        st.rerun()
