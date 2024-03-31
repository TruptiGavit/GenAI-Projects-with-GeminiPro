import streamlit as st
from pages.subpages import healthapp, sqlllm,qachat,pdfextractor,youtubesummerizer,JBResumematch,vision,invoiceextractor

def main():
    st.title("My Generative AI Projects (Gemini Pro)")
    st.write("This is Page 1 content.")

    # Subpage navigation
    # st.sidebar.subheader("Subpages")
    subpage_mapping = {
        
        "Nutrition value calculator": healthapp,
        "SQL Query Generator": sqlllm,
        "Interactive Chat with AI": qachat,
        "PDF Extractor": pdfextractor,
        "Youtube Video Summerizer": youtubesummerizer,
        "Image to Text Generation": vision,
        "Resume- JD matching": JBResumematch,
        "Invoice Extractor": invoiceextractor
    }
    selected_subpage = st.sidebar.radio("Go to", list(subpage_mapping.keys()))

    # Load the selected subpage module and call its main function
    selected_subpage_module = subpage_mapping[selected_subpage]
    selected_subpage_module.main()

if __name__ == "__main__":
    main()