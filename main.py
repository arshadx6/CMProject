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



df=pd.read_csv("./smart.csv")

for i in df.values:  
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(i[1])
        st.write(i[2])        

    with col2:
      
        st.subheader(str(i[4])+str(i[3]) + "  -  " + str(i[6]))
        if(i[5]=="Normal"):
            st.success(i[7])
        elif(i[5]=="High"):
            st.error(i[7])
        else:
            st.info(i[7])
        



       


