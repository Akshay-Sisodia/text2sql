import sqlite3
import streamlit as st

class SQLQueryExecutor:
    """
    Executes SQL queries and manages results.
    """
    @staticmethod
    def clean_sql_query(sql_query):
        """
        Clean the SQL query by removing markdown code fences, extra backticks, 
        and trimming whitespace.
        
        :param sql_query: Raw SQL query string
        :return: Cleaned SQL query
        """
        # Remove markdown code fences and language specifiers
        cleaned_query = sql_query.replace('```sql', '').replace('```', '').strip()
        
        # Remove any extra backticks
        cleaned_query = cleaned_query.strip('`').strip()
        
        # Remove any trailing semicolons and whitespace
        cleaned_query = cleaned_query.rstrip(';').strip() + ';'
        
        return cleaned_query

    @staticmethod
    def execute_query(db_path, sql_query):
        """
        Execute the generated SQL query and return results.
        
        :param db_path: Path to the SQLite database
        :param sql_query: SQL query to execute
        :return: Query results
        """
        try:
            # Connect to the database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Clean the SQL query before execution
            cleaned_query = SQLQueryExecutor.clean_sql_query(sql_query)
            
            cursor.execute(cleaned_query)
            columns = [column[0] for column in cursor.description]
            results = cursor.fetchall()
            conn.close()
            return columns, results
        except sqlite3.Error as e:
            st.error(f"Error executing query: {e}")
            return None, None
        except Exception as e:
            st.error(f"Unexpected error: {e}")
            return None, None