import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px 

st.set_page_config(layout='wide')

df = pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India ka Data viz')

selected_state = st.sidebar.selectbox('Select a State',list_of_states)

primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))



plot = st.sidebar.button("Plot Graph")


if plot:

    st.text("Size represents primary parameter")
    st.text("Color represents secondary parameter")


    if selected_state == 'Overall India':
        # plot for India
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', 
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=3, size=primary, color=secondary,
                  mapbox_style="carto-positron")
        st.plotly_chart(fig)

    else:
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', 
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=6, size=primary, color=secondary,hover_name='District',
                  mapbox_style="carto-positron")
        st.plotly_chart(fig)