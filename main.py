import streamlit as st


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

mydata = [
    ['a', 'b', 'c'],
      [12, 34, 56],
      ['Geeks', 'for', 'geeks!']
]
st.header("Dashboard")
for i in range(3):  
    col1, col2= st.columns(2)
    col1.info(mydata[i][i])
    st.info( col2.metric("Humidity", "86%", "4%") )
    
