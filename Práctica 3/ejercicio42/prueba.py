#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pymongo
from pymongo import MongoClient


if __name__ == "__main__":
	client = MongoClient()
	db = client.probando
	post = {"author": "Mike",
		"text": "My first blog post!",
		"tags": ["mongodb", "python", "pymongo"],
		"date": 11}
	posts = db.posts
	post_id = posts.insert(post)
	posts.find_one({"author": "Mike"})
	print  posts.count()