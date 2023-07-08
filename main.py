import os
import streamlit as st
from llama_index import SQLStructStoreIndex, SQLDatabase
from llama_index.indices.struct_store import SQLContextContainerBuilder
from sqlalchemy import create_engine, inspect, text, MetaData, Table, DDL
from sqlalchemy.schema import CreateTable
import my_key
import json
import db_helper
from langchain import OpenAI
from llama_index import ServiceContext, LLMPredictor
from langchain.chat_models import ChatOpenAI

def load_selected_files():
    # Load selected files from a JSON file
    selected_files = []
    if os.path.exists('selected_files.json'):
        with open('selected_files.json', 'r') as file:
            selected_files = json.load(file)
    return selected_files

# Helper function: Save selected SQL files to JSON
def save_selected_files(selected_files):
    # Save selected files to a JSON file
    with open('selected_files.json', 'w') as file:
        json.dump(selected_files, file)

# Set up Streamlit app title and image
st.title("MySQL Large Model Query Assistant")
image = open('background.jpg', 'rb').read()
st.image(image)

# Set up input fields for MySQL connection details
col1, col2, col3 = st.columns(3)
with col1:
    username = st.text_input("Username", value="root")
with col2:
    host = st.text_input("Host", value="localhost")
with col3:
    password = st.text_input("Password", type="password", value="root")
with col1:
    port = st.text_input("Port", value="3306")
with col2:
    database = st.text_input("Database", value="my_shop")
with col3:
    db_url = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}?charset=utf8'

if st.button("Get Database Data"):
    db_helper.scan_table_to_file(db_url)

# Load previously selected files from JSON
selected_files = load_selected_files()
# Create a multi-select box to choose SQL file names
sql_files = os.listdir('data')
selected_files = st.multiselect("Select SQL Files", sql_files, selected_files)

if st.button("Update Index"):
    # Save the selected files to JSON
    save_selected_files(selected_files)
    db_helper.build_index(selected_files)

tab1, tab2 = st.tabs(["Self-Service Query", "Smart Q&A"])

with tab1:
    st.subheader("Self-Service Query")
    db_query_str = st.text_area("Query Command")
    request_str = st.text_area("Query Requirements", value="Retrieve only 3 records")
    if st.button("Query"):
        query_str = db_helper.create_query(db_query_str, request_str)
        st.code(query_str, language='sql')
        df = db_helper.run_sql(db_url, str(query_str))
        st.dataframe(df)

with tab2:
    st.subheader("Architecture Analysis")
    db_question = st.text_area("Enter a Question")
    if st.button("Analyze"):
        result = db_helper.analyse_db(db_question)
        st.write(result, width=500)
