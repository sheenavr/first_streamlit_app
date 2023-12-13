import streamlit
import pandas

streamlit.title('My parents new Healthy Diner')
streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗Omega3 & Blueberry Oat Meal')
streamlit.text('🍞 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑 Avacado toast')
streamlit.text('🐔 Hard boiled free-range egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

