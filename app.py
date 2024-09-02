import streamlit as st

# Set the title of the app
st.title("My Autobiography and Portfolio")

# Autobiography Section
st.header("About Me")
st.image("my_photo.jpg", caption="Your Photo", use_column_width=True)
st.write("""
    Hello! My name is Vincent Dalan. I am a dedicated fourth-year Bachelor of Science in Information Technology student at Cebu Institute of Technology-University. 
    I am passionate about programming and enjoy working with languages such as C++, Java, Python, SQL, CSS, JavaScript, Kotlin, and PHP. 
    I am eager to learn and develop my skills through hands-on experiences and contribute to the working environment.
""")

# Portfolio Section
st.header("Portfolio")

# Project 1
st.subheader("Project 1: Streamlit App")
st.write("""
    This project demonstrates the use of Streamlit to create interactive web applications.
    - **Technologies Used:** Streamlit, Python
    - **Description:** A simple Streamlit app showcasing an autobiography and portfolio.
    - **Link:** [Streamlit App](https://share.streamlit.io/your-repo/streamlit-app)
""")

# Project 2
st.subheader("Project 2: Data Analysis with Python")
st.write("""
    This project involves analyzing a dataset and visualizing the results using Python.
    - **Technologies Used:** Python, Pandas, Matplotlib
    - **Description:** Analysis of data to uncover trends and patterns.
    - **Link:** [GitHub Repository](https://github.com/sewyyyy/streamlit-portfolio.git)
""")

# Contact Information
st.header("Contact Me")
st.write("""
    - **Email:** dalanvincent@gmail.com
    - **GitHub:** [Your GitHub Profile](https://github.com/yourprofile)
""")

# Add any other sections or components you find relevant
