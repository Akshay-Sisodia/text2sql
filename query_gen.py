import streamlit as st
import ollama

class SQLQueryGenerator:
    """
    Generates SQL queries using an LLM.
    """
    @staticmethod
    def generate_sql_query(user_task, metadata, model='llama3.2:1b'):
        """
        Use Ollama to generate an SQL query based on user task and database metadata.
        
        :param user_task: Natural language task description
        :param metadata: Database metadata
        :param model: Ollama model to use
        :return: Generated SQL query
        """
        # Prepare a prompt with database schema information
        schema_description = "\nDatabase Schema:\n"
        for table, columns in metadata.items():
            schema_description += f"Table: {table}\n"
            schema_description += "Columns:\n"
            for col in columns:
                schema_description += f"  - {col['name']} ({col['type']}{', Primary Key' if col['is_primary_key'] else ''})\n"
        
        # Combine task with schema description
        full_prompt = f"""
You are an expert SQL query generator. Given the following database schema and user task, 
generate ONLY the SQL query to accomplish the task. Do not include any explanations or additional text.
The SQL query must be for SQLite3.

{schema_description}

User Task: {user_task}

SQL Query:"""
        
        try:
            # Generate SQL query using Ollama
            response = ollama.chat(
                model=model,
                messages=[
                    {
                        'role': 'system', 
                        'content': 'You are an expert SQL query generator.'
                    },
                    {
                        'role': 'user', 
                        'content': full_prompt
                    }
                ]
            )
            
            # Extract the SQL query from the response
            sql_query = response['message']['content'].strip().rstrip(';') + ';'
            return sql_query
        except Exception as e:
            st.error(f"Error generating SQL query: {e}")
            return None