import streamlit as st

def page3_app():
    st.title("📞 Contact Us")

    # Displaying the contact number prominently
    st.subheader("Reach Out to Us Anytime!")
    st.markdown("""
    ## **+33 7 48 51 33 57**
    """)

    # Additional message
    st.write("""
    We are here to assist you with any questions, feedback, or support you need regarding our project. 
    Feel free to reach out to us on the provided contact number, and a member of our team will be happy to assist you.

    Alternatively, you can send us an email, and we'll get back to you as soon as possible.
    """)
