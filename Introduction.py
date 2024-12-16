import streamlit as st
from pages import Home
from pages import SUMMARYSKILLS
from pages import EDUCATION
from pages import EXPERIENCE
from pages import Contact

options = ["Home","SUMMARY & SKILLS", "EDUCATION","EXPERIENCE","CONTACT"]


left_column, right_column = st.columns([1.2, 2.8])

# Add content to the left column
with left_column:
    page = st.radio("Select a page", options)

# Add content to the right column
with right_column:
    if page == "Home":
        Home.main()
    elif page == "SUMMARY & SKILLS":
        SUMMARYSKILLS.main()
    elif page == "EDUCATION":
        EDUCATION.main()
    elif page == "EXPERIENCE":
        EXPERIENCE.main()
    elif page == "CONTACT":
        Contact.main()   

