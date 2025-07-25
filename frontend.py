import streamlit as st
import backend
shloka=""
divine=""
speak=""
if 'text_input' not in st.session_state:
    st.session_state.text_input=""
else:
    res=backend.getans(st.session_state.text_input)
    qu=st.session_state.text_input
    st.session_state.text_input=""
    shloka=res['metadatas'][0][0]['verse']
    speak=res['metadatas'][0][0]['speak']
    prompt=f"""
       I am sharing a sacred verse from the Bhagavad Gita.
      Please follow this exact structure in your response:

      First, give the clear and concise meaning of the verse in bold.

      Then, in a new paragraph, respond to the devotee's question like a loving parent, god, or divine guide — offering compassionate spiritual guidance based on the message of the shloka.

      Here is the input:

      Shloka (Sanskrit):
      {shloka}

      Devotee’s Question:
      {qu}

    """
    divine=backend.promptans(prompt).text
    speak=speak.split('\n')
    shloka=shloka.split('\n')
    shloka="<br>".join(shloka)
    speak="<br>".join(speak)
    print(prompt)
    
st.markdown("""
    <style>
    /* Remove padding from main content area */
    .main, .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }

    /* Optional: remove padding from header/title */
    header, footer, .css-18ni7ap.e8zbici2 {
        padding: 0;
        margin: 0;
    }

    /* Optional: remove hamburger menu and footer */
    #MainMenu, footer {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)


container1=st.container()
st.set_page_config(layout="wide")  # Make layout wider by default

st.markdown("""
    <style>
    /* Set the main background */
    .stApp {
        background-color: #fffff0;
    }
    </style>
""", unsafe_allow_html=True)
    
left_col, center_col,=st.columns([1.5,4])

with center_col:
    with st.container():
         st.markdown(f"""
        <div style="
            height: 480px;
            overflow-y: auto;
            padding: 20px;
            background-color: #fffaf0;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        ">
            {divine}
        </div>
    """, unsafe_allow_html=True)

     mssg=st.text_input(label="Your prompt",key="text_input",value=st.session_state.text_input)
with left_col:
    st.markdown(f"""
        <div style="
            position: relative;
            background-color:#800000;
            height: 95vh;
            width: 100%;
            border-radius: 10px;
        ">
        <div style='
          font-family: "Cinzel", serif;
         font-size: 30px;
         color: #FFD700;
         text-align: center;
         padding: 0px 30px;
         border-radius: 12px;
         letter-spacing: 2px;
         text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);'>
         GitaSarthi</div>
           
                
         <div style='
                margin-top: 40px;
                font-family: "Sanskrit Text", "Noto Serif Devanagari", serif;
                font-size: 16px;
                color: #fff5cc;
                text-align: center;
                line-height: 1.8;
                white-space: pre-line;
                padding: 0 20px;
            '>
             {shloka}
         </div>

         <div style='
                margin-top: 40px;
                font-family: "Sanskrit Text", "Noto Serif Devanagari", serif;
                font-size: 17px;
                color: #fffff0;
                text-align: center;
                line-height: 1.8;
                white-space: pre-line;
                padding: 0 20px;
            '>
             {speak}
         </div>


         </div>
    """, unsafe_allow_html=True)    
        
