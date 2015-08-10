import sqlite3
from sqlite3 import OperationalError
import sys

columns = ['SMILES', 'TT', 'TM', 'Viscosity', 'Fragility', 'Citation']

def db_edit(**args):
	conn = sqlite3.connect('GLC.db')
	c = conn.cursor()
	#conn.execute("CREATE TABLE GLC(SMILES, TT INT, TM INT, Viscosity INT, Fragility INT, Citation INT)")
	#conn.execute("alter table GLC add column SMILES, TT, TM, Viscosity, Fragility, Citation")
	statement = "INSERT INTO GLC (" + reduce(lambda x,y: x + ', ' + y, columns) + ") VALUES (" + str([(args[ci]).encode("ascii") for ci in columns]).replace("[","").replace("]","")  + ")"
	try:
		c.execute(statement)
	except OperationalError as e:
		print e
		return None
	conn.commit()
	conn.close()
	return "hola"

def db_search(query):
	conn = sqlite3.connect('GLC.db')
	c = conn.cursor()
	if query == "":
		return {"new": False}
	else:
		c.execute("SELECT * FROM GLC WHERE " + columns[0] + "=" + "'{}'".format(query))
		all_rows = c.fetchall()
		try:
			json_dic = {}
			length = int(len(columns))
			for i in range(length):
				json_dic[columns[i]] = all_rows[0][i]
			#json_dic = {"{}".format(columns[i]): all_rows[0][i].encode("ascii"), "{}".format(columns[0]): all_rows[0][1], "TM": all_rows[0][2], "Viscosity": all_rows[0][3], "Fragility": all_rows[0][4], "Citation": all_rows[0][5]}
			return json_dic
		except IndexError:
			return {"string": query, "new": True}

def db_update(**args):
	conn = sqlite3.connect('GLC.db')
	c = conn.cursor()
	statement = "UPDATE GLC SET"
	for k,v in args.iteritems():
		if k != "SMILES":
			statement += " {} = {},".format(k,v)
	c.execute(statement[:-1] + " WHERE " + str(columns[0]) + "=" + "'{}'".format(str(args[columns[0]])))
	conn.commit()
	conn.close()

if __name__ == "__main__":
    #db_edit(smiles, tt, tm, vis, frag, cit)
    db_search(sys.argv[1])


