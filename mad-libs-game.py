import streamlit as st

# Title
st.title("🎉 Mad Libs Game")

# Instructions
st.write("Fill in the blanks with words of your choice and generate a fun story!")

# Input fields for user
noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")
adjective = st.text_input("Enter an adjective:")
adverb = st.text_input("Enter an adverb:")
place = st.text_input("Enter a place:")
person = st.text_input("Enter a person's name:")

# Button to generate story
if st.button("Generate Story"):
    if all([noun, verb, adjective, adverb, place, person]):
        story = (
            f"One day, {person} went to the {place} with a {adjective} {noun}. "
            f"They decided to {verb} {adverb} through the park. "
            f"Everyone who saw them couldn't believe their eyes!"
        )
        st.success("Here's your Mad Libs story:")
        st.write(story)
    else:
        st.warning("Please fill in all the fields to generate the story.")
