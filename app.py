import streamlit as st


# ---------------- UI SETUP ----------------
st.set_page_config(page_title="Job AutoBot",  layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            font-size: 18px;
            padding: 10px 24px;
            border-radius: 12px;
        }
        .stButton>button:hover {
            background-color: #d73838;
        }
        .title-text {
            text-align: center;
            color: #1F4E79;
            font-size: 40px;
            font-weight: bold;
        }
        .sub-text {
            text-align: center;
            font-size: 20px;
            color: #6c757d;
        }
        .box-style {
            background-color: #f1f3f6;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER SECTION ----------------
st.markdown("<p class='title-text'> AUTOMATED JOB APPLICATION BOT </p>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Apply for jobs smartly and quickly with one click!</p>", unsafe_allow_html=True)
st.markdown("")

# ---------------- MAIN FORM ----------------
with st.container():
    with st.container():
        st.markdown("<div class='box-style'>", unsafe_allow_html=True)

        # Job role selection
        st.markdown("### 🧠 Select Your Preferred Job Role")
        job_options = ["Power BI Developer", "Data Analyst", "Business Analyst"]
        selected_role = st.selectbox("🔽 Choose a role", job_options)

        # Custom keyword
        custom_keyword = st.text_input("🔍 Add Custom Keyword (Optional)", placeholder="e.g. remote, python")

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- ACTION BUTTON ----------------
st.markdown("---")
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

if st.button("One Hit to start  automatic ", use_container_width=True):
    st.success("⏳ Running your job bot now...")
    from login import login
    login()
    st.success("✅ Login and automation script executed.")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    """
    <p style='text-align: center; font-size:14px; color:gray;'>
        Built by <a href='https://www.linkedin.com/in/chandrashekarippili/' target='_blank' style='color:#1f77b4; text-decoration:none; font-weight:bold;'>
        Chandra Shekar Ippili</a>
    </p>
    """,
    unsafe_allow_html=True
)
