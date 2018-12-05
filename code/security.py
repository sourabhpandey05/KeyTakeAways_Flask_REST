from werkzeug.security import safe_str_cmp
from user import User

users =[

	# {
	# 	'id':1,
	# 	'username':'bob',
	# 	'passowrd':'asdf'
	# }

	User(1,'bob','asdf')
]

username_mapping = { u.username:u for u in users }
# 'bob':
# 	{
# 		'id':1,
# 		'username':'bob',
# 		'passowrd':'asdf'
# 	}
		


userid_mapping={u.id : u for u in users }

# 1: 

# 	{
# 		'id':1,
# 		'username':'bob',
# 		'passowrd':'asdf'
# 	}

	

def authenticate(username,password):
	#user = username_mapping.get(username , None)
	user = User.find_by_username(username)
	if user and safe_str_cmp(user.password,password):
		return user

def identity(payload):
	user_id = payload['identity']
	#return userid_mapping.get(user_id, None)
	return User.find_by_userId(user_id)


