import sqlite3

conn = sqlite3.connect('db_files.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        file_Name TEXT\
        )")
    conn.commit()
conn.close()

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
list_str = []

for file in fileList:
    str=file.split('.')
    if str[1] == 'txt':
        str='.'.join(str)
        list_str.append(str)
print(list_str) 





        
conn = sqlite3.connect('db_files.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_Files(file_Name) VALUES (?)",\
                         (list_str[0],))
    cur.execute("INSERT INTO tbl_Files(file_Name) VALUES (?)",\
                         (list_str[1],))
    conn.commit()
conn.close()
      
      


conn = sqlite3.connect('db_files.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT file_Name FROM tbl_Files")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg ="File Name:{}\n ".format(item)
        print(msg)

    
