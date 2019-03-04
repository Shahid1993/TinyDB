from tinyDB import TinyDB

db = TinyDB('./tinydb.db')

#db.set('name', 'Shahid')

#print(db.get('name'))
#

# test = {
# 		'name' : 'Shahid',
# 		'company' : 'Codemantra',
# 		'languages' : ['java', 'C', 'Python']
# 	}

print(db.get('profile'))
print(db.get('profile.languages'))
print(db.get('profile.languages.test'))