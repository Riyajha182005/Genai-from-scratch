import streamlit as st
import pandas as pd 
import numpy as np

## Title  of the Apllication 
st.title("Riya Jha")

## Display the simple text
st.write("This is a simple text ")

## Create a simple dataframe
df=pd.DataFrame({
    'First Column':[1,2,3,4],
    'Second Column':[9,5,6,5]
})

## Display the DatafRame
st.write("Here is the dataframe")
st.write(df)
st.line_chart(df)

## Create a line chart \
chart_data=pd.DataFrame(
  np.random.randn(20,3),columns=['A','B','C']

 )
st.line_chart(chart_data)


## Widgets
st.title("Text Input")
name=st.text_input("Enter your name")

if name:
    st.write(f"Hello !,{name} how's ur day going?")

## Lets make the slider 
age=st.slider("Select Your age",0,100,25)
st.write("Your age is ",age)

## Lets create a selection box
options=['python','C++','java','C']
choice=st.selectbox(f"Choose Your favourite Programming language,{name}",options)
st.write(f"You selected,{choice}.")

## Lets create a upload file button
uploaded_files=st.file_uploader("Choose a csv file",type="csv")
if uploaded_files is not None:
    df=pd.read_csv(uploaded_files)
    st.write(df)