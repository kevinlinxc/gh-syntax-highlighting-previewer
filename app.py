"""GUI that implements the pseudocode for this repo"""
import streamlit as st
import yaml
import os

with open('languages.yml', 'r') as f:
    languages = yaml.safe_load(f)
    schemes = languages.keys()
    if not schemes:
        st.error("Error loading languages.yml")
    scheme_count = len(schemes)


st.header("gh-syntax-highlighting-previewer")
with st.form("Entry form"):
    input_text = st.text_area("Enter text to generate syntax highlighting sampler")
    generate = st.form_submit_button("Generate")
    placeholder = st.empty()
    if generate:
        # store the potentially long string in a temporary file instead of memory
        with open('buffer.txt', 'w') as f:
            for index, scheme in enumerate(schemes):
                placeholder.write("Progress: {:.1f}%".format((100/(scheme_count-1)*index)))
                print(scheme, file=f)
                print(f"```{scheme}", file=f)
                print(input_text, file=f)
                print("```", file=f)
        # display the contents of the file in a streamlit text area
        with open('buffer.txt', 'r') as f:
            st.text_area("Output (select all and copy)", f.read())
