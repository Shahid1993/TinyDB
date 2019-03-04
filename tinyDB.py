import os
import json


class TinyDB(object):
	def __init__(self, loc):
		self.loc = os.path.expanduser(loc);
		self.load(self.loc);

	def load(self, loc):
		if(os.path.exists(loc)):
			self._load()
		else:
			self.db = {}

		return True

	def _load(self):
		self.db = json.load(open(self.loc, 'r'))

	def dumpdb(self):
		try:
			json.dump(self.db, open(self.loc, 'w+'))
			return True
		except:
			return False

	def set(self, key, value):
		try:
			self.db[str(key)] = value
			self.dumpdb()
		except Exception as e:
			print("[X] Error Saving Values to Database : "+ str(e))
			return False

	# def get(self, key):
	# 	try:
	# 		return self.db[str(key)]
	# 	except KeyError:
	# 		print("No Value Can Be Found for "+ str(key))
	# 		return False

	def get(self, key):
		try:
			obj = self.db
			tokens = key.split(".");
			for tok in tokens:
				if type(obj) != dict:
					raise KeyError()
				obj = obj[tok]
			return obj
		except KeyError:
			print("No Value Can Be Found for "+ str(key))

	def delete(self, key):
		if not key in self.db:
			return False;
		del self.db[key]
		self.dumpdb()
		return True

	def resetdb(self):
		self.db = {}
		self.dumpdb()
		return True




		