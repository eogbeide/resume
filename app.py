from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "main.css"
resume_file = current_dir / "CV.pdf"
profile_pic = current_dir / "profile-pic.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Manny Ogbeide"
PAGE_ICON = ":wave:"
layout="wide"
initial_sidebar_state="expanded"
NAME = "Manny Ogbeide"
DESCRIPTION = """
- ✔️Snr. Technical Product Manager \n
- ✔️Helping enterprises to tackle complex, ambiguous and cross-functional business problems & delivering 5-10X value through product and process leadership.
"""
EMAIL = "eogbeide@asu.edu"

SOCIAL_MEDIA = {
    "Visit Manny's LinkedIn Page": "https://www.linkedin.com/in/emmanuelogbeide/"}
 
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col1:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write("---")
st.write(
    """
- ✔️ Mid-level professional (consulting, cloud computing, energy and financial services)
- ✔️ Strong hands-on experience in data engineering, analytics and data story-telling
- ✔️ Excellent background in supply chain & financial planning and analytics
- ✔️ Excellent results-oriented team-player
- ✔️ Product and program leadership
"""
)

# --- EDUCATIONAL BACKGROUND ---
st.write('\n')
st.subheader("Educational Background")
st.write("---")
st.write(
    """
- ✔️ Accelerated Executive Management, Yale School of Management, CT., United States.
- ✔️ MBA, Arizona State University, Tempe, AZ, United States.
- ✔️ M.Sc., Process Engineering, University of Nottingham, Nottingham, England, U.K.
- ✔️ B.Sc(Hons), Applied Sciences (Dean's List, 2nd Best Graduating Student)
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, Alteryx
- 📊 Data Visualization: Tableau, PowerBI, MS Excel, Plotly
- 📚 Modeling: Machine Learning (Logistic regression, linear regression, decision trees)
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Relevant Experience")
st.write("---")
# --- JOB 1
st.write("🚧", "**Snr. Technical Product Manager | Amazon**")
st.write("Worldwide Science Product Team")
st.write("11/2022 - Present")
st.write(
    """
- ► Lead AI/ML hands-off-the-wheel planning product strategy and delivery across Amazon worldwide businesses
- ► Lead the team's three-year product strategy and annual planning and product roadmap for Amazon Finance Science team
- ► Lead Amazon Forecasting Lab initiative for worldwide Finance organization
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Manager, Finance, Supply Chain and Procurement Planning & Analytics | Amazon Web Services**")
st.write("AWS Infrastructure Supply Chain, Procurement and Finance")
st.write("06/2019 - 11/2022")
st.write(
    """
- ► Owned and managed AWS supply chain, finance and procurement end-to-end planning, including data pipeline, and analytics product strategy and delivery.
- ► Led and oversaw quarterly business planning and review meetings with senior leaders across supply chain and finance organizations.
- ► Defined, tracked and reported on AWS annual, quarterly and monthly supply chain and finance key metrics
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Program Engineer | BHP Billiton Canada**")
st.write("North America Project Strategy and Development")
st.write("05/2012 - 03/2015")
st.write(
    """
- ► Supported the delivery of three green field exploration and delivery projects for BHP Billiton Jansen multi-billion dollars project.
- ► Owned capacity planning for Jansen assumption modeling for emerging markets (India, Brazil and China)
- ► Supported definition studies and operations readiness for new production facilities and delivered the risk and safety management plans and contract management strategy.
"""
)


# --- Projects & Accomplishments ---
#st.write('\n')
#st.subheader("Projects & Accomplishments")
#st.write("---")
#for project, link in PROJECTS.items():
    #st.write(f"[{project}]({link})")
