import streamlit as st
from streamlit_option_menu import option_menu

#st.title('Enjoy ayder dashboard')

#this is the menu
with st.container():
     selected=option_menu(
            menu_title=None,
            options=['Home','objective history','current pregnancy','general medical','pregnancy follow up'],
            #icons=['house','clock-history','activity'],
            menu_icon='cast',
            default_index=0,
            orientation="horizontal",

    )

#change the background color of the body
st.markdown("""
    <style>
            [data-testid="stAppViewContainer"]{
                background-color:#A9A9A9;
            }
    </style>
""",unsafe_allow_html=True)

#this is the 