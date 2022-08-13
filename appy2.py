import streamlit as st

st.write('Hello World')

url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-07/coffee_ratings.csv'
#url = '../data/raw/coffee.csv'
df_raw = pd.read_csv(url)
df_raw.to_csv('../data/raw/coffee.csv')
df_raw.info()


X = df.drop(['total_cup_points','specialty'], axis=1)
y = df['specialty']