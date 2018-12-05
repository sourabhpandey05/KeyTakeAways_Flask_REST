import sqlite3
import json
from flask_jwt import jwt_required
from flask_restful import reqparse,Resource
from flask import jsonify


class KeyTakeaways:
	def __init__(self,_id,Keylearning,userid,bookid):
		self.id = _id
		self.Keylearning=Keylearning
		self.userid = userid
		self.bookid = bookid



class Takeaways(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('Keylearning',
			type=str,
			required =True,
			help= "This field cannot be left blank!"
			)
	

	parser.add_argument('userid',
			type=int,
			required =True,
			help= "This field cannot be left blank!"
			)

	parser.add_argument('bookid',
			type=int,
			required =True,
			help= "This field cannot be left blank!"
			)


	def post(self):

		data = Takeaways.parser.parse_args()


		#if Book.find_by_name(data['title']):
		
		# for item in items:   # if next(filter(lambda x: x['name']==name,items),None)
		# 	if item['name'] == name:
				#return {'message' : "A book with title '{}' already exists".format(data['title']) }, 400

		#data = request.get_json()	
	
		takeaways = {'Keylearning':data['Keylearning'],'userid':data['userid'],'bookid':data['bookid']}
		#items.append(item)
		connection = sqlite3.connect("data.db") 
		cursor = connection.cursor()
		query = "insert into TakeAways values(NULL,?,?,?)"

		cursor.execute(query,(data['Keylearning'],data['userid'],data['bookid']))

		connection.commit()
		connection.close()



		return takeaways, 201

	def get(self):
		takeaways = []
		connection = sqlite3.connect("data.db") 
		cursor = connection.cursor()
		select_query_result = "SELECT * FROM TakeAways"
		result  = cursor.execute(select_query_result)
		row = result.fetchall()
		for key in row:
				takeaways.append({'id':key[0],'Keylearning':key[1],'userid':key[2], 'bookid':key[3]})
		connection.close()

		if row:
			print(json.dumps({'Takeaways':takeaways}))
			return jsonify({'Takeaways':takeaways})	