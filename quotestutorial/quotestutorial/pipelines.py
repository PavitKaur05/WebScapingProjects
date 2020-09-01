# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#Extracted Data->Temp Containers-> json/xml/csv
#Extracted Data->Temp Containers->Pipelines->Database
from itemadapter import ItemAdapter
import sqlite3
# import pymongo

# #MongoDB Code
# class QuotestutorialPipeline:

#     def __init__(self):
#         self.conn=pymongo.MongoClient('localhost',27017)
#         db=self.conn['quotes_db']
#         self.collection=db['Quotes'] # Table


#     def process_item(self,item,spider):
#         self.collection.insert((dict(item)))
#         return item


#Sqlite3 Database code
class QuotestutorialPipeline:

    def __init__(self):
        self.create_connection()
        self.create_tb()

    def create_connection(self):
        self.conn=sqlite3.connect('quotes.db')
        self.curr=self.conn.cursor()

    def create_tb(self):
        self.curr.execute("""DROP TABLE IF EXISTS Quotes""")
        self.curr.execute("""CREATE TABLE Quotes
                            (title text,
                            author text,
                            tags text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline "+item['title'][0])
        return item

    def store_db(self,item):
        self.curr.execute("""INSERT INTO Quotes VALUES(?,?,?)""",(item['title'][0],item['author'][0],item['tags'][0]))
        self.conn.commit()
