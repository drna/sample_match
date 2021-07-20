import numpy
import pandas as pd
import sys

HOST_NAME = "localhost"
USER_NAME = "postgres"
USER_PASSWORD = "admin"


class AnalysisManager:  

    def __init__(self, save_name):
        self.save_name = save_name
    
    def connect_to_db(self):
        self.connection = self.create_server_connection(HOST_NAME, USER_NAME, USER_PASSWORD)
        print(self.connection)  
        pass

    def load_new_data(self, new_data_filepath):
        
        pass

    def create_save(self):
        
        self.connection = self.create_server_connection(HOST_NAME, USER_NAME, USER_PASSWORD)

        cursor = self.connection.cursor()
        try:
            cursor.execute("CREATE DATABASE " + self.save_name)
            print("Database created successfully")
        except Error as err:
            print(f"Error: '{err}'")
            sys.exit(1)
        
        self.db_connection = self.create_db_connection(HOST_NAME, USER_NAME, USER_PASSWORD, self.save_name)
        self.execute_query(self.db_connection, "") 

    
    def list_save_names(self):
        self.connect_to_db()
        pass
    
    def output_metrics(self):
        
        pass
    
    def output_matches(self):
        
        pass
