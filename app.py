import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.subplots as sp

# Load the dataset
@st.cache
def load_df():
    return pd.read_csv('desktop/streamlit-dashboard/dataset.csv') 

df = load_df()
df_grouped = df.groupby(['year', 'sex'])[['total_inactive_population', 'total_unemployed_population', 'total_employed_population','Basic_unemployment','Intermediate_unemployment','Advanced_unemployment','age_group']].sum().reset_index()
# Simple Streamlit app using Plotly
st.title("Streamlit Dashboard with Plotly")
st.write("This is a simple example dashboard with Plotly visualizations.")

fig1 = px.line(df_grouped, x="year", y="total_inactive_population", color="sex",color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Inactive Population By Sex")
st.plotly_chart(fig1)
fig2 = px.pie(df_grouped, values='total_inactive_population', names='sex', color='sex',
             color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Inactive Population By Sex")
st.plotly_chart(fig2)

fig3 = px.line(df_grouped, x="year", y="total_unemployed_population", color="sex", color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Unemployed Population")
st.plotly_chart(fig3)
fig4 = px.pie(df_grouped, values='total_unemployed_population', names='sex', color='sex',
             color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Unemployed Population")
st.plotly_chart(fig4)

fig5 = px.line(df_grouped, x="year", y="total_employed_population", color="sex", color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Employed Population")
st.plotly_chart(fig5)
fig6 = px.pie(df_grouped, values='total_employed_population', names='sex', color='sex',
             color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Employed Population")
st.plotly_chart(fig6)


fig7 = px.pie(df_grouped, values='Basic_unemployment', names='sex', color='sex',
             color_discrete_map={'male':'blue', 'female':'yellow'}, title="Unemployment status by basic education",hole=0.5)
st.plotly_chart(fig7)
fig8=px.bar(df,x='age_group',y='Basic_unemployment',color='sex',color_discrete_map={'male':'blue', 'female':'yellow'},title='sum of unemployment by basic ed')
st.plotly_chart(fig8)
fig9 = px.pie(df_grouped, values='Intermediate_unemployment', names='sex', color='sex',
             color_discrete_map={'male':'blue', 'female':'green'}, title="Unemployment status by intermediate education",hole=0.5)
st.plotly_chart(fig9)
fig10=px.bar(df,x='age_group',y='Intermediate_unemployment',color='sex',color_discrete_map={'male':'blue', 'female':'green'},title='sum of unemployment by intermediate ed')
st.plotly_chart(fig10)
fig11 = px.pie(df_grouped, values='Advanced_unemployment', names='sex', color='sex',
             color_discrete_map={'male':'blue', 'female':'brown'}, title="Unemployment status by advanced education",hole=0.5)
st.plotly_chart(fig11)
fig12=px.bar(df,x='age_group',y='Advanced_unemployment',color='sex',color_discrete_map={'male':'blue', 'female':'brown'},title='sum of unemployment by advanced ed')
st.plotly_chart(fig12)