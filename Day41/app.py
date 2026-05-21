# Streamlit
# pip install streamlit

import streamlit as st
"""
st.title("My first Application")
st.header("Sales Report Analysis")
st.subheader("Profit Analysis")
st.text("Data Loading...")
name = st.text_input("Enter Your Name: ")
st.subheader("Name")

st.title("Calculator")
st.subheader("You Can add Two Numbers.")
num1 = st.number_input("Enter 1st Number")
num2 = st.number_input("Enter 2nd Number")
num3 = num1 + num2
if st.button("Addition"):
    st.subheader(f"Addition:  {num3}")

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = st.file_uploader("Upload Your File" , type=['xlsx'])
df = pd.read_excel(file)

# df = pd.read_excel(r"F:\Python\Python_Practice\Data\Financial_Sample.xlsx")
st.subheader("Dataset Sample")
st.dataframe(df.head())
df =df.bfill()
pbs =df.groupby("Segment").agg({'Profit':'sum'}).reset_index()
st.subheader("Profit By Segment")
st.dataframe(pbs)


fig, ax = plt.subplots(figsize=(8,3))
sns.barplot(x ='Segment', y='Profit', data=df, ax=ax)
st.pyplot(fig)

st.checkbox("I Agree!")
st.radio("Gender",['Male','Female'])
st.selectbox("Select Course",["DA","DS","FS"])
st.slider("Select Range",0,100)
