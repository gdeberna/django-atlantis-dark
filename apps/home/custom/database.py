import mariadb
import sys

#connessione al db
def db_connect ():
    """Function to connect to sPYCY database"""
    # provo la connessione al DB
    try:
        conn = mariadb.connect(
        user="spycy",
        password="spycy!",
        host="127.0.0.1",
        port=3306,
        database="spycy")
        return conn
        
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
        
#disconnessione dal db
def db_disconnect (conn):
    """Function to disconnect from database"""
    try:
        conn.close()
    
    except mariadb.Error as e:
        print(f"Error disconnecting to MariaDB Platform: {e}")
        sys.exit(1)
        
def db_get (what, fromm, where, val, conn):
    """Function to retrive info from database"""
    try:
        query= "SELECT "+what+" FROM "+fromm+" WHERE "+where+"=?"
        data=(val,)
        cursor= conn.cursor()
        cursor.execute(query, data)
        result = cursor.fetchone()
        return result[0]
    
    except mariadb.Error as e:
        print(f"Error quering MariaDB Platform: {e}")
        sys.exit(1)

def db_getdict (index, what, fromm, conn):
    """Function to map db info in a dictionary"""
    try:
        query= "SELECT "+index+" ,"+what+" FROM "+fromm
        cursor= conn.cursor(dictionary=True)
        cursor.execute(query)
        rows = cursor.fetchall()   
        dic = {x[index]:x[what] for x in rows}
        return dic
    
    except mariadb.Error as e:
        print(f"Error quering MariaDB Platform: {e}")
        sys.exit(1)

def db_getlist (what, fromm, conn):
    """Function to map db info in a list"""
    try:
        query= "SELECT "+what+" FROM "+fromm
        cursor= conn.cursor()
        cursor.execute(query)
        array = list(cursor.fetchall())  
        return array
    
    except mariadb.Error as e:
        print(f"Error quering MariaDB Platform: {e}")
        sys.exit(1)

def db_insert (table, col, val, conn):
    """Function to insert in table with multiple values"""
    cols=""
    for i in col:
        if cols =="":
            cols = i
        else:
          cols=cols+","+ i
      
    vals=""
    for i in val:
        if vals =="":
            vals = "'"+i+"'"
        else:
          vals=vals+",'"+i+"'"
      
    try:
       query= "INSERT INTO "+table+" ("+cols+") VALUES ("+vals+")" 
       #print (query)
       cursor= conn.cursor()
       cursor.execute(query)
       conn.commit()
       print ("Data inserted in"+table)
       
    except mariadb.Error as e:
        print(f"Error quering MariaDB Platform: {e}")
        sys.exit(1)
 
def db_create_prj_quest(prjName, conn):
    tabName=prjName+"_quest"     
    try:
        query= "CREATE TABLE "+tabName+""" (
        id INT(11) NOT NULL AUTO_INCREMENT,
        area VARCHAR(100) NOT NULL COLLATE 'utf8mb4_general_ci',
        question LONGTEXT NOT NULL COLLATE 'utf8mb4_general_ci',
        note LONGTEXT NOT NULL COLLATE 'utf8mb4_general_ci',
        answer LONGTEXT NOT NULL COLLATE 'utf8mb4_general_ci',
        typology VARCHAR(20) NOT NULL COLLATE 'utf8mb4_general_ci',
        applicable VARCHAR(20) NOT NULL COLLATE 'utf8mb4_general_ci',
        PRIMARY KEY (id) USING BTREE)"""
        cursor= conn.cursor()
        cursor.execute(query)
        #populate the table with all questionnarire questions
        cursor2=conn.cursor()
        query2="INSERT INTO "+tabName+" (area, question, note, typology) SELECT area, question, note, typology FROM home_questionnaire"
        cursor2.execute(query2)  
        return None
        
    except mariadb.Error as e:
        print(f"Error quering MariaDB Platform: {e}")
        sys.exit(1)
 
  
def db_create_prj_timeline(prjName, pub_date, conn):
    tabName=prjName+"_timeline"
    try:
       query= "CREATE TABLE "+tabName+""" (
       id INT(11) NOT NULL AUTO_INCREMENT,
       milestone_date DATE NOT NULL,
       description LONGTEXT NOT NULL COLLATE 'utf8mb4_general_ci',
       PRIMARY KEY (id) USING BTREE)"""
       cursor= conn.cursor()
       cursor.execute(query)
       #populate the table with a kickstart milestone on the timeline
       cursor2=conn.cursor()
       query2="INSERT INTO "+tabName+" (milestone_date, description) SELECT DATE('"+pub_date+"'), 'Project publishing date'" 
       cursor2.execute(query2) 
       
       return None
    
    except mariadb.Error as e:
        print(f"Error quering MariaDB Platform: {e}")
        sys.exit(1)
