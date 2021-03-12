#import json

class Account:
	def __init__(self):
		pass
		# self.activeCard = activeCard
		# self.availableLimit = availableLimit
		# self.isActive = True
	
	def get_activeCard(self):
		return self.activeCard
	
	def set_activeCard(self):
		return self.activeCard

	def get_avaibleLimit(self):
		return self.availableLimit

	def set_avaibleLimit(self):
		return self.availableLimit

	def get_violations(self):
		if self.isActive == True:
			print ("account-already-initialized")

		#print (accountCard, availableLimit)
#		print(json.dumps(accountCard, availableLimit, indent = 4, sort_keys=True))

