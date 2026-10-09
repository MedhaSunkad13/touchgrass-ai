import streamlit as st
import ollama
import json
import re


# ============================================================
# Available outdoor activities
# ============================================================

activities = [
    "Walking",
    "Hiking",
    "Cycling",
    "Running",
    "Gardening",
    "Fishing",
    "Bird Watching",
    "Sketching"
]


# ============================================================
# Check whether text contains unexpected languages
# ============================================================

def contains_non_english(text):

    pattern = r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af\u0600-\u06ff\u0900-\u097f]"

    return bool(re.search(pattern, text))


# ============================================================
# Generate personalized activity using Ollama
# ============================================================

def generate_activity(activity, mood):

    prompt = f"""
Create one personalized outdoor plan for the following activity.

Chosen activity:
{activity}

User's mood:
{mood}

Requirements:
- The plan must be specifically about {activity}.
- Create only ONE plan.
- Give exactly 4 or 5 practical steps.
- Each step must be a plain string containing only the instruction.
- Do NOT number the steps.
- Do NOT write "Step 1", "Step 2", etc.
- Do NOT return objects or dictionaries inside the steps.
- Write the entire response in English only.
- Do NOT use Chinese, Japanese, Korean, Arabic, Hindi,
  or any other language.
- Do not suggest phones, cameras, photography, apps,
  social media, videos, or other digital devices.
- Do not tell the person to close their eyes while walking,
  running, cycling, hiking, or doing any other activity.
- Do not suggest unsafe actions.
- Keep the activity realistic and simple.
- Adapt the wording and suggestions to the user's mood.

Return ONLY valid JSON in exactly this format:

{{
    "description": "A short friendly description of the plan.",
    "steps": [
        "First practical instruction.",
        "Second practical instruction.",
        "Third practical instruction.",
        "Fourth practical instruction."
    ]
}}
"""

    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json"
    )

    result = json.loads(response.message.content)


    # --------------------------------------------------------
    # Check description and steps for unexpected languages
    # --------------------------------------------------------

    text_to_check = result.get("description", "")

    for step in result.get("steps", []):

        if isinstance(step, dict):
            step = step.get("step", "")

        text_to_check += " " + str(step)


    if contains_non_english(text_to_check):

        raise ValueError(
            "The AI generated text in a language other than English."
        )


    return result


# ============================================================
# Clean AI-generated steps
# ============================================================

def clean_steps(steps):

    cleaned_steps = []

    for step in steps:

        # Handle steps returned as dictionaries
        if isinstance(step, dict):
            if "step" in step:
                step = step["step"]
            else:
                step = str(step)

        # Convert to text and remove surrounding whitespace
        step = str(step).strip()

        # Remove unwanted quotation marks at the beginning and end
        step = step.strip("\"'“”‘’")

        # Remove trailing whitespace and stray punctuation
        step = step.rstrip().rstrip("\"'“”‘’").rstrip()

        if step:
            cleaned_steps.append(step)

    return cleaned_steps


# ============================================================
# Display generated activity
# ============================================================

def display_activity(
    activity,
    description,
    duration,
    steps
):

    st.markdown(
        "### 🌱 Your personalized outdoor plan"
    )

    with st.container(border=True):

        st.success(
            "Your outdoor activity is ready! 🌱"
        )

        st.markdown(
            f"## {activity}"
        )

        st.write(description)

        st.markdown(
            f"⏱️ **Duration:** {duration}"
        )

        st.markdown(
            "### 🌿 Steps"
        )

        for index, step in enumerate(
            steps,
            start=1
        ):

            st.write(
                f"**{index}.** {step}"
            )

        st.markdown(
            "### 📵 Screen-Free Rule"
        )

        st.info(
            "Keep your phone and other digital devices "
            "away during the activity."
        )

# ============================================================
# Streamlit page configuration
# ============================================================

st.set_page_config(
    page_title="TouchGrass AI",
    page_icon="🌱",
    layout="wide"
)


# ============================================================
# Custom page styling
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f5f7f2;
    }

    .hero {
        text-align: center;
        padding: 30px 20px 25px 20px;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 10px;
    }

    .tagline {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 8px;
    }

    .subtitle {
        font-size: 1.05rem;
    }

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        padding: 14px;
        font-size: 1.05rem;
        font-weight: 600;
        background-color: #2f6b30;
        color: black;
        border: none;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# Hero section
# ============================================================

st.markdown(
    """
<div class="hero">
<h1>🌱 TouchGrass AI</h1>
<p class="tagline">Spend less time on screens and more time outside.</p>
<p class="subtitle">Tell us how you want to spend your time outdoors.</p>
</div>
""",
    unsafe_allow_html=True
)

# ============================================================
# User inputs
# ============================================================

st.markdown(
    "### 🌿 Plan your time outdoors"
)


with st.container(border=True):

    col1, col2 = st.columns(2)


    with col1:

        available_time = st.text_input(
            "⏱️ How much time do you have?",
            placeholder="Example: 30 minutes"
        )


    with col2:

        mood = st.text_input(
            "😊 How are you feeling?",
            placeholder="Example: relaxed"
        )


    activity = st.selectbox(
        "🌿 What would you like to do outdoors?",
        activities
    )


# ============================================================
# Generate button
# ============================================================

if st.button(
    "🌱 Generate My Activity",
    use_container_width=True
):

    # --------------------------------------------------------
    # Validate time
    # --------------------------------------------------------

    if not available_time.strip():

        st.error(
            "Please enter how much time you have."
        )


    # --------------------------------------------------------
    # Validate mood
    # --------------------------------------------------------

    elif not mood.strip():

        st.error(
            "Please tell us how you are feeling."
        )


    else:

        # ----------------------------------------------------
        # Generate activity using local AI
        # ----------------------------------------------------

        with st.spinner(
            "🌱 Creating your outdoor plan..."
        ):

            try:

                result = generate_activity(
                    activity,
                    mood
                )


            except json.JSONDecodeError:

                st.error(
                    "The AI returned an invalid response. "
                    "Please try again."
                )

                st.stop()


            except ValueError as e:

                st.error(
                    str(e)
                )

                st.warning(
                    "Please click the Generate button again."
                )

                st.stop()


            except ollama.ResponseError:

                st.error(
                    "The local AI model could not generate "
                    "the activity. Please try again."
                )

                st.stop()


            except Exception as e:

                st.error(
                    "Something went wrong while generating "
                    "your activity."
                )

                st.write(
                    f"Error: {e}"
                )

                st.stop()


        # ----------------------------------------------------
        # Validate AI fields
        # ----------------------------------------------------

        if "description" not in result:

            st.error(
                "The AI did not return a description. "
                "Please try again."
            )

            st.stop()


        if "steps" not in result:

            st.error(
                "The AI did not return any steps. "
                "Please try again."
            )

            st.stop()


        # ----------------------------------------------------
        # Clean AI-generated steps
        # ----------------------------------------------------

        steps = clean_steps(
            result["steps"]
        )


        # ----------------------------------------------------
        # Check number of steps
        # ----------------------------------------------------

        if len(steps) < 4 or len(steps) > 5:

            st.error(
                "The AI generated an invalid number of steps. "
                "Please try again."
            )

            st.stop()


        # ----------------------------------------------------
        # Display final activity
        # ----------------------------------------------------

        display_activity(
            activity,
            result["description"],
            available_time,
            steps
        )
