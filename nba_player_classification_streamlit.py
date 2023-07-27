import streamlit as st
import pandas as pd
import plotly.express as px

# Title our app
st.title('NBA Player Classification')

# Read in our data and drop columns that aren't user-friendly
csv_url = 'https://docs.google.com/spreadsheets/d/1-vu0l5MrdyGcEDnvML5J5kYHT3jP7ai8jgoSWb5dLDM/export?format=csv&gid=0'
data = pd.read_csv(csv_url)
data.drop(columns = ['PCA 1', 'PCA 2', 'PCA 3', 'Category'], inplace = True)

# Add in filter for user to filter by team and player type
teams = data['Tm'].drop_duplicates().sort_values()
team_filter = st.selectbox('Team', teams)

# Filter data by user selected filters
filtered_data = data[(data['Tm'] == team_filter)].reset_index(drop = True)

# Load filtered data in Streamlit
st.dataframe(filtered_data)

# Create pie chart with distribution of positions by team
fig = px.pie(filtered_data,
             values = filtered_data['Category Name'].value_counts().values,
             names = filtered_data['Category Name'].value_counts().index
             )
st.plotly_chart(fig, theme = 'streamlit')