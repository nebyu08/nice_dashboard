import streamlit as st
from streamlit_option_menu import option_menu
import distribution,relationship,home,heatmap

class MultiPage:
    def __init__(self) -> None:
        self.apps=[]

    def add_app(self,title,function):
        self.apps.append({
            "title":title,
            "function":function
        })

    def run(self):
        with st.sidebar:
            app=option_menu(
                menu_title='Menu',
                options=[app['title'] for app in self.apps],
                #options=['Home','distribution','relationship'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container":{"padding":"10px","background-color":"#000000"},
                    "icon":{"color":"white","font-size":"23px"},
                    "nav-link":{"color":"white","font-size":"23px","text-align":"10px","--hover-color":"#228B22"},
                    "nav-link-selected":{"background-color":"#006400"}
                }
            )
        for chosen_app in self.apps:
            if app==chosen_app['title']:
                chosen_app['function']()

        


#initiating the multipage
app=MultiPage()

#add the pages
app.add_app("Home",home.app)
app.add_app("distribution",distribution.app)
app.add_app("relationship",relationship.app)
app.add_app("heatmap",heatmap.app)

app.run()

