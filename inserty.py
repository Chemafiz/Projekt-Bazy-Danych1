from datetime import datetime

def insert_kierowca(nazwisko, imie, cursor, connection ):
    insert = """
    INSERT INTO kierowca (nazwisko, imie)
    VALUES (%s, %s)
    """

    cursor.execute(insert, (nazwisko, imie))
    connection.commit()


def insert_przystanek(nazwa, cursor, connection ):
    insert = """
    INSERT INTO przystanek(nazwa)
    VALUES (%s)
    """

    cursor.execute(insert, (nazwa,))
    connection.commit()


def insert_autobus(typ, liczba_miejsc, cursor, connection ):
    insert = """
    INSERT INTO autobus(typ_autobusu, liczba_miejsc)
    VALUES (%s, %s)
    """

    cursor.execute(insert, (typ, liczba_miejsc))
    connection.commit()

def insert_linia(nr_linii, cursor, connection):
    insert = """
    INSERT INTO linia(nr_linii)
    VALUES (%s)
    """

    cursor.execute(insert, (nr_linii,))
    connection.commit()


def insert_polaczenie(id_przystanek, na_zadanie,  cursor, connection):
    insert = """
    INSERT INTO polaczenie(id_przystanek, na_zadanie)
    VALUES (%s, %s)
    """

    cursor.execute(insert, (id_przystanek,na_zadanie))
    connection.commit()


def insert_linia_polaczenie(id_linia, id_polaczenie,  cursor, connection):
    insert = """
    INSERT INTO linia_polaczenie(id_linia, id_polaczenie)
    VALUES (%s, %s)
    """

    cursor.execute(insert, (id_linia, id_polaczenie))
    connection.commit()


def insert_przyjazd_polaczenie(id_polaczenie,id_przyjazd, cursor, connection):
    insert = """
    INSERT INTO przyjazd_polaczenie(id_polaczenie,id_przyjazd)
    VALUES (%s, %s)
    """

    cursor.execute(insert, (id_polaczenie,id_przyjazd))
    connection.commit()


def insert_przyjazd(godzina_przyjazd, godzina_odjazd, cursor, connection):
    insert = """
    INSERT INTO przyjazd(godzina_przyjazd, godzina_odjazd)
    VALUES (%s, %s)
    """

    cursor.execute(insert, (godzina_przyjazd, godzina_odjazd))
    connection.commit()


def view_kierowca(cursor):
    select = """
    SELECT * from kierowca
    """
    cursor.execute(select)
    rows = cursor.fetchall()
    string = ""
    for row in rows:
        string += str(row)
        string += "\n"
    return string


def view_autobus(cursor):
    select = """
    SELECT * from autobus
    """
    cursor.execute(select)
    rows = cursor.fetchall()
    string = ""
    for row in rows:
        string += str(row)
        string += "\n"
    return string


def view_linia(cursor):
    select = """
    SELECT * from linia
    """
    cursor.execute(select)
    rows = cursor.fetchall()
    string = ""
    for row in rows:
        string += str(row)
        string += "\n"
    return string


def view_przystanek(cursor):
    select = """
    SELECT * from przystanek
    """
    cursor.execute(select)
    rows = cursor.fetchall()
    string = ""
    for row in rows:
        string += str(row)
        string += "\n"
    return string


def get_last_linia_id(cursor):
    query = """
    SELECT id_linia FROM linia ORDER BY id_linia DESC LIMIT 1;
    """
    cursor.execute(query)
    id = cursor.fetchall()
    return id[0][0]


def get_last_polaczenie_id(cursor):
    query = """
    SELECT id_polaczenie FROM polaczenie ORDER BY id_polaczenie DESC LIMIT 1;
    """
    cursor.execute(query)
    id = cursor.fetchall()
    return id[0][0]


def get_last_przyjazd_id(cursor):
    query = """
    SELECT id_przyjazd FROM przyjazd ORDER BY id_przyjazd DESC LIMIT 1;
    """
    cursor.execute(query)
    id = cursor.fetchall()
    return id[0][0]


def wyswietl_przystanki(id, cursor):
    query = f"""
        SELECT * FROM wyswietl_przystanki({id})
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    string = "Linia    nazwa    na żądanie    przyjazd    odjazd\n"
    for row in rows:
        string += str(row[0]) + "    " + row[1] + "      " + str(row[2])
        string += "    " + row[3].strftime("%H:%M:%S") + "    " + row[4].strftime("%H:%M:%S")
        string += "\n"
    return string