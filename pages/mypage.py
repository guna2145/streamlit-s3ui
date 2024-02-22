
import streamlit as st
import boto3
import os

session = boto3.Session( aws_access_key_id=st.secrets["AWS_ACCESS_KEY_ID"], aws_secret_access_key=st.secrets["AWS_SECRET_ACCESS_KEY"])

s3 = boto3.client('s3')
response = s3.list_buckets()

def list_s3_bucket():
    selection = st.selectbox("SELECT S3 BUCKET", [bucket["Name"] for bucket in response['Buckets']])
    if selection:
        s3_res = session.resource('s3')
        my_bucket = s3_res.Bucket(selection)

        for my_bucket_object in my_bucket.objects.all():
            st.checkbox(f"{my_bucket_object.key} {my_bucket_object.last_modified} {my_bucket_object.size}",key=my_bucket_object.key)
        
        if st.button("Download"):   
            for file,state in st.session_state.items():
                if state:
                    s3.download_file(selection, file, file)
                    #edited_df = st.data_editor(file)
        
        st.markdown("#")
        filename = st.file_uploader("UPLOAD FILE")
        if filename:
            s3.upload_fileobj(filename, selection, filename.name)

def return_to_home():
    if st.button("Back"):
        st.switch_page("myapp.py")

list_s3_bucket()
return_to_home()





