#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pymongo
from pymongo import MongoClient


if __name__ == "__main__":
	connection = MongoClient()

	db = connection.students.ctec121

		# create dictionary
	student_record = {}

	# set flag variable
	flag = True

	# loop for data input
	#while (flag):
	   # ask for input
	student_name = "holapaco"
	student_grade = "primero"
	   # place values in dictionary
	student_record = {'name':student_name,'grade':student_grade}
	   # insert the record
	db.insert(student_record)
	   # should we continue?
	    #flag = input('Enter another record? ')
	   #if (flag[0].upper() == 'N'):
	   #   flag = False

	# find all documents
	results = db.find({'name':"holapaco"})

	print()
	print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

	# display documents from collection
	for record in results:
	# print out the document
		print(record['name'] + ',',record['grade'])
		print()
		print type(record['name'])
		print type(str(record['name']))
		print str(record['name'])

	# close the connection to MongoDB
	connection.close()