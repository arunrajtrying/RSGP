import streamlit as st
import random

# Title
st.title("🗣️ Random Sentence Generator")

# Word lists
subjects = ["The cat", "A robot", "My friend", "The teacher", "An alien"]
verbs = ["eats", "builds", "chases", "teaches", "explores"]
objects = ["a sandwich", "the galaxy", "a lesson", "a mouse", "a spaceship"]
adverbs = ["quickly", "silently", "gracefully", "loudly", "carefully"]

# Sentence generation function
def generate_sentence():
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    adverb = random.choice(adverbs)
    return f"{subject} {verb} {obj} {adverb}."

# Button to generate sentence
if st.button("Generate Sentence"):
    sentence = generate_sentence()
    st.success(f"✨ {sentence}")
else:
    st.info("Click the button to generate a random sentence.")
