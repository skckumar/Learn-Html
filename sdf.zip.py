import streamlit as st

def add_custom_css():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://i.postimg.cc/nhX3KfVw/synthwave-car-ai-162023.png");
            background-size: cover;
  <font color="white"></font>
        """,
        unsafe_allow_html=True
    )

# Call the function to add custom CSS
add_custom_css()
st.html("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learn Html with Sk</title>
</head>
<body background="synthwave-car-ai-162023.png">
 

""")
st.sidebar.title("Learn with sk")
st.sidebar.image("we.png")
st.sidebar.link_button("Youtube","https://youtube.com/shorts/t2s5MqeU9jI?si=bebqULeE31Bn7Qq2")
st.sidebar.link_button("instagram","https://www.instagram.com/shivam_python_700?igsh=Z3lpNjNkczB2aHp5")
st.title("Learn with sk")
st.code("""
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

</body>
</html>
""")




