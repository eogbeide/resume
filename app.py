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
NAME = "Emmanuel Ogbeide"
DESCRIPTION = """
Senior Technical Product Manager, assisting enterprises by developing, deploying and shipping products.
"""
EMAIL = "eogbeide@asu.edu"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com"}

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

with col2:
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
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Mid-level professional
- ✔️ Strong hands on experience and knowledge in data engineering, business analytics and data story-telling
- ✔️ Excellent background in supply chain, procurement and financial planning and analytics
- ✔️ Excellent results-oriented team-player
- ✔️ Product and program leadership
"""
)

# --- EDUCATIONAL BACKGROUND ---
st.write('\n')
st.subheader("Qulifications")
st.write(
    """
- ✔️ Accelerated Executive Management, Yale School of Management, CT., United States.
- ✔️ MBA, Arizona State University, Tempe, AZ, United States.
- ✔️ M.Sc., Process Engineering, University of Nottingham, Nottingham, England, United Kingdom.
- ✔️ B.Sc(Hons), Applied Sciences (Dean's List, 2nd Best Graduating Student)
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, Alteryx
- 📊 Data Visulization: Tableau, PowerBi, MS Excel, Plotly
- 📚 Modeling: Machine Learning (Logistic regression, linear regression, decition trees etcetera)
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Technical Product Manager | Amazon**")
st.write("11/2022 - Present")
st.write(
    """
- ► Lead AI hands-off-the-wheel planning product strategy and delivery across Amazon worldwide businesses
- ► Lead the team's three-year product strategy and annual planning and product roadmap for Amazon Finance Science team
- ► Lead Amazon Forecasting Lab initiative for worldwide Finance organization
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Manager, Finance and Supply Chain/Procurement Planning & Analytics | Amazon Web Services**")
st.write("06/2019 - 11/2022")
st.write(
    """
- ► Owned and managed AWS supply chain, finance and procurement end-to-end planning, including data pipeline, and analytics product strategy and delivery.
- ► Led and oversaw quarterly business planning and review meetings with senior leaders across supply chain and finance organizations.
- ► Defined, tracked and reported on AWS annual, quarterly and monthly supply chain and finance metrics
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Engineer | BHP Billiton Canada**")
st.write("05/2012 - 03/2015")
st.write(
    """
- ► Led the delivery of three green field exploration and delivery projects for BHP Billiton Jansen multi-billion dollars project.
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
