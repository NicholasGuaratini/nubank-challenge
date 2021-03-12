import json
from DataBase import dbConnection

class Account:
	def __init__(self,account):
		self.activeCard = account['active-card']
		self.availableLimit = account['available-limit']
	
	def data_json():
		users_list = []

		with open('Desktop/nubank-challenge/File/Accounts.json', 'r') as json_file:
			user_data = json.loads(json_file.read())
			for u in user_data ['active-card']['available-limit']:
				users_list.append(Account(**u))

		return users_list

print ('Welcome')

dados = Account.data_json()

print (dados)

print ('Imported json!')

dtBase = dbConnection.create_connection()
conn = dtBase

table = dbConnection.create_table(conn)
# insert = dbConnection.insert_register(conn, dados.activeCard, dados.availableLimit)
select = dbConnection.select_register(conn)
print(select)

# if __name__ == '__main__':
#     main()