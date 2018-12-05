from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT

from security import authenticate,identity
from user import UserRegister,IdeaList,UserLogin
from booklist import BookList
from takeaways import Takeaways

#from item import Item,ItemList

app = Flask(__name__)
app.secret_key = 'sourabh'

api = Api(app)

jwt = JWT(app, authenticate,identity)    #/auth

#items = []


class Student(Resource):
	def get(self,name):
		return{'student': name}


api.add_resource(Student,'/student/<string:name>')




api.add_resource(UserLogin,'/login')
api.add_resource(IdeaList, '/ideas')

api.add_resource(UserRegister, '/register')

api.add_resource(BookList, '/book')

api.add_resource(Takeaways,'/takeaways')
		
if __name__ == '__main__':
	app.run(host="127.0.0.1", port=5000, debug =True)	