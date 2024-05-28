auths = [
	{'username': 'sdelquin', 'password': '1234'},
	{'email': 'sdelquin@gmail.com', 'token': '4321'},
	{'email': 'test@test.com', 'password': 'ABCD'},
	{'username': 'sdelquin', 'password': '1234'}
]

for auth in auths:
	print(auth)
	match auth:
		case{'username': str(username), 'password': str(password)}:
			print('Authenticating with username and password')
			print(f'{username}: {password}')
		case{'email': str(email), 'token': str(token)}:
			print('Authenticating with email and token')
			print(f'{email}: {token}')
		case _:
			print('Authenticating methn not valid!')
	print('-----------')

