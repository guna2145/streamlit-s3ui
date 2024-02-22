import streamlit as st
import psycopg2

with st.form("register"):
   username=st.text_input("Username")
   password=st.text_input("Password")
   confirm_password=st.text_input("Confirm Password")

   submitted = st.form_submit_button("Submit")
   if submitted:
    if password==confirm_password and username:
          conn = psycopg2.connect(database="stream_users", user="postgres", 
                        password="1234", host="localhost", port="5432") 
          #conn.autocommit = True
          sql =f"""INSERT INTO users (username,password) VALUES('{username}','{password}')"""
          cursor = conn.cursor()
          cursor.execute(sql)
          conn.commit() 
          cursor.close()
          conn.close()
          st.info("Registration Completed")
    else:
        st.warning("Your password does not match or  username is empty")

if st.button("Back"):
    st.switch_page("myapp.py")
        