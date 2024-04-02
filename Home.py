import streamlit as st
from st_pages import Page, add_page_title, show_pages

def main():
    
    st.header("Hi,I am Trupti")
    st.subheader("Welcome to my Portfolio")
    st.write("Hello There,I'm Trupti Gurudatta Gavit, a graduate from IIT Bombay. I've recently developed a strong interest in Generative AI. I've been diving deep into this field, taking courses and learning as much as I can. It's an exciting journey that combines technology with creativity. Before this, I've worked in different roles, like helping with research projects and managing communities. But now, my focus is on exploring the possibilities of AI. I'm eager to apply what I've learned to contribute to the world of Generative AI. It's all about pushing boundaries and making new discoveries.")
    st.header("My GenAI Projects")
    st.subheader("You can interact with different projects by switching between pages listed on sidebar")
    list=["Social Media Caption Generator: Engineered a tool for creating captivating social media captions using opensource LLM models","MCQ Generator: Developed an efficient system for generating multiple-choice questions from givrn text or pdf for educational purpose.","Chat with PDF: Created an intuitive solution for seamless interaction with large and multiple PDF documents using langchain and vector database.","Nutrition Value Calculator: Designed an intelligent app for informed dietary decisions using advanced AI capabilities.","Image to Text Generation: Implemented AI-driven image recognition for accurate text extraction from images.","YouTube Video Summarizer: Engineered a summarization tool for condensing Youtube videos efficiently with AI.","Interactive Chat with AI: Developed a user-friendly AI chat interface for engaging interactions.","Invoice Extractor: Utilized AI algorithms for automated extraction of essential information from invoices-images."]
    for i in list:
        st.caption("- " + i)
    show_pages(
        [
            Page("captiongenerator.py", "Social Media Caption Generator"),
         
            
            Page("healthapp.py", "Nutrition value calculator"),
            Page("vision.py", "Image to Text Generation"),
            Page("youtubesummerizer.py", "YouTube Video Summerizer"),
            Page("qachat.py", "Interactive Chat with AI"),
            Page("invoiceextractor.py", "Invoice Extractor"),
            Page("JBResumematch.py", "Resume- JD matching"),
            Page("About.py", "About Me"),
            
        ]
    )

    add_page_title()  # Optional method to add title and icon to current page

if __name__ == "__main__":
    main()