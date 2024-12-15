import sqlite3
import streamlit as st

class DatabaseManager:
    """
    Manages database connection and metadata retrieval.
    """
    def __init__(self, db_path=None):
        """
        Initialize DatabaseManager with optional database path.
        
        :param db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        self.conn = None
        self.cursor = None
    
    def connect_to_database(self, db_path=None):
        """
        Establish a connection to the SQLite database.
        
        :param db_path: Optional path to override the current database path
        :return: Tuple of (connection, cursor) or (None, None) if connection fails
        """
        if db_path:
            self.db_path = db_path
        
        if not self.db_path:
            st.error("No database path provided.")
            return None, None
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            return conn, cursor
        except sqlite3.Error as e:
            st.error(f"Error connecting to database: {e}")
            return None, None
    
    def get_database_metadata(self):
        """
        Retrieve metadata about the database schema.
        
        :return: Dictionary containing table names and their column information
        """
        conn, cursor = self.connect_to_database()
        if not conn or not cursor:
            return {}
        
        try:
            # Get all table names
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            
            # Collect metadata for each table
            metadata = {}
            for table in tables:
                table_name = table[0]
                cursor.execute(f"PRAGMA table_info({table_name});")
                columns = cursor.fetchall()
                
                # Create column metadata
                column_info = [
                    {
                        'name': col[1],
                        'type': col[2],
                        'is_primary_key': col[5] == 1
                    } for col in columns
                ]
                
                metadata[table_name] = column_info
            
            return metadata
        except sqlite3.Error as e:
            st.error(f"Error retrieving database metadata: {e}")
            return {}
        finally:
            if conn:
                conn.close()