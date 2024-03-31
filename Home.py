import streamlit as st
from pages import About, Projects,Otherprojects,Certifications,ContactMe

def main():
    # st.sidebar.title("Navigation")

    # Mapping of display names to page modules
    page_mapping = {
        "About Me": About,
        "My Gen AI Projects": Projects,
        "My All Other Projects": Otherprojects,
        "My Certified Courses":Certifications ,
        "Contact-Me": ContactMe
    }

    selected_page = st.sidebar.radio("Go to", list(page_mapping.keys()))

    # Load the selected page module and call its main function
    selected_page_module = page_mapping[selected_page]
    selected_page_module.main()

if __name__ == "__main__":
    main()