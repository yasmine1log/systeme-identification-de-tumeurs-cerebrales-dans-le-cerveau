import streamlit as st

def page1_app():
    st.title("Meet the ITC Team 👥")
    st.write("""
    Welcome to the ITC Team page! We are a passionate and dedicated group working together on this project to advance brain tumor 
    research and technology development. Our goal is to leverage technology to make a positive impact on healthcare, improve early 
    detection, and support the medical community in offering timely, effective treatment.
    """)

    # Displaying team member names and roles
    team_members = [
        {"name": "KOUMMANE Saad", "role": "Research & Data Analysis"},
        {"name": "LOGHMARI Yasmine", "role": "Software Engineering"},
        {"name": "Kassimi Abdessamad", "role": "Project Lead & ML Development"},
        {"name": "LABCHIR Anas", "role": "Frontend Development"},
        {"name": "Zinoune Ouissal-Ilham", "role": "Backend Development"}
    ]

    # Displaying each team member with a brief introduction
    for member in team_members:
        st.subheader(f"{member['name']}")
        st.write(f"**Role**: {member['role']}")
        st.write(f"**About**: {member['name']} is committed to driving forward the vision of this project, bringing expertise in {member['role'].lower()} to support our goals.")
        st.write("---")

    # Motivation section
    st.header("Our Motivation 🌟")
    st.write("""
    Brain tumors affect thousands of individuals and families worldwide, and early detection remains a crucial factor in improving 
    patient outcomes. Our team is motivated by a shared desire to harness the power of technology and machine learning to make 
    impactful contributions in the medical field. With this project, we aim to create tools that empower healthcare professionals 
    in diagnosing and understanding brain tumors more effectively, ultimately enhancing the quality of care provided to patients.

    By combining our diverse skills in software development, machine learning, data analysis, and design, we hope to pave the way for 
    innovative healthcare solutions that address real-world challenges. This project represents our commitment to using technology 
    for good, pushing the boundaries of what’s possible in the medical domain, and supporting the future of personalized medicine. 
    We are excited to be part of this journey and look forward to making a meaningful impact. 🌍
    """)
