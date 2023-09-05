import psycopg2

Connection = None
Cursor =  None
try: 
    Connection = psycopg2.connect(
        dbname = 'PsycoPg' ,
        user = 'postgres' , 
        password = 'nssh@4707' , 
        host = 'localhost' , 
        port = 4707   
    )
        
        
    Cursor = Connection.cursor()
    
    Create_Script = '''
        CREATE TABLE IF NOT EXISTS CUSTOMUSERS (
            id          int PRIMARY KEY , 
            name        varchar(30) , 
            username    varchar(30),  
            email       varchar(30)        
        )
    '''
    Cursor.execute(Create_Script)
    
    Insert_Script = ' INSERT INTO CUSTOMUSERS ( id , name , username , email ) VALUES ( %s , %s , %s , %s ) '
    Insert_Values = [ ( 1 , 'nitin' , 'sharmanitin' , 'nssh@gamil.com' ) , 
                      ( 2 , 'chandan' , 'sharmachandan' , 'cssh@gmail.com' ) , 
                      ( 3 , 'rohit' , 'sharmarohit' , 'rssh@gamil.com' ) , 
                      ( 4 , 'lavish' , 'sharmalavish' , 'lavi@gamil.com' ) , 
                      ( 5 , 'ankit' , 'sharmaankit' , 'anki@gamil.com ' ) ]
    
    for Record in Insert_Values:
        Cursor.execute(Insert_Script , Record)
        
    Cursor.execute( 'SELECT * FROM CUSTOMUSERS' )
    for Data in Cursor.fetchall():
        print(Data)
        
        
        
    
        
    
except Exception as Error:
    print(Error)

finally:
    if Connection is not None:
        Connection.close()
    if Cursor is not None:
        Cursor.close()
    
    

    