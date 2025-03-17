import streamlit as st
import page1  # Import page1.py module
import page2  # Import page2.py module
import page3  # Import page3.py module
import page4  # Import page4.py module

# Function to set login page style
def set_login_style():
    login_style = """
    <style>
    .stApp {
        background-image: url("https://scitechdaily.com/images/3D-Brain-Illustration.gif");
        background-size: cover;
        background-position: center;
        color: white;
        font-family: Arial, sans-serif;
    }
    
    .login-container {
        max-width: 400px;
        padding: 2rem;
        background-color: rgba(0, 0, 0, 0.7);
        border-radius: 10px;
        text-align: center;
    }
    
    .login-container h1 {
        font-size: 32px;
        color: #ffcc00;
    }
    
    .login-container input {
        margin-top: 1rem;
        padding: 0.5rem;
        font-size: 18px;
        border-radius: 5px;
        border: none;
        width: 100%;
    }
    
    .login-button {
        margin-top: 1.5rem;
        padding: 0.7rem;
        font-size: 18px;
        color: white;
        background-color: #4CAF50;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
    }
    
    .login-button:hover {
        background-color: #45a049;
    }
    </style>
    """
    st.markdown(login_style, unsafe_allow_html=True)

# Function to dynamically set CSS based on the selected page
def set_page_style(page_name):
    if page_name == "main":
        image_url = "https://images.mirror-media.xyz/publication-images/2bmnI8kbsAe1RO2kBFXiy.gif"
        background_color = "#808080"
    elif page_name == "page1":
        image_url = "https://www.devteam.space/wp-content/uploads/2022/05/What-makes-a-good-dev-team.jpg"
        background_color = "#8c8c8c"  # Dark purple-blue for ITC Team
    elif page_name == "page2":
        image_url = "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/f68af2102686225.602aace875913.gif"
        background_color = "#999999"  # Slate blue for Technologie
    elif page_name == "page3":
        image_url = "https://assets-v2.lottiefiles.com/a/3f3c800e-1168-11ee-8c3b-131af4d303a5/RVW0iShHMK.gif"
        background_color = "#a6a6a6"  # Dark teal for Contact Us
    elif page_name == "page4":
        image_url = "https://mathieuromain.web-edu.fr/wp-content/uploads/2023/01/Accueil-1.gif"
        background_color = "#b2b2b2"  # Green-teal for Analyse

    page_style = f"""
    <style>
    .stApp {{
        background-color: {background_color};
        color: white;
        font-family: Arial, sans-serif;
    }}

    .block-container {{
        max-width: 75%;
        padding: 2rem;
    }}

    .banner {{
        background-image: url("{image_url}");
        background-position: center;
        background-size: cover;
        height: 300px;
        border-radius: 10px;
        margin-bottom: 2rem;
    }}

    .section {{
        background-color: #333333;
        padding: 1.5rem;
        margin-bottom: 2rem;
        border-radius: 10px;
    }}

    .section h2 {{
        font-size: 24px;
        margin-bottom: 0.5rem;
    }}

    .section p {{
        font-size: 16px;
        line-height: 1.6;
        margin-bottom: 1rem;
    }}

    .sidebar-button {{
        display: block;
        width: 100%;
        padding: 10px;
        font-size: 18px;
        color: white !important;
        background-color: #172e0b;
        border: 1px solid #888;
        text-align: center;
        cursor: pointer;
        border-radius: 5px;
        transition: background-color 0.3s ease, color 0.3s ease;
        margin-bottom: 10px;
        text-decoration: none;
    }}

    .sidebar-button:hover {{
        background-color: #606060;
    }}

    .sidebar-button:active {{
        background-color: #808080;
        color: #f0f0f0 !important;
    }}
    </style>
    """
    st.markdown(page_style, unsafe_allow_html=True)
    st.markdown('<div class="banner"></div>', unsafe_allow_html=True)

