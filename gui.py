import PySimpleGUI as sg
import psycopg2
from inserty import *

conn = psycopg2.connect("postgres://ljawypfv:1fhvD5FHUkoKLkHkgm24i5BUEpIu3cVg@rogue.db.elephantsql.com/ljawypfv")
window_size = (800,600)



def main(cursor):
    strona_glowna = [[sg.Text('Strona główna')]]                #strona główna


    kierowca_form = [                                           #wprowadzanie danych
        [sg.Text('Nazwisko'), sg.InputText(key="input1")],
        [sg.Text('Imię'), sg.InputText(key="input2")],
        [sg.Submit("Zapisz", key='zapisz_kierowca')]
    ]
    autobus_form = [
        [sg.Text('Typ autobusu:'), sg.InputText(key="input3")],
        [sg.Text('Liczba miejsc:'), sg.InputText(key="input4")],
        [sg.Submit("Zapisz", key='zapisz_autobus')]
    ]
    linia_form = [
        [sg.Text('Dostępne przystanki:          '), sg.Text('Aktualny podgląd linii: ')],
        [sg.Output(size=(20, 10), key='dostepne_przystanki'),
         sg.Output(size=(50, 10), key='aktualna_linia')],
        [sg.Text('Numer linii:'), sg.InputText(key="numer_linii")],
        [sg.Submit("Zapisz", key='zapisz_linia')],
        [sg.Text('ID przystanku'), sg.InputText(key="id_przystanek")],
        [sg.Text('Godzina przyjazdu w formacie HH:MM:SS:'), sg.InputText(key="godzina_przyjazdu")],
        [sg.Text('Godzina odjazdu w formacie HH:MM:SS:'), sg.InputText(key="godzina_odjazdu")],
        [sg.Checkbox("Czy na żądanie?", key="na_zadanie")],
        [sg.Submit("Dodaj przystanek +", key='dodaj_przystanek')]
    ]

    przystanek_form = [
        [sg.Text('Nazwa przystanku'), sg.InputText(key="input5")],
        [sg.Submit("Zapisz", key='zapisz_przystanek')]
    ]

    # Create the main layout
    wprowadzanie_danych = [[
        sg.TabGroup([
        [sg.Tab("kierowca", kierowca_form),
        sg.Tab("autobus", autobus_form),
        sg.Tab("przystanek", przystanek_form),
        sg.Tab("linia", linia_form)
         ]])]]


    kierowca_czyt= [                                            #wyświetlanie danych
        [sg.Output(size=(100, 10), key='kierowca_output')],
        [sg.Button('Wyświetl dane', key="kierowca_czyt")],
    ]
    autobus_czyt = [
        [sg.Output(size=(100, 10), key='autobus_output')],
        [sg.Button('Wyświetl dane', key="autobus_czyt")],
    ]
    linia_czyt = [
        [sg.Text('Wszystkie linie:          '), sg.Text('               Podgląd linii: ')],
        [sg.Output(size=(50, 10), key='linia_output'), sg.Output(size=(50, 10), key='dana_linia')],
        [sg.Button('Wyświetl dane', key="linia_czyt")],
        [sg.Text('Wybierz nr linii do wyświetlenia:'), sg.InputText(key="nr_linii")],
        [sg.Submit("Pokaż", key='pokaz_linia')],
    ]

    przystanek_czyt = [
        [sg.Output(size=(100, 10), key='przystanek_output')],
        [sg.Button('Wyświetl dane', key="przystanek_czyt")],
    ]

    wyswietlanie_danych = [[
        sg.TabGroup([
            [sg.Tab("kierowca", kierowca_czyt),
             sg.Tab("autobus", autobus_czyt),
             sg.Tab("linia", linia_czyt),
             sg.Tab("przystanek", przystanek_czyt)
             ]])]]


    laczenie = [                                                #łączenie
        [sg.Text('Dostępni kierowcy:            '),
         sg.Text('Dostępne autobusy:                '),
         sg.Text('Dostępne linie:')],
        [sg.Output(size=(20, 10), key='wolni_kierowcy'),
         sg.Output(size=(30, 10), key='wolne_autobusy'),
         sg.Output(size=(40, 10), key='wolne_linie')],
        [sg.Button('Wyświetl dane', key="laczenie_pokaz")],
        [sg.Text('Wybierz ID kierowcy:'), sg.InputText(key="laczenie_kierowca")],
        [sg.Text('Wybierz ID autobusu:'), sg.InputText(key="laczenie_autobus")],
        [sg.Text('Wybierz nr linii:'), sg.InputText(key="laczenie_linia")],
        [sg.Text('Wybierz numer przejazdu:'), sg.InputText(key="laczenie_numer")],
        [sg.Submit("Zapisz", key='laczenie_zapisz')],
    ]

    wyswietlanie_laczenie = [
        [sg.Output(size=(100, 10), key='polaczane_dane')],
        [sg.Button('Wyświetl dane', key="polaczane_dane_wyswietl")],
    ]

    laczenie_danych = [[
        sg.TabGroup([
            [sg.Tab("laczenie", laczenie),
             sg.Tab("wyswietlanie_laczenie", wyswietlanie_laczenie),
             ]])]]


    dodawanie_godzin_layout = [                                                        # dodawanie godzin
        [sg.Text('Linie:            '),
         sg.Text('Podgląd linii:                ')],
        [sg.Output(size=(20, 10), key='linie'),
         sg.Output(size=(50, 10), key='podglad_linii')],
        [sg.Text('Wybierz nr linii:'), sg.InputText(key="numer_linia")],
        [sg.Button('Wyświetl linie', key="wyswietl_linie")],
        [sg.Text('Godzina przyjazdu:'), sg.InputText(key="nowy_przyjazd")],
        [sg.Text('Godzina odjazdu:'), sg.InputText(key="nowy_odjazd")],
        [sg.Submit("Zapisz", key='dodaj_zapisz')],
    ]

    dodawanie_godzin = [[
        sg.TabGroup([
            [sg.Tab("Dodawanie_godzin", dodawanie_godzin_layout)]])]]


    layout = [[sg.Column(strona_glowna, key='1'),
               sg.Column(wprowadzanie_danych, visible=False, key='2'),
               sg.Column(wyswietlanie_danych, visible=False, key='3'),
               sg.Column(laczenie_danych, visible=False, key='4'),
               sg.Column(dodawanie_godzin, visible=False, key='5')],
              [sg.Button('Strona Główna'), sg.Button("Wprowadź dane"), sg.Button("Wyświetl dane"), sg.Button("Łączenie danych"), sg.Button("Dodawanie godzin"), sg.Button('Wyjście')]]

    window = sg.Window('Projekt Baza Danych 1', layout, size=window_size)

    layout = 1
    numer_przejazdu = 0
    first_id_polaczenie = 0
    try:
        while True:
            event, values = window.read()
            print(event, values)
            if event in (None, 'Wyjście'):
                break
            if event == 'Strona Główna':
                window[str(layout)].update(visible=False)
                layout = 1
                window[str(layout)].update(visible=True)
            if event == "Wprowadź dane":
                window[str(layout)].update(visible=False)
                layout = 2
                window[str(layout)].update(visible=True)
            if event == "Wyświetl dane":
                window[str(layout)].update(visible=False)
                layout = 3
                window[str(layout)].update(visible=True)
            if event == "Łączenie danych":
                window[str(layout)].update(visible=False)
                layout = 4
                window[str(layout)].update(visible=True)
            if event == "Dodawanie godzin":
                window[str(layout)].update(visible=False)
                layout = 5
                window[str(layout)].update(visible=True)
                output = window.find_element("linie")
                output.update('')
                output.print(view_linia(cursor))

            if event in ["zapisz_kierowca", "zapisz_autobus", "zapisz_przystanek", "zapisz_linia", "dodaj_przystanek"]:          #zapis danych
                if event == "zapisz_kierowca":
                    print(str(values["input1"]))
                    insert_kierowca(values["input1"], values["input2"], cursor, conn)
                    window.find_element('input1').update('')
                    window.find_element('input2').update('')
                    sg.popup('Zapisano dane!!!')
                if event == "zapisz_autobus":
                    insert_autobus(values["input3"], values["input4"], cursor, conn)
                    window.find_element('input3').update('')
                    window.find_element('input4').update('')
                    sg.popup('Zapisano dane!!!')
                if event == "zapisz_przystanek":
                    insert_przystanek(values["input5"], cursor, conn)
                    window.find_element('input5').update('')
                    sg.popup('Zapisano dane!!!')

                if event == "zapisz_linia":
                    output1 = window.find_element("dostepne_przystanki")
                    output1.update('')
                    output1.print(view_przystanek(cursor))
                    window.find_element('numer_linii').update('')
                    insert_linia(values["numer_linii"], cursor, conn)
                    output2 = window.find_element("aktualna_linia")
                    output2.update('')
                    output2.print("Linia: " + values["numer_linii"] + "\nPrzystanki: \n")
                    sg.popup('Dodano linię!!!')
                if event == "dodaj_przystanek":
                    insert_polaczenie(values["id_przystanek"], values["na_zadanie"], cursor, conn)
                    insert_przyjazd(values["godzina_przyjazdu"], values["godzina_odjazdu"], cursor, conn)
                    insert_linia_polaczenie(get_last_linia_id(cursor), get_last_polaczenie_id(cursor), cursor, conn)
                    insert_przyjazd_polaczenie(get_last_polaczenie_id(cursor), get_last_przyjazd_id(cursor), 1, cursor, conn)
                    output2 = window.find_element("aktualna_linia")
                    output2.update('')
                    output2.print(wyswietl_przystanki(get_last_linia_id(cursor), cursor))
                    window.find_element('id_przystanek').update('')
                    window.find_element('na_zadanie').update('')

                    sg.popup('Zapisano dane!!!')

            if event in ["kierowca_czyt", "autobus_czyt", "linia_czyt", "przystanek_czyt", "pokaz_linia"]:            #wyświetlanie danych
                if event == "kierowca_czyt":
                    output = window.find_element("kierowca_output")
                    output.update('')
                    output.print(view_kierowca(cursor))
                if event == "autobus_czyt":
                    output = window.find_element("autobus_output")
                    output.update('')
                    output.print(view_autobus(cursor))
                if event == "przystanek_czyt":
                    output = window.find_element("przystanek_output")
                    output.update('')
                    output.print(view_przystanek(cursor))
                if event == "linia_czyt":
                    output = window.find_element("linia_output")
                    output.update('')
                    output.print(view_linia(cursor))
                if event == "pokaz_linia":
                    output1 = window.find_element("dana_linia")
                    output1.update('')
                    output1.print(wyswietl_przystanki_dla_numeru_linii(values["nr_linii"], cursor))


            if event in ["laczenie_pokaz", "laczenie_zapisz", "polaczane_dane_wyswietl"]:              # laczenie danych
                if event == "laczenie_pokaz":
                    output1 = window.find_element("wolni_kierowcy")
                    output2 = window.find_element("wolne_autobusy")
                    output3 = window.find_element("wolne_linie")
                    output1.update('')
                    output2.update('')
                    output3.update('')
                    output1.print(view_wolny_kierowca(cursor))
                    output2.print(view_wolny_autobus(cursor))
                    output3.print(view_wolna_linia(cursor))
                if event == "laczenie_zapisz":
                    polacz_dane(values["laczenie_kierowca"], values["laczenie_autobus"], values["laczenie_linia"], values["laczenie_numer"], cursor, conn)
                    sg.popup('Zapisano dane!!!')
                if event == "polaczane_dane_wyswietl":
                    output = window.find_element("polaczane_dane")
                    output.update('')
                    output.print(view_polaczone_dane(cursor))


            if event in ["wyswietl_linie", "dodaj_zapisz"]:              # dodawanie godzin
                if event == "wyswietl_linie":
                    output = window.find_element("podglad_linii")
                    output.update('')
                    output.print(wyswietl_przystanki_dla_numeru_linii(values["numer_linia"], cursor))
                    numer_przejazdu = get_ostatni_numer_przejazdu(values["numer_linia"], cursor) + 1
                    first_id_polaczenie = get_pierwszy_id_przyjazd(values["numer_linia"], cursor)
                if event == "dodaj_zapisz":
                    insert_przyjazd_polaczenie(first_id_polaczenie, get_last_przyjazd_id(cursor) + 1, numer_przejazdu, cursor, conn)
                    insert_przyjazd(values["nowy_przyjazd"], values["nowy_odjazd"], cursor, conn)
                    first_id_polaczenie += 1
                    output = window.find_element("podglad_linii")
                    output.update('')
                    output.print(wyswietl_przystanki_dla_numeru_linii(values["numer_linia"], cursor))
                    sg.popup('Zapisano dane!!!')


    except Exception as e:
        sg.popup_error_with_traceback(f'An error happened.  Here is the info:', e)
    window.close()

if __name__ == "__main__":
    cur = conn.cursor()
    main(cur)
    cur.close()
    conn.close()



