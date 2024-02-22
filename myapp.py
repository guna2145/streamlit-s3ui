import streamlit as st
#from streamlit_extras.switch_page_button import switch_page
from time import sleep

st.header("Simple Data Management Application")
st.write("Please login to continue")    

username = st.text_input("Username", label_visibility = "visible")
password = st.text_input("Password", type="password")

db_username = ''
db_password = ''

if st.button("Log in"):
    conn = st.connection("postgresql", type="sql")
    df = conn.query(f"SELECT * FROM users where username='{username}' and password='{password}'", ttl="10m")
   
    for row in df.itertuples():
        db_username=row.username
        db_password=row.password

    if username==db_username and password==db_password:
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        sleep(0.5)
        st.write(df)
        st.switch_page("pages/mypage.py")
    else:
        st.error("Incorrect username or password")
    
if st.button("Register"):
    st.switch_page("pages/register.py")

