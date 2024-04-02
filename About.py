import streamlit as st

def main():
    st.title("Welcome! I am Trupti")

    st.header("About Me")
    st.write("""
    Hello There,
    I'm Trupti Gurudatta Gavit, a graduate from IIT Bombay. I've recently developed a strong interest in Generative AI. I've been diving deep into this field, taking courses and learning as much as I can. It's an exciting journey that combines technology with creativity. Before this, I've worked in different roles, like helping with research projects and managing communities. But now, my focus is on exploring the possibilities of AI. I'm eager to apply what I've learned to contribute to the world of Generative AI. It's all about pushing boundaries and making new discoveries.
    """)

    st.header("Education")
    st.write("""
    - [B.Tech] in [Metallurgical Engineering and Material Science], [Indian Institute of Technology, Bombay], [2019]
    
    """)
    st.header("Skills")
    st.write("""
    - HTML, CSS, JavaScript, C++, Python, Machine Learning Algorithms, React Native, Pytorch,Tensorflow, Streamlit, Generative AI, Prompt Engineering, Figma, Canva, Shapr3D,LLMs    """)
   

    st.header("Work Experience")
    st.write("""
    - [PROJECT RESEARCH ASSISTANT], [Chemical Engineering, IIT Bombay], [June 2019 – Dec 2023]
    - [BUSINESS DEVELOPMENT EXECUTIVE], [Drivensteel Inc ], [Mar 2021 – Oct 2021]
    - [COMMUNITY MANAGER], [Oyela], [June 2022 – Jan 2023]
    """)
    st.header("My GenAI Projects")
    list=["Social Media Caption Generator: Engineered a tool for creating captivating social media captions using opensource LLM models","MCQ Generator: Developed an efficient system for generating multiple-choice questions from givrn text or pdf for educational purpose.","Chat with PDF: Created an intuitive solution for seamless interaction with large and multiple PDF documents using langchain and vector database.","Nutrition Value Calculator: Designed an intelligent app for informed dietary decisions using advanced AI capabilities.","Image to Text Generation: Implemented AI-driven image recognition for accurate text extraction from images.","YouTube Video Summarizer: Engineered a summarization tool for condensing Youtube videos efficiently with AI.","Interactive Chat with AI: Developed a user-friendly AI chat interface for engaging interactions.","Invoice Extractor: Utilized AI algorithms for automated extraction of essential information from invoices-images."]
    for i in list:
        st.write("- " + i)


    st.header("Courses")
    st.write("""
    - • Generative AI For Data Scientists|| Specialization || IBM (https://www.coursera.org/account/accomplishments/certificate/V9MW4AUQ3A7Y)
    - • Generative AI For Cyber Security Professionals || Specialization || IBM (https://www.coursera.org/account/accomplishments/certificate/V9MW4AUQ3A7Y)
    - • Generative AI: Prompt Engineering Basics || IBM (https://www.coursera.org/account/accomplishments/certificate/V9MW4AUQ3A7Y)
    - • Responsible AI in the Generative AI era || Fractal (https://coursera.org/share/dda37e246fc21aac6bb022101134b013)
    - • Introduction to Prompt Injection Vulnerabilities || Coursera (https://coursera.org/share/cf7cffe9cce301ae0b1578d351619aaf)
    - • Foundations of User Experience (UX) Design || Google (https://www.coursera.org/account/accomplishments/verify/KHX84K3WSR2Q?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=course)
    - • Innovation Through Design: Think, Make, Break, Repeat || University of Sydney (https://coursera.org/share/e2027567079d3fc0c4922e688e3b4170)
    - • Python For Data Science || IBM (https://www.credly.com/badges/5716bb44-d6dd-4226-8356-a75520b738b7?source=linked_in_profile)
    """)

    st.header("My Other Projects")
    st.write("Apart from My Strong Interest in Generative AI, I have worked and tried to gain knowledge in multiple areas like Research (Chemical Engineering), UI-Designs, Web Developement and I have described my projects below ")

    st.subheader("My Figma UI Designs")
    col1, col2=st.columns(2)
    with col1:

        st.markdown(
            '<iframe src="https://www.behance.net/embed/project/188589391?ilo0=1"  height="237" width="303" allowfullscreen lazyload frameborder="0" allow="clipboard-write" refererPolicy="strict-origin-when-cross-origin"></iframe>',
            unsafe_allow_html=True
        )

   
        st.markdown(
            '<iframe src="https://www.behance.net/embed/project/188504813?ilo0=1"   height="237" width="303" allowfullscreen lazyload frameborder="0" allow="clipboard-write" refererPolicy="strict-origin-when-cross-origin"></iframe>',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<iframe src="https://www.behance.net/embed/project/188592541?ilo0=1"  height="237" width="303"  allowfullscreen lazyload frameborder="0" allow="clipboard-write" refererPolicy="strict-origin-when-cross-origin"></iframe>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<iframe src="https://www.behance.net/embed/project/185402941?ilo0=1" height="237" width="303" allowfullscreen lazyload frameborder="0" allow="clipboard-write" refererPolicy="strict-origin-when-cross-origin"></iframe>',
            unsafe_allow_html=True
        )

    st.subheader("My Research Projects")
    st.markdown('''
    :blue[Project1: Development of the grease for contact forming of acrylic sheets in single engine Helicopters]''')
    st.markdown('''
    :blue[Hindustan Aeronautics Limited- Chemical Engineering, IIT Bombay]''')
    list=["Analyzed greases using techniques like ICP-AES, DSC, Microscopy, Rheology, Melting and dropping point.","designed our own techniques to compare properties and select best grease among them","Prepared 10 different greases with different compositions in large quantity (up to 100kg)","Evaluated acrylic sheet forming process that uses grease as lubricant"]
    for i in list:
        st.caption("- " + i)

    st.markdown('''
    :blue[Project2: Scale Formation in Injection Water Heat Exchangers at Mangala Processing Terminal]''')
    st.markdown('''
    :blue[Cairn-Vedanta- Chemical Engineering, IIT Bombay]''')
    list=["Investigated the cause of debris formation in polymer flooding for crude oil extraction","Explored over 50 different element-polymer combinations to identify the root cause of debris formation","Proposed cost-effective solutions to mitigate debris formation and provided practical recommendations"]
    for i in list:
        st.caption("- " + i)

    
    st.subheader("My React Native-Full Stack App Developement Project")
    list=["Developed full-stack React Native Android app for food-based dating.","Implemented MongoDB for efficient database management."]
    for i in list:
        st.caption("- " + i)
    st.link_button("Github Link","https://github.com/TruptiGavit/Foodmate--Dating-App-React-Native-")

    st.subheader("Contact Information")
    st.write("""
    - Email: [truptigavit100@gmail.com]
    - LinkedIn: [https://www.linkedin.com/in/trupti-g-078829b2/]
    - GitHub: [https://github.com/TruptiGavit]
    - Behance: [https://www.behance.net/truptiigavit]
    - Contact No: [+91 8433540271]
    """)

    st.header("Thank you for visiting :)")


if __name__ == "__main__":
    main()