#Hello! This is Issac. This is my own code (with the help of online resources). Feel free to refrence this code for any projects of yours.

import streamlit as st
from PIL import Image

#Move set_page_config to the top
st.set_page_config(page_title="Caffeine Production", page_icon=":trees:", layout="wide")

#Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = "Eco-Impacts"

def navigate_to(page_name):
    st.session_state.page = page_name

#Sidebar navigation
st.sidebar.title("Navigation")
if st.sidebar.button("Eco-Impacts of Caffeine Production"):
    navigate_to("Eco-Impacts")
if st.sidebar.button("Dangers of Synthetic Caffeine"):
    navigate_to("Synthetic Caffeine") 
if st.sidebar.button("About Me"):
    navigate_to("About Me")
if st.sidebar.button("Source Code"):
    navigate_to("Source Code")

#Eco-Impacts of Caffeine Production page content
if st.session_state.page == "Eco-Impacts":

    col1, col2 = st.columns([0.8, 3])
    with col2:
        st.title("The Eco-Impacts of Caffeine Production")
    st.write("")
    st.success("")

    content_col, image_col = st.columns([4, 1.5])

    with content_col:
        st.subheader('_Consequences_')
        st.markdown("""
        - **Deforestation for Coffee Plantations:**
            - Leads to habitat loss, disrupting ecosystems and decreasing biodiversity.
            - Removes trees that absorb carbon dioxide, accelerating carbon release and contributing to climate change.
            - Causes increased greenhouse gases, intensifying global warming.
        """)
        st.write("")
        st.markdown("""
        - **Excessive Use of Chemical Fertilizers:**
            - Results in runoff that contaminates nearby water bodies, including aquifers, which are primary sources of potable water.
            - Polluted aquifers are difficult and costly to purify, posing long-term water quality risks.
        """)
        st.write("")
        st.markdown("""
        - **Monocropping in Coffee Farming:**
            - Depletes soil nutrients and reduces fertility over time.
            - Impacts long-term agricultural productivity and ecosystem health.
        """)

    with image_col:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        img = Image.open("issac1.jpg")
        st.image(img, caption="", width=350)

    
    st.success("")
    st.subheader('_Synthetic Caffeine_')
    content_col2, image_col2 = st.columns([4, 1.5])

    with content_col2:
        st.markdown("""
        - **What is it?:**
            - Produced in laboratories through chemical synthesis, using urea as a raw material.
            - It's absorbed more rapidly by the body compared to natural caffeine.
        """)
        st.write("")
        st.markdown("""
        - **Energy Consumption in Synthetic Caffeine Production:**
            - Requires significant energy for heating, cooling, mixing, and other manufacturing processes.
            - Relies on fossil fuels, primarily coal and oil.
        """)
        st.write("")
        st.markdown("""
        - **Environmental Impacts of Coal & Oil Usage:**
            - Coal produces harmful fly ash, contributing to acid rain & contaminating groundwater.
            - Oil extraction isn't consistent and slows down over time, requiring controversial techniques to be used such as fracking.
        """)

    with image_col2:
        st.write("")
        img2 = Image.open("issac2.jpg")
        st.image(img2, caption="Anhydrous synthetic caffeine", width=350)
        
    st.success("")
    st.subheader('_The Solution?_')
    content_col3, image_col3 = st.columns([1, 1.5])
    
    with content_col3:
        st.write("""
        **Implementing Sutainability:** Sustainability means making choices that benefit both the present and future, and it’s essential to apply this
        principle to coffee production. There are various ways to make coffee production more sustainable.
        """)
        st.write("")
        st.markdown("""
        - **Agroforestry Practices:**
            - Grow trees and crops together to provide shade for coffee plants, which helps conserve water,
            maintain soil health, and reduce the need for synthetic fertilizers and pesticides.
        """)
        st.write("")
        st.markdown("""    
        - **Water Conservation:**
            - Implement methods such as drip irrigation, wastewater recycling, and planting cover crops to reduce the water footprint in
            coffee production, addressing water scarcity in coffee-growing regions.
        """)
        st.write("")
        st.markdown("""
        - **Reduce Greenhouse Gas Emissions:**
            - Use renewable energy, reduce waste, and promote sustainable land practices to decrease emissions from coffee production,
            particularly from deforestation and synthetic fertilizer use.
        """)
        
        with image_col3:
            st.video("https://www.youtube.com/watch?v=oAoAUAhmAPE")
            
            st.write("Interested in more? Watch this video for in-depth information about the consquences and solutions to be brought to caffeine production.")
            
    
