import psycopg2
from psycopg2 import Error

class DataOps:
    def __init__(self) -> None:
        try:
            self.conn = conn = psycopg2.connect(database = "testdb", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")
            self.cursor = self.conn.cursor()
        except Error as err:
            raise "An Error occured while connecting to database - {}".format(err)

    def Create_Users_Table(self,commit = False):

        CREATE_USERS_TABLE = (
        """CREATE TABLE IF NOT EXISTS users  
         (id SERIAL PRIMARY KEY NOT NULL,           
        firstname TEXT NOT NULL,                    
        lastname TEXT NOT NULL,                     
        other_names TEXT,                           
        password TEXT NOT NULL,                     
        date_created DATE NOT NULL;""")

        try:
            self.cursor.execute(CREATE_USERS_TABLE)
            if commit is True:
                self.conn.commit()
            return {"status": True,"content":"Users Table Successfully created"}

        except Error as err:
            return {"status": False, "detail":f"Could not create user table | Error Message - {err}"}


    def Insert_Users(self,columns:tuple,values:tuple,commit = False):
        
        try:
            id = self.cur.execute(f"INSERT INTO users {columns} VALUES {values} RETURNING id;")
            assert id is not None
            if commit is True:
                self.conn.commit()
            
            return {"status":True,"content":id}

        except Error as err:
            return {"status":False,"detail":"An error occured during insertion - {}".format(err)}
        except AssertionError as ass_error:
            return {"status":False,"detail":f"Insertion did not return any id | Error Messsage - {ass_error}"}


    def SelectOne(self,detail,table,columns = "*",by = "id"):
        try:
            response = self.cur.execute(f"SELECT columns FROM {table} where {by} = {detail}")
            if response:
                return {"status":True,"content": response}
        except Error:
            return {"status": False, "detail":f"Execution Failed | Error Message - {err}"}


    def ExecuteSql(self,query_string:str):
        try:
            response = self.cursor.execute(query_string)
        except Error as err:
            return {"status": False, "detail":f"Execution Failed | Error Message - {err}"}

        return {"status": True, "content":response}

    def close_connection(self,func):

        def wrapper(*args,**kwargs):
            response = func(*args,**kwargs)
            if (self.conn):
                self.cursor.close()
                self.conn.close()
                print("PostgreSQL connection is closed")
            return response

        return wrapper