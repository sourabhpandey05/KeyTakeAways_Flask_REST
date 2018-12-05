import sqlite3
import json
from flask_jwt import jwt_required
from flask_restful import reqparse,Resource
from flask import jsonify



class Book:
	def __init__(self,_id,title,author,publication,tag,userid):
		self.id = _id
		self.title=title
		self.author= author
		self.publication = publication
		self.tag = tag
		self.userid = userid

	

	@classmethod
	def find_by_name(cls,title):
		connection = sqlite3.connect("data.db") 
		cursor = connection.cursor()
		select_query_result = "SELECT * FROM BookList where title=?"
		result  = cursor.execute(select_query_result,(title,))
		row = result.fetchone()

		if row:

			book = cls(*row)

		else:
			book = None	

		connection.close()

		return book


class BookList(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('title',
			type=str,
			required =True,
			help= "This field cannot be left blank!"
			)
	parser.add_argument('author',
			type=str,
			required =True,
			help= "This field cannot be left blank!"
			)
	parser.add_argument('publication',
			type=str,
			required =True,
			help= "This field cannot be left blank!"
			)
	parser.add_argument('tag',
			type=str,
			required =True,
			help= "This field cannot be left blank!"
			)

	parser.add_argument('userid',
			type=int,
			required =True,
			help= "This field cannot be left blank!"
			)
	


		
	def post(self):

		data = BookList.parser.parse_args()


		if Book.find_by_name(data['title']):
		
		# for item in items:   # if next(filter(lambda x: x['name']==name,items),None)
		# 	if item['name'] == name:
				return {'message' : "A book with title '{}' already exists".format(data['title']) }, 400

		#data = request.get_json()	
	
		book = {'title':data['title'], 'author': data['author'],'publication':data['publication'],'tag':data['tag'], 'userid':data['userid']}
		#items.append(item)
		connection = sqlite3.connect("data.db") 
		cursor = connection.cursor()
		query = "insert into BookList values(NULL,?,?,?,?,?)"

		cursor.execute(query,(data['title'], data['author'],data['publication'],data['tag'],data['userid']))

		connection.commit()
		connection.close()



		return book, 201

	def delete(self,name):
		global items
		items = list(filter(lambda x:x['name']!=name,items))
		return {'message': "An item with name '{}' is deleted".format(name)}

	def put(self,name):
		#data = request.get_json()
		data = Item.parser.parse_args()

		item = next(filter(lambda x: x['name']==name,items),None)

		if(item==None):
			item = {'name':name, 'price': data['price']}
			items.append(item)
		else:
			item.update(data)

		return item

	def get(self):
		booklist = []
		connection = sqlite3.connect("data.db") 
		cursor = connection.cursor()
		select_query_result = "SELECT * FROM BookList"
		result  = cursor.execute(select_query_result)
		row = result.fetchall()
		for book in row:
				booklist.append({'id':book[0],'title':book[1], 'author':book[2],'publication':book[3],'tag':book[4], 'userid':book[5]})
		connection.close()

		if row:
			print(json.dumps({'book':booklist}))
			return jsonify({'book':booklist})



class ItemList(Resource):
	def get(self):
		return {'items' :items}