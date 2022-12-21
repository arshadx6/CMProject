import streamlit as st
from PIL import Image

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
x=mydata.size
st.write(x)
for i in range(mydata.size):
    
    col1, col2= st.columns(2)
    col1.header(mydata[i][i])
    col2.metric("Humidity", "86%", "4%")
