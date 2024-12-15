import streamlit as st
import pandas as pd
import requests
from db_manager import DatabaseManager
from query_gen import SQLQueryGenerator
from query_exec import SQLQueryExecutor
from db_selector import select_database_file

def get_available_models():
    """Fetch available models from the API and return their names."""
    try:
        response = requests.get("http://localhost:11434/api/tags")
        response.raise_for_status()
        data = response.json()
        models = [model["name"] for model in data.get("models", [])]
        return models
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching models: {e}")
        return []

def main():
    # Set page configuration
    st.set_page_config(page_title="Text2SQL App", page_icon=":robot_face:")
    st.title("🤖 Text to SQL Query Generator")
    
    # Select database file
    db_path = select_database_file()
    
    if db_path:
        # Initialize database manager
        db_manager = DatabaseManager(db_path)
        
        # Retrieve database metadata
        metadata = db_manager.get_database_metadata()
        
        # Display database schema information
        with st.expander("Database Schema"):
            for table, columns in metadata.items():
                st.subheader(f"Table: {table}")
                schema_df = [
                    {
                        "Column Name": col['name'], 
                        "Type": col['type'], 
                        "Primary Key": "Yes" if col['is_primary_key'] else "No"
                    } for col in columns
                ]
                st.table(schema_df)
        
        # Fetch available models
        model_options = get_available_models()
        if model_options:
            selected_model = st.selectbox("Select Ollama Model:", model_options)
        else:
            st.warning("No models available. Please check the API.")

        # User input for task
        user_task = st.text_area("Enter your task in natural language:", 
                                placeholder="e.g., Show me the top 5 customers by total purchase amount")
        
        # Generate and execute SQL query
        if st.button("Generate SQL Query"):
            if user_task:
                # Generate SQL query
                sql_query = SQLQueryGenerator.generate_sql_query(user_task, metadata, selected_model)
                
                if sql_query:
                    # Display generated SQL query
                    st.code(sql_query, language='sql')
                    
                    # Execute query and show results
                    columns, results = SQLQueryExecutor.execute_query(db_path, sql_query)
                    
                    if columns and results:
                        # Create a DataFrame for better display
                        results_df = pd.DataFrame(results, columns=columns)
                        
                        st.subheader("Query Results")
                        st.dataframe(results_df)
                    else:
                        st.warning("Could not execute the generated query.")
                else:
                    st.error("Failed to generate SQL query.")
            else:
                st.warning("Please enter a task description.")
    else:
        st.warning("Please upload or select a database file.")

if __name__ == "__main__":
    main()
