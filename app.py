import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("COVID-19 Dashboard")
st.write("Upload your dataset")

file = st.file_uploader("Upload CSV", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    st.write("Dataset Preview")
    st.write(df.head())

    # Top Countries
    st.subheader("Top 10 Countries by Confirmed Cases")
    top10 = df.sort_values(by='Confirmed', ascending=False).head(10)

    fig1, ax1 = plt.subplots()
    ax1.bar(top10['Country/Region'], top10['Confirmed'])
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    # Region-wise
    st.subheader("Region-wise Comparison")

    fig2, ax2 = plt.subplots()
    sns.barplot(x='WHO Region', y='Confirmed', data=df, ax=ax2)
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    # Death & Recovery
    st.subheader("Death vs Recovery Rate")

    df['Death Rate'] = (df['Deaths'] / df['Confirmed']) * 100
    df['Recovery Rate'] = (df['Recovered'] / df['Confirmed']) * 100

    top10 = df.sort_values(by='Confirmed', ascending=False).head(10)

    fig3, ax3 = plt.subplots()
    ax3.plot(top10['Country/Region'], top10['Death Rate'], label='Death Rate')
    ax3.plot(top10['Country/Region'], top10['Recovery Rate'], label='Recovery Rate')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(fig3)