# Check login status
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Display login page
if not st.session_state["logged_in"]:
    set_login_style()
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.title("Good Doctor Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login", key="login-button"):
        if username == "admin" and password == "123456789":
            st.session_state["logged_in"] = True
            st.success("Login successful! Redirecting...")
        else:
            st.error("Incorrect username or password")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    # Set page in session state if not set
    if "page" not in st.session_state:
        st.session_state["page"] = "main"

    # Sidebar navigation
    with st.sidebar:
        st.title("Dashboard")
        st.write("Navigate to different sections:")

        if st.button("🏠 Home"):
            st.session_state["page"] = "main"
        if st.button("👥 ITC Team"):
            st.session_state["page"] = "page1"
        if st.button("💻 Technologie"):
            st.session_state["page"] = "page2"
        if st.button("📞 Contact Us"):
            st.session_state["page"] = "page3"
        if st.button("📊 Analyse"):
            st.session_state["page"] = "page4"

    # Apply style based on selected page
    set_page_style(st.session_state["page"])

    # Display content based on the selected page
    if st.session_state["page"] == "page1":
        page1.page1_app()  # Call the function in page1.py
    elif st.session_state["page"] == "page2":
        page2.page2_app()  # Call the function in page2.py
    elif st.session_state["page"] == "page3":
        page3.page3_app()  # Call the function in page3.py
    elif st.session_state["page"] == "page4":
        page4.page4_app()  # Call the function in page4.py
    else:
        # Main content area for the Home page
        st.title("Good Doctor - Brain Tumor Insights")
        st.subheader("Understanding Brain Tumors and Advancements in Detection")

        st.write("""
        Brain tumors are a complex and often life-altering condition, affecting thousands of lives globally. At Good Doctor, 
        we're dedicated to using advanced technology to support early diagnosis, effective treatment, and personalized care. Our AI-driven 
        platform provides medical professionals with powerful tools to detect, analyze, and understand brain tumors, aiding them in making 
        timely and informed decisions for better patient outcomes.
        """)

        # Content sections with descriptions
        content = [
    {
        "title": "🧠 What is a Brain Tumor?",
        "description": """A brain tumor is an abnormal mass of cells within or surrounding the brain. Tumors can be either benign (non-cancerous) 
                          or malignant (cancerous), and both types can pose significant risks depending on their size, growth rate, and location. 
                          Brain tumors disrupt normal brain functions by compressing, invading, or displacing healthy brain tissue, leading 
                          to symptoms such as persistent headaches 🤕, seizures, nausea 🤢, difficulty with speech 🗣️ or vision 👀, and even 
                          behavioral changes.
                          Diagnostic techniques have advanced significantly, with MRI, CT scans, and PET scans 🖥️ providing clear images of brain 
                          structures. In addition, biopsies help doctors examine tumor cells under a microscope 🔬, enabling precise diagnosis. 
                          Scientists are also exploring blood-based biomarkers to detect brain tumors early and non-invasively, a promising 
                          development that could revolutionize brain tumor screening. The journey of diagnosis is complex but crucial, as 
                          early detection can improve treatment options and outcomes. 💪"""
    },
    {
        "title": "⚠️ The Dangers of Brain Tumors",
        "description": """Brain tumors can be life-altering, as they may impair critical functions and lower the quality of life. Symptoms vary 
                          based on the tumor's size, location, and growth speed. For instance, a tumor in the frontal lobe can affect personality 
                          and decision-making 🤔, while a tumor in the occipital lobe can lead to visual disturbances 👁️. As tumors grow, they 
                          may increase intracranial pressure, leading to severe headaches, vomiting 🤮, and even coma in extreme cases. The 
                          location of the tumor makes surgical removal challenging and sometimes risky.
                          Treatment plans are often complex, involving a combination of surgery 🔪, radiation therapy 🌐, and chemotherapy 💊. 
                          Each case requires a personalized approach, as treatment goals vary: some aim to remove the tumor entirely, while others 
                          focus on slowing its growth or alleviating symptoms. 🌎 Globally, the healthcare community is working to improve 
                          surgical techniques, develop targeted radiation therapies, and introduce less invasive treatments that minimize 
                          damage to surrounding healthy tissue. ❤️‍🩹"""
    },
    {
        "title": "💼 Dedication of Medical Professionals",
        "description": """Healthcare professionals, including neurosurgeons 🧑‍⚕️, oncologists, radiologists 🧑‍🔬, and nurses 🧑‍⚕️, dedicate their 
                          expertise to the fight against brain tumors. Neurosurgeons perform delicate operations on brain tissue to remove or 
                          reduce tumors, often with robotic surgery tools 🤖 that enhance precision. Radiation oncologists use advanced imaging 
                          and planning software 🖥️ to target cancer cells with minimal damage to healthy brain tissue. Medical oncologists work 
                          on the best drug combinations to prevent recurrence and improve survival rates.
                          Modern healthcare relies on AI-driven diagnostic tools 📈 that analyze MRI and CT scans, identifying tumors early and 
                          predicting their behavior. Innovations in intraoperative imaging allow surgeons to view high-resolution images during 
                          procedures, enhancing the chances of complete removal. These professionals also provide psychological support 💙, 
                          guiding patients and families through the emotional challenges associated with brain tumor treatments. They are 
                          truly healthcare heroes! 🦸‍♂️🦸‍♀️"""
    },
    {
        "title": "🌍 Global Statistics on Brain Tumors",
        "description": """Brain tumors affect hundreds of thousands of individuals annually, with a growing incidence rate partly due to 
                          aging populations and better diagnostic imaging 📊. Primary malignant brain tumors are more common in older adults, 
                          but pediatric brain tumors 🎗️ also represent a significant portion of childhood cancers. The survival rate varies by 
                          tumor type; for instance, glioblastoma has a lower survival rate compared to other tumors due to its aggressive nature.
                          The healthcare burden of brain tumors is substantial, with patients requiring extensive treatments and long-term care, 
                          often leading to high costs 💵. International organizations 🌐 and research institutions are joining forces to 
                          improve brain tumor research, accessibility to treatments, and support for affected families. Raising awareness 
                          and funding research for new therapies are critical to making strides in global healthcare. 📈"""
    },
    {
        "title": "🔬 Innovations in Brain Tumor Research",
        "description": """Brain tumor research is advancing rapidly, with scientists exploring new and personalized therapies 🧬 that aim 
                          to minimize side effects and maximize effectiveness. Immunotherapy, which harnesses the body’s immune system 🛡️ to 
                          target cancer cells, shows promise in trials with checkpoint inhibitors and CAR T-cell therapy. Precision medicine 
                          is another breakthrough, allowing doctors to customize treatments based on genetic markers unique to each patient’s 
                          tumor 🧬.
                          AI and machine learning 🤖 are also revolutionizing diagnosis and treatment planning. Predictive algorithms analyze 
                          patient data 📊 to forecast tumor progression, aiding oncologists in making informed decisions. Surgical innovations, 
                          like awake brain surgery, allow patients to stay conscious during tumor removal, protecting essential brain functions. 
                          🚀 The rapid development of minimally invasive procedures and targeted therapies is bringing hope to patients and 
                          doctors alike! 💡"""
    },
    {
        "title": "💪 Living with and Beyond Brain Tumors",
        "description": """Living with a brain tumor requires immense courage and resilience 💪. Patients and their families often face 
                          psychological challenges, including anxiety, depression 😔, and cognitive changes 🧩 that affect daily life. However, 
                          a range of supportive care options—like rehabilitation therapy, counseling, and support groups—helps patients 
                          regain a sense of normalcy and well-being.
                          Life after treatment involves ongoing health needs, from managing side effects to regular screenings for recurrence. 
                          Rehabilitation services, including physical 🏃, occupational 🛠️, and speech therapy 🗣️, play a vital role in recovery, 
                          enabling individuals to restore lost abilities and adapt to new ways of life. Support from loved ones ❤️, healthcare 
                          providers, and advocacy groups makes a profound difference, reminding patients that they are not alone. With 
                          resilience, community support, and advancing medical care, many patients find strength and hope to lead fulfilling lives 
                          despite the challenges they face. """
    }
]

        # Display each section as structured text
        for item in content:
            st.markdown(f"""
                <div class="section">
                    <h2>{item['title']}</h2>
                    <p>{item['description']}</p>
                </div>
            """, unsafe_allow_html=True)

    # Footer
    st.write("© 2024 Good Doctor | Designed by Abdessamad Kassimi")
