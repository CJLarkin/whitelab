import sqlite3
from sqlite3 import OperationalError
import sys

def db_edit(smiles, tt, tm, vis, frag, cit):
	conn = sqlite3.connect('GLC.db')
	c = conn.cursor()
	#conn.execute("CREATE TABLE GLC(SMILES, TT INT, TM INT, Viscocity INT, Fragility INT, Citation INT)")
	#conn.execute("alter table GLC add column SMILES, TT, TM, Viscocity, Fragility, Citation")
	statement = "INSERT INTO GLC (SMILES, TT, TM, Viscocity, Fragility, Citation) VALUES ('{0}',{1},{2},{3},{4},{5})".format(smiles, tt, tm, vis, frag, cit)
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
	#c.execute("SELECT * FROM GLC;")
	#return (c.fetchall())
	if query == "":
		return {"new": False}
	else:
		c.execute("SELECT * FROM GLC WHERE SMILES=?", (query,))
		all_rows = c.fetchall()
		try:
			json_dic = {"smiles": all_rows[0][0].encode("ascii"), "tt": all_rows[0][1], "tm": all_rows[0][2], "vis": all_rows[0][3], "frag": all_rows[0][4], "cit": all_rows[0][5]}
			return json_dic
		except IndexError:
			return {"string": query, "new": True}

def db_update(smiles, tt, tm, vis, frag, cit):
	conn = sqlite3.connect('GLC.db')
	c = conn.cursor()
	c.execute("UPDATE GLC SET TT=? WHERE SMILES=?", (tt,smiles))
	c.execute("UPDATE GLC SET TM=? WHERE SMILES=?", (tm,smiles))
	c.execute("UPDATE GLC SET Viscocity=? WHERE SMILES=?", (vis,smiles))
	c.execute("UPDATE GLC SET Fragility=? WHERE SMILES=?", (frag,smiles))
	c.execute("UPDATE GLC SET Citation=? WHERE SMILES=?", (cit,smiles))
	conn.commit()
	conn.close()

if __name__ == "__main__":
    #db_edit(smiles, tt, tm, vis, frag, cit)
    db_search(sys.argv[1])