#Dangers of Synthetic Caffeine
elif st.session_state.page == "Synthetic Caffeine":
    col3, col4 = st.columns([0.74, 2.5])
    with col4:
        st.title("The Dangers of Synthetic Caffeine")
        st.write("")
    st.success("")
    
    col5, col6, = st.columns([500, 1.5])
    with col5:
        st.markdown(
    """
    <div style="text-align: center; max-width: 800px; margin: auto;">
        Synthetic caffeine is a laboratory-produced version of caffeine. Unlike caffeine extracted from natural sources like coffee or tea, synthetic caffeine is created through chemical synthesis processes in industrial settings. It’s produced by chemical synthesis of urea as a raw material, which is a substance formed by the breakdown of protein in the liver. Then, it’s combined with different chemicals such as methyl chloride and ethyl acetate. The raw form often glows with a bluish phosphorescence, which is removed through various rinsing processes.
    </div>
    """,
    unsafe_allow_html=True
)
    
    col7, col8 = st.columns([1, 2.5])
    with col8:
        st.write("")
        st.write("")
        img3 = Image.open("issac4.jpg")
        st.image(img3, caption="Breakdown of protein in the liver.", width=500)
    
    
    col9, col10 = st.columns([500, 2.5])
    with col9:
        st.success("")
        st.markdown(
    """
    <div style="text-align: center; max-width: 900px; margin: auto;">
        The production of synthetic caffeine is highly energy-intensive due to the chemical processes that require high temperatures and pressures. Using raw materials like urea and petrochemical derivatives, the synthesis involves steps like ammonia production through the Haber-Bosch process, known for its high energy demand. Additional processes, including methylation and purification via distillation, add to the energy consumption, which is typically met by burning fossil fuels or using non-renewable electricity sources. This heavy reliance on fossil fuels leads to significant greenhouse gas emissions, contributing to the overall carbon footprint and environmental impact of synthetic caffeine production.
    </div>
    """,
    unsafe_allow_html=True
)
        st.write("")
        st.write("")
        st.markdown(
    """
    <div style="text-align: center; max-width: 900px; margin: auto;">
        Synthetic caffeine is largely produced in unregulated labs in China, with three major factories exporting around four million kilograms annually to the U.S., including 1.8 million kilograms from CSPC Innovation Pharmaceutical Company. The industry lacks transparency and oversight, with limited public information and minimal foreign inspections, raising concerns about potential health risks and regulatory shortcuts. Many consumers are unaware that most caffeine is now synthetic, and energy drink manufacturers are not required to disclose this on labels. Additionally, China’s production practices raise contamination concerns due to environmental issues and inefficient chemical use.
    </div>
    """,
    unsafe_allow_html=True
)
        st.write("")
        st.success("")
        
        col11, col12 = st.columns([5, 7.5])
        with col12:
            st.header("In Conclusion...")
            st.write("")
            
        st.info("1. **Production Process and Energy Demand:** Synthetic caffeine is created in labs through chemical synthesis using urea, methyl chloride, and other chemicals, requiring high temperatures and pressures. This energy-intensive process, including ammonia synthesis via the Haber-Bosch method, relies on fossil fuels, leading to a substantial carbon footprint and environmental impact.")
        st.write("")
        st.info("2. **Lack of Transparency and Regulation:** Most synthetic caffeine is produced in unregulated factories in China, with three major facilities exporting millions of kilograms to the U.S. annually. The industry has minimal oversight and limited public information, raising health and safety concerns due to potential shortcuts and contamination risks.")
        st.write("")
        st.info("3. **Consumer Awareness and Labeling Issues:** Many consumers are unaware that most caffeine in products today is synthetic, and there is no requirement for energy drink manufacturers to disclose this on packaging. This lack of transparency may lead consumers to unknowingly consume synthetic caffeine.")
        
    pdf_path = "/Users/issactewolde/Desktop/Issac Tewolde Midterm Essay - The Dangers of Synthetic Caffiene (2).pdf"
    with open(pdf_path, "rb") as pdf_file:
        pdf_data = pdf_file.read()

#download button for synthetic caffeine essay
    st.write("")
    st.write("")
    st.subheader("Interested in more? Check out this essay which goes into depth about synthetic caffeine manufacturing.")
    st.download_button(
        label="Download PDF: The Dangers of Synthetic Caffeine",
        data=pdf_data,
        file_name="The Dangers of Synthetic Caffeine.pdf",
        mime="application/pdf"
)

#about me
elif st.session_state.page == "About Me":
    col5, col6 = st.columns([2.55, 3.5])
    with col6:
        st.title("About Me")
        st.write("")
    
    st.success("")
   
    
    st.markdown(
        """
        <div style="text-align: center;">
            <h3>Hello! My name is Issac Tewolde, and I am a student at James Madison University. I am passionate about exploring technology and science, volunteering to support my community, and staying active through fitness. I am currently pursuing a degree in Integrated Science & Technology with a minor in Honors Interdisciplinary Studies.</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.write("")
    img4 = Image.open("issac8.jpg")
    st.image(img4, caption="Volunteering at Mount Daniels - 2022", use_column_width=True)
    \
    
    st.markdown(
        """
        <div style="text-align: center;">
            <h3>
This website was entirely created by me using Python and Streamlit. I taught myself how to navigate and utilize the full range of features that Streamlit offers.</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.success("")

    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 20px;">
            <h1>Get In Touch With Me!</h1>
        </div>
        """,
        unsafe_allow_html=True,
)


    contact_form = """
    <form action="https://formsubmit.co/issac.tewolde88@gmail.com" method="POST" style="max-width: 500px; margin: auto;">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; margin-top: 6px; margin-bottom: 16px; box-sizing: border-box;">
        <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; margin-top: 6px; margin-bottom: 16px; box-sizing: border-box;">
        <textarea name="message" placeholder="Shoot me a message!" required style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; margin-top: 6px; margin-bottom: 16px; box-sizing: border-box; resize: vertical;"></textarea>
        <button type="submit" style="background-color: #04AA6D; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer; width: 100%;">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

#source code
elif st.session_state.page == "Source Code":
    col7, col8 = st.columns([2.20, 3.5])
    with col8:
        st.title("Source Code")
        st.write("")
    st.success("")
        
    with open("Tewolde.py", "r") as file:
        source_code = file.read()

    st.code(source_code, language='python')
    

#download button for source code
    st.header("Download Source Code")

    with open("Tewolde.py", "r") as file:
        source_code = file.read()

    st.download_button(
        label="Download",
        data=source_code,
        file_name="Tewolde.py",
        mime="text/plain"
)
