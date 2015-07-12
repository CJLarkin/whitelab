import sqlite3

def db_edit(smiles, tt, tm, vis, frag, cit, Abs):
	conn = sqlite3.connect('GLC.db')
	c = conn.cursor()

	#conn.execute("CREATE TABLE GLC(SMILES, TT INT, TM INT, Viscocity INT, Fragility INT, Citation INT, Abstract TEXT)")
	statement = "INSERT INTO GLC (SMILES, TT, TM, Viscocity, Fragility, Citation, Abstract) VALUES ('{0}',{1},{2},{3},{4},{5},'{6}')".format(smiles, tt, tm, vis, frag, cit, Abs)
	#print statement
	conn.execute(statement)
	thing = conn.execute("SELECT SMILES, TT, TM, Viscocity, Fragility, Citation, Abstract from GLC")
	for row in thing:
		return row[0],row[1],row[2],row[3],row[4],row[5],row[6]
	#FOR SEARCHING
	cur.execute("SELECT * FROM list WHERE InstitutionName=?", (Variable,))
	conn.commit()
	conn.close()

if __name__ == "__main__":
    db_edit(smiles, tt, tm, vis, frag, cit, Abs)