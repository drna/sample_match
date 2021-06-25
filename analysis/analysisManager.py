import numpy
import pandas as pd
import mysql.connector
from mysql.connector import Error

class AnalysisManager:  

    def __init__(self, save_file):
        self.save_file = save_file
    
    def connect_to_db(self):
        self.connection = self.create_server_connection("localhost", "root", "j-vm")
        print(self.connection)  
        pass

    def load_new_data(self, new_data_filepath):
        
        pass

    def create_save_file(self):
        
        self.connection = self.create_server_connection("localhost", "root", "j-vm")

        cursor = self.connection.cursor()
        try:
            cursor.execute("CREATE DATABASE " + self.save_file)
            print("Database created successfully")
        except Error as err:
            print(f"Error: '{err}'")
        pass
    
    def list_save_files(self):
        self.connect_to_db()
        pass
    
    def output_metrics(self):
        
        pass
    
    def output_matches(self):
        
        pass

    
    def create_server_connection(self, host_name, user_name, user_password):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password
            )
            print("Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return connection
