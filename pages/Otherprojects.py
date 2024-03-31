import streamlit as st
from pages.subpages import 

def main():
    st.title("Page 1")
    st.write("This is Page 1 content.")

    # Subpage navigation
    # st.sidebar.subheader("Subpages")
    subpage_mapping = {
        # "Data Science Vision with streamlit": datasciencevision,
        # "Machine Learning with streamlit": machineL,
        # "Interactive dashboards": interactivedashboard

    }
    selected_subpage = st.sidebar.radio("Go to", list(subpage_mapping.keys()))

    # Load the selected subpage module and call its main function
    selected_subpage_module = subpage_mapping[selected_subpage]
    selected_subpage_module.main()

if __name__ == "__main__":
    main()