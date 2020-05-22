import sqlite3

def banco():
    conn = sqlite3.connect(':memory:')

    c = conn.cursor()

    c.execute('''CREATE TABLE teste (id integer, nome text not null)''')
    c.execute("INSERT INTO teste VALUES (1, 'Thiago')")
    c.execute("INSERT INTO teste VALUES (2, 'Kuma')")
    c.execute("INSERT INTO teste VALUES (3, 'Impacta')")

    c.execute('''SELECT count(*)  FROM  teste''')

    x = None
    for row in c.fetchall():
        x = row
        print(row)

    conn.commit()
    conn.close()
    return x

def test_banco():
    assert banco() == (3,), 'Deveria ser 3'