import streamlit as st
import pandas as pd 
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide"
)

st.title(" Welcome to the smart blood report generator ")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


st.header("Dashboard")



df=pd.read_csv("./smartreport1.csv")
st.write(df)
for i in df.values:  
    col1, col2 , col3 = st.columns(3)
    with col1:
        st.header(i[1])
        st.subheader("Hemoglobin is a protein contained within red RBCs that sends oxygen from the lungs to the body’s tissues. The hemoglobin test is useful in diagnosing anemia, with many practitioners preferring this test over the hematocrit test.")
        

    with col2:
        st.subheader("Your levels are okay")
        st.subheader("")


    with col3:
        st.header("An owl")
        st.warning("sdasdasdasdasdSA")


