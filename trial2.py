import streamlit as st
st.set_page_config(page_title="My Dashboard",layout="wide")

css="""
    <style>
        .navbar{
           display:flex;
            background-color:#F0F8FF;
            position:fixed;
            justify-content:space-around;
            width:100%;
            height:3rem;
            padding:10px;
        }

        .navbar a{
            color:red;
            text-decoration:none;
            font-weight:bold;
            /*padding:10px 20px;*/
            border-radius:5%;
        }
        .navbar a:hover{
            background-color:#A9A9A9;
        }
        </style>
     """


st.markdown(css,unsafe_allow_html=True)

#lets define the contents of the navigation bar
pages=["home","Obsteric History","current pregnancy","general medical"]
nav_html='<div class="navbar">'
for page in pages:
    nav_html+=f'<a href="#{page}">{page}</a>'

nav_html+='</div>'

st.markdown(nav_html,unsafe_allow_html=True)
