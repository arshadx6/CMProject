import streamlit as st
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

mydata = [
    ['a', 'b', 'c'],
      [12, 34, 56],
      ['Geeks', 'for', 'geeks!']
]
st.header("Dashboard")

st.markdown("""
    ### Hemoglobin
    ##### lwrflwrjf;wrjf wrofjwo;rf jw;ojf w;ofjw; oefjw;fj;wfj w;fj wofjw;o fjwo;jf w;fj w;rkjlfknlflsfklfj fj f
""")
for i in range(3):  
    col1, col2 , col3 = st.columns(3)
    with col1:
        st.header(mydata[i][i])
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.metric("Humidity", "86%", "-8%")


    with col3:
        st.header("An owl")


