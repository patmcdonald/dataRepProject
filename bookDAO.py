import mysql.connector

class BookDAO:
# localhost credentials
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host = ["localhost"],
        user = ["root"],
        password = ["rootuser"],
        database = ["datarep"]
        )

    def createTable(self):
        cursor = self.db.cursor()
        sql="CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), year INT)"
        cursor.execute(sql)
        self.db.commit()
        print("Table Created")


    def populateTable(self):
        books=[
            {"Title":"Dune", "Author":"Frank Herbert", "Year": 1965},
            {"Title":"The Alchemist", "Author":"Paulo Coelho", "Year": 1988},
            {"Title":"Deep Work ", "Author":"Cal Newport", "Year": 2016}
        ]

        cursor = self.db.cursor()
        cursor.executemany("insert into books (title, author, year) values (%(Title)s,%(Author)s,%(Year)s)", books)
        self.db.commit()
      
    
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into book (title,author, price) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from book"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from book where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update book set title= %s,author=%s, price=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from book where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','Title','Author', "Price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
bookDAO = BookDAO()