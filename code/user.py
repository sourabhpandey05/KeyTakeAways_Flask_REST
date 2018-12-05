import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required



class User:
	def __init__(self,_id,username,password):
		self.id = _id
		self.username=username
		self.password= password

	@classmethod
	def find_by_username(cls,username):
		connection = sqlite3.connect("data.db") 
		cursor = connection.cursor()
		select_query_result = "SELECT * FROm users where username=?"
		result  = cursor.execute(select_query_result,(username,))
		row = result.fetchone()


		if row:
			user = cls(*row)
		#   user = User(row[0],row[1],row[2])

		else :
			user = None

		connection.close()
		return user

	@classmethod
	def find_by_userId(cls,_id):
		connection = sqlite3.connect("data.db") 
		cursor = connection.cursor()
		select_query_result = "SELECT * FROm users where id=?"
		result  = cursor.execute(select_query_result,(_id,))
		row = result.fetchone()

		if row:
			user = cls(*row)
			#user = User(row[0],row[1],row[2])

		else :
			user = None	

		connection.close()
		return user	

class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('username',
			type=str,
			required =True,
			help= "This field cannot be left blank!"			

			)
	parser.add_argument('password',
			type=str,
			required =True,
			help= "This field cannot be left blank!"

			)


	def post(self):

		data = UserRegister.parser.parse_args()

		if User.find_by_username(data['username']) != None:
			return {"message" :" User already exists"}, 400
		else:
			connection = sqlite3.connect("data.db") 
			cursor = connection.cursor()
			insert_query = "INSERT INTO users VALUES(NULL,?,?)"
			cursor.execute(insert_query,(data['username'],data['password']))
			connection.commit()
			connection.close()
			return {"message" :" User created successfully."}, 201


class UserLogin(Resource):
	
	
	def post(self):

		parser = reqparse.RequestParser()
		parser.add_argument('username',
			type=str,
			required =True,
			help= "This field cannot be left blank!"
			)
		parser.add_argument('password',
			type=str,
			required =True,
			help= "This field cannot be left blank!"
			)
		data = parser.parse_args()



		# for item in items:
		# 	if item['name'] == name:
		# 		return item
		# return {'item' : None}, 404

		user = User.find_by_username(data['username'])

		if user:
			if data['password'] == user.password:
				return {'message': 'Logged in as {}'.format(user.username)}
			else:
				return {'message': 'Wrong credentials'}

		return {'message':'user not found'},404

class IdeaList(Resource):
	def get(self):
		return {'ideas' :"Do coding with Flask and Android"}

   
    
    









		

