import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

#setting up the basic page layout
st.set_page_config(
    page_title='Ayder Dashboard',
    page_icon='clipboard',
    layout='wide'   
)

#data path
data_path='./survey.csv'

#lets load data from datasource or cached
@st.cache_data
def load_data():
    data=pd.read_csv(data_path)
    return data

df=load_data()

#convert the text into small letter
df=df.applymap(lambda x:x.lower() if isinstance(x,str) else x)

#adding filter
options=df['Country'].unique()
option=st.selectbox('select column',options)

#create a filtered dataset
filtered_data=df[df['Country']==option]

#length of the filtered data
length_filtered=len(filtered_data)

#gender
num_males=len(filtered_data[filtered_data['Gender']=='male'])
              
num_female=len(filtered_data[filtered_data['Gender']=='female'])

#remote workers or not
yes_remote=len(filtered_data[filtered_data['remote_work']=='yes'])
no_remote=len(filtered_data[filtered_data['remote_work']=='no'])

#works at tech
works_tech=len(filtered_data[filtered_data['tech_company']=='yes'])
non_tech=len(filtered_data[filtered_data['tech_company']=='no'])

placeholder=st.empty()

##applying css to the streamlit app


with placeholder.container():
    #there is going to be 4 features to be seen here
    kpi1,kpi2,kpi3,kpi4=st.columns(4)

    with st.container():
        with kpi1:
            #st.markdown('Gender')
            ch_gen=st.selectbox('Choose Gender',['male','female'])
            st.write(ch_gen)
            if(ch_gen=='male'):
                st.write(num_males)
            else:
                st.write(num_female)

    with st.container():
        with kpi2:
            st.markdown('Age')
            st.write(round(filtered_data['Age'].mean()))

    with st.container():
        with kpi3:
        ## st.markdown('remote-worker')
            rm_mk=st.selectbox('Remote Workers',['remote-work','non-remote-work'])
            if(rm_mk=='remote-work'):
                st.write(yes_remote)
            else:
                st.write(no_remote)

    with st.container():
        with kpi4:
            tech_mk=st.selectbox('Tech Company',['work-at-tech','non-tech'])
            if(tech_mk=='work-at-tech'):
                st.write(works_tech)
            else:
                st.write(non_tech)

#lets add interactive charts
#interact_1,interact_2=st.columns(2)
#fig=go.Figure()
#fig.add_trace(go.Histogram(x=df['mental_health_consequence'],y=df['phys_health_consequence']))

# #display what to display
# def create_update_buttons():
#     button=[]
#     for x_col in df.columns:
#         for y_col in df.columns:
#             if x_col != y_col:
#                 button.append(
#                     dict(
#                     label=f'{x_col} vs f{y_col}',
#                     method='update',
#                     args=[
#                         {'x':df[x_col].tolist(),'y':df[y_col].tolist()},
#                         {'title',f'Histogram of {x_col} vs {y_col}'}
#                     ]
#                     )   
#                 )

#     return button


# fig.update_layout(
#     title='select X and Y Axes for Histogra',
#     updatemenus=[
#         dict(
#             buttons=create_update_buttons(),
#             direction='down',
#             showactive=True,
#             x=0.1,
#             xanchor='left',
#             y=1.15,
#             yanchor='top'
#         )
#     ],
#     xaxis_title='X Axis',
#     yaxis_title='Y Axis'
# )


# fig.show()


#simple histogram
fig=px.histogram(df,x='mental_health_interview')
fig.show()