import json
from DataBase import dbConnection
from Entities import CreateAccount

print ('Welcome')

print ('Creating memory database...')

print ('Reading JSON file...')

with open('Desktop/NuBank_Challenge/File/Accounts.json') as file:
  data = json.load(file)

print(json.dumps(data, indent = 4, sort_keys=True))
print ('Imported json!')

activeCard = None
availableLimit = None
acc = CreateAccount.Account()

for item in data:
    for data_item in item['account']:
    	activeCard = acc.set_activeCard(data_item['active-card']), 
    	availableLimit = acc.set_activeCard(data_item['available-limit'])

print(activeCard)
print(availableLimit)

dtBase = dbConnection.create_connection()
conn = dtBase

table = dbConnection.create_table(conn)
insert = dbConnection.insert_register(conn, activeCard, availableLimit)
select = dbConnection.select_register(conn)
print(select)

# if __name__ == '__main__':
#     main()