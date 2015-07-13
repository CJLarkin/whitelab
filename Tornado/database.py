import sqlite3
import sys

def db_edit(smiles, tt, tm, vis, frag, cit, Abs):
	conn = sqlite3.connect('GLC.db')
	c = conn.cursor()

	#conn.execute("CREATE TABLE GLC(SMILES, TT INT, TM INT, Viscocity INT, Fragility INT, Citation INT, Abstract TEXT)")
	#conn.execute("alter table GLC add column SMILES, TT, TM, Viscocity, Fragility, Citation, Abstract")
	statement = "INSERT INTO GLC (SMILES, TT, TM, Viscocity, Fragility, Citation, Abstract) VALUES ('{0}',{1},{2},{3},{4},{5},'{6}')".format(smiles, tt, tm, vis, frag, cit, Abs)
	c.execute(statement)
	conn.commit()
	conn.close()

def db_search(query):
	conn = sqlite3.connect('GLC.db')
	c = conn.cursor()
	#c.execute("SELECT * FROM GLC;")
	#return (c.fetchall())
	c.execute("SELECT * FROM GLC WHERE SMILES=?", (query,))
	all_rows = c.fetchall()
	json_dic = {"smiles": all_rows[0][0].encode("ascii"), "tt": all_rows[0][1], "tm": all_rows[0][2], "vis": all_rows[0][3], "frag": all_rows[0][4], "cit": all_rows[0][5], "abs": all_rows[0][6].encode("ascii")}
	return json_dic

if __name__ == "__main__":
    #db_edit(smiles, tt, tm, vis, frag, cit, Abs)
    db_search(sys.argv[1])