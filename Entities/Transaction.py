class Transaction:
	def __init__(self, merchant, amount, time): 
		self.merchant = merchant
		self.amount = amount
		self.time = time
		self.transactions = []