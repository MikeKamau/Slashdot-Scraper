# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

class SlashdotPipeline(object):
    host = '127.0.0.1'
    user = 'root'
    password = '$up3s1cr1t'
    db = 'slashdot'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        #return item
        sql = "INSERT INTO stories (title, comments) VAlUES (%s, %s)"
        values = (item['title'], item['comments'])
        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
        except:
            print("Error occured inserting data")
