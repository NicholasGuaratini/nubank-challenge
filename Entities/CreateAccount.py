import json

class Account:
	def __init__(self,activeCard,availableLimit):
		self.activeCard = activeCard
		self.availableLimit = availableLimit
	
	def data_json():
		users_list = []

		with open('Desktop/nubank-challenge/File/Accounts.json', 'r') as json_file:
			user_data = json.loads(json_file.read())
			for u in user_data ['active-card']['available-limit']:
				users_list.append(Account(**u))

		print(users_list)

	# def get_activeCard(self):
	# 	return self.activeCard
	
	# def set_activeCard(self):
	# 	return self.activeCard

	# def get_avaibleLimit(self):
	# 	return self.availableLimit

	# def set_avaibleLimit(self):
	# 	return self.availableLimit

	# def get_violations(self):
	# 	if self.isActive == True:
	# 		print ("account-already-initialized")

		#print (accountCard, availableLimit)
#		print(json.dumps(accountCard, availableLimit, indent = 4, sort_keys=True))

