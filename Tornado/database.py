import sqlite3

def db_edit(data):
	conn = sqlite3.connect('GLC.db')
	c = conn.cursor()

	c.execute("CREATE TABLE GLC(TG INT, TT INT, Viscocity INT, Molecular Formula TEXT, Fragility INT, Citation TEXT, Abstract TEXT")
	conn.commit()
	conn.close()

if __name__ == "__main__":
    db_edit()