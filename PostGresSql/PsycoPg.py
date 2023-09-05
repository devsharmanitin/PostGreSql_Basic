import psycopg2
# if Data Should be in Dictionary format 
import psycopg2.extras


Connection = None
Cursor = None
try:
    # Connecting Database PostGresql
    Connection = psycopg2.connect(
        dbname =  'PsycoPg' , 
        user = 'postgres' ,
        password = 'nssh@4707' ,
        host = 'localhost' ,
        port = 4707
    )
    
    # Connect Using Context Manager 
    # with psycopg2.connect(
    #     dbname =  'PsycoPg' , 
    #     user = 'postgres' ,
    #     password = 'nssh@4707' ,
    #     host = 'localhost' ,
    #     port = 4707
    # ) as Connection:
    #     with Connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as Cursor:
            # Change Intendiation under Backtes 
    
    # Creating Cursor to Execute Commands 
    # Cursor = Connection.cursor()
    
    #Connection Cursor With Data in Dict Format 
    Cursor = Connection.cursor(cursor_factory=psycopg2.extras.DictCursor)  #Now We get Data In Dict Format 

    # Deleting the Table IF Exists 
    Cursor.execute( 'DROP TABLE IF EXISTS Employee' )

    # Create Employee Table 
    Create_Script =  ''' 
        CREATE TABLE IF NOT EXISTS Employee (
            id      int PRIMARY KEY , 
            name    varchar(30) NOT NULL    ,
            salary  int ,
            dept_id varchar(10) 
        )
       '''
    # Execute Commands Information 
    Cursor.execute(Create_Script)
    
    Insert_Script = ' INSERT INTO Employee ( id , name , salary , dept_id ) VALUES ( %s , %s , %s , %s ) '
    # Insert A Single Value to Table 
    
    # Insert_Value = ( 1 , 'Nitin'  , 15000 , 'D1' )
    # Cursor.execute(Insert_Script , Insert_Values)
    
    # Inserting Multiple Values/List Of Values 
    Insert_Values = [ ( 1 , 'Nitin' , 15000 , 'D1' ) , ( 2 , 'Rohit'  , 12000 , 'D2' ) , ( 3 , 'Lavish'  , 18000 , 'D3' ) ]
    for Data in Insert_Values:
        Cursor.execute(Insert_Script , Data)
        
       
    # Updating The Data 
    Update_Script = ' UPDATE Employee SET salary = salary + (salary * 0.5 ) '
    Cursor.execute(Update_Script) 
       
       
       
    # Deleting Specific User From Table 
    Delete_Script = ' DELETE FROM Employee WHERE name = %s '
    Delete_Value = ('Rohit',)
    Cursor.execute(Delete_Script , Delete_Value)
        
    # Fetching Data From Table 
    Cursor.execute( 'SELECT * FROM Employee' )
    # print(Cursor.fetchall())
    
    # Data With Loop 
    for Data in Cursor.fetchall():
        # Fetch Data With Single item
        print(Data) 
        #Fetch Data With Its Indexing of column item 
        print(Data[1] , Data[2]) 
        
        # Now We Get Data By mentioning Column Name From Table 
        print(Data['name'] , Data['salary'])  
        
        
    # Getting One Data 
    Update_Script_One =  'SELECT DISTINCT name , salary , dept_id FROM Employee WHERE name = %s' 
    Update_Script_Value = ('Nitin',) 
    Cursor.execute(Update_Script_One , Update_Script_Value)
    print(Cursor.fetchone() , "Fetch One Data")  
    
    
    # Commenting Values to Databse 
    Connection.commit()
    
except Exception as Error:
    print(Error)
    
finally:
    # Checking If Connection is Open Or Not 
    if Connection is not None:  
        # Closing Connection   
        Connection.close()
    if Cursor is not None:
        Cursor.close()
