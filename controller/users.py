import services.database as db

def incluir(nome, matricula, password):
    try:
        db.cur.execute("""
                    INSERT into streamservice.users (name, matricula, password)
                    VALUES ('%s','%s','%s')
                    """ % (nome, matricula, password))
        db.con.commit()
    
    except:
        db.con.rollback()
        return False


def deletar(matricula):
    try:
        query = "DELETE FROM streamservice.users WHERE matricula = %s"
        db.cur.execute(query, (matricula,))
        db.con.commit()
    except:
        db.con.rollback()
        return False
    
def selecionar():
    query = "SELECT * FROM streamservice.users"
    db.cur.execute(query)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows
