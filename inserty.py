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


def insert_przyjazd_polaczenie(id_polaczenie,id_przyjazd, numer_przejazdu, cursor, connection):
    insert = """
    INSERT INTO przyjazd_polaczenie(id_polaczenie,id_przyjazd, numer_przejazdu)
    VALUES (%s, %s, %s)
    """

    cursor.execute(insert, (id_polaczenie, id_przyjazd, numer_przejazdu))
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


def view_wolny_kierowca(cursor):
    select = """
    select id_kierowca, nazwisko, imie from kierowca 
    left join autobus using (id_kierowca)
    where autobus.id_kierowca is null 
    order by id_kierowca;
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


def view_wolny_autobus(cursor):
    select = """
    select id_autobus, typ_autobusu, liczba_miejsc from autobus
    where id_kierowca is NULL
    and id_linia is NULL
    group by id_autobus;
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
    select nr_linii, count(*) from przystanki_info
    group by nr_linii
    order by nr_linii;
    """
    cursor.execute(select)
    rows = cursor.fetchall()
    string = "nr linii     ilość przystanków\n"
    for row in rows:
        string += str(row[0]) + "         " + str(row[1])
        string += "\n"
    return string


def view_wolna_linia(cursor):
    select = """
    select nr_linii, numer_przejazdu, count(*) from przystanki_info 
    left join autobus using (id_linia)
    where autobus.id_linia is null
    group by (nr_linii, numer_przejazdu)
    order by nr_linii;
    """
    cursor.execute(select)
    rows = cursor.fetchall()
    string = "nr linii     ilość przystanków\n"
    for row in rows:
        string += str(row[0]) + "  " + str(row[1]) + "         " + str(row[2])
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

def view_polaczone_dane(cursor):
    select = """
    select imie, nazwisko, id_autobus, nr_linii, numer_przejazdu from
    kierowca join autobus using (id_kierowca)
    join linia_polaczenie using (id_linia)
    join linia using (id_linia)
    join polaczenie using (id_polaczenie)
    join przyjazd_polaczenie using (id_polaczenie)
    where id_kierowca is not NULL
    and id_linia is not NULL
    group by (imie, nazwisko, id_autobus, nr_linii, numer_przejazdu );
    """
    cursor.execute(select)
    rows = cursor.fetchall()
    string = "imie      nazwisko     id autobusu        nr linii\n".upper()
    string += "-" * 100 + "\n"
    for row in rows:
        string += str(row[0]) + "      " + str(row[1]) + "                 " + str(row[2]) + "                     " + str(row[3]) + "   " + str(row[4])
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

def wyswietl_przystanki_dla_numeru_linii(nr, cursor):
    query = f"""
        SELECT * FROM przystanki_dla_linii({nr}) order by godzina_przyjazdu
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    string = "Linia    nazwa        na żądanie    przyjazd    odjazd\n"
    for row in rows:
        string += str(row[0]) + "  " + str(row[1]) + "    " + row[2] + "      " + str(row[3])
        string += "    " + row[4].strftime("%H:%M:%S") + "    " + row[5].strftime("%H:%M:%S")
        string += "\n"
    return string


def polacz_dane(id_kierowca, id_autobus, nr_linia, cursor, connection):
    query = f"""
        SELECT * FROM polacz_dane({id_kierowca},{id_autobus},{nr_linia})
    """
    cursor.execute(query)
    connection.commit()


def get_ostatni_numer_przejazdu(nr_linii, cursor):
    query = f"""
            select * from ostatni_numer_przejazdu({nr_linii});
        """
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows[0][0]


def get_pierwszy_id_przyjazd(nr_linii, cursor):
    query = f"""
            select * from get_pierwszy_id_przyjazd({nr_linii});
        """
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows[0][0]



