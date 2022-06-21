
import sqlite3 as sql


class DataBase_Connection():
    def __init__(self):
        print('Database Connected!')



    def totaldiseases(self):
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute('''select * from ILLNESS ''')
            row = cursor.fetchall()
            return str(len(row))            
        except Exception as e:
            print(e)

    def totalusers(self):    
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute('''select * from USERS''')
            row = cursor.fetchall()
            return str(len(row))
        except Exception as e:
            print(e)


    def numberdoctors(self):
        try:
            conn = sql.connect('IDMS.db')   
            cursor = conn.cursor()
            cursor.execute('''select DISTINCT Doctorname from DEPARTMENT''')
            row = cursor.fetchall()
            return str(len(row))
        except Exception as e:
            print(e)

    def totalhospital(self):    
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute('''select * from HOSPITAL''')
            row = cursor.fetchall()
            return str(len(row))
        except Exception as e:
            print(e)

    def totalsearchhistory(self):
      
        try:
            conn = sql.connect('IDMS.db')  
            cursor = conn.cursor()
            cursor.execute('''select * from PATIENTHISTORY''')
            row = cursor.fetchall()
            return str(len(row))
        except Exception as e:
            print(e)
