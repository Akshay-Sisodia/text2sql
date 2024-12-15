import os
import streamlit as st

def select_database_file():
    """
    Provides a file uploader and selection mechanism for SQLite database files.
    
    :return: Path to the selected database file
    """
    # File uploader for SQLite databases
    uploaded_file = st.file_uploader("Upload SQLite Database", type=['db', 'sqlite'])
    
    if uploaded_file is not None:
        # Save the uploaded file
        temp_db_path = os.path.join("temp_databases", uploaded_file.name)
        os.makedirs("temp_databases", exist_ok=True)
        
        with open(temp_db_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"Database file '{uploaded_file.name}' uploaded successfully!")
        return temp_db_path
    
    # Option to select from existing databases in a directory
    st.subheader("Or select an existing database:")
    existing_db_dir = "databases"  # You can change this to your preferred directory
    os.makedirs(existing_db_dir, exist_ok=True)
    
    # List all .db and .sqlite files in the directory
    db_files = [f for f in os.listdir(existing_db_dir) if f.endswith(('.db', '.sqlite'))]
    
    if db_files:
        selected_db = st.selectbox("Choose a database:", db_files)
        return os.path.join(existing_db_dir, selected_db)
    
    st.info("No existing database files found. Please upload a database.")
    return None