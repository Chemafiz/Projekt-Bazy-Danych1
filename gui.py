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
        [sg.Output(size=(200, 10), key='kierowca_output')],
        [sg.Button('Wyświetl dane', key="kierowca_czyt")],
    ]
    autobus_czyt = [
        [sg.Output(size=(200, 10), key='autobus_output')],
        [sg.Button('Wyświetl dane', key="autobus_czyt")],
    ]
    linia_czyt = [
        [sg.Output(size=(200, 10), key='linia_output')],
        [sg.Button('Wyświetl dane', key="linia_czyt")],
    ]

    przystanek_czyt = [
        [sg.Output(size=(200, 10), key='przystanek_output')],
        [sg.Button('Wyświetl dane', key="przystanek_czyt")],
    ]

    wyswietlanie_danych = [[
        sg.TabGroup([
            [sg.Tab("kierowca", kierowca_czyt),
             sg.Tab("autobus", autobus_czyt),
             sg.Tab("linia", linia_czyt),
             sg.Tab("przystanek", przystanek_czyt)
             ]])]]


    layout = [[sg.Column(strona_glowna, key='1'),
               sg.Column(wprowadzanie_danych, visible=False, key='2'),
               sg.Column(wyswietlanie_danych, visible=False, key='3')],
              [sg.Button('Strona Główna'), sg.Button("Wprowadź dane"), sg.Button("Wyświetl dane"), sg.Button('Wyjście')]]

    window = sg.Window('Projekt Baza Danych 1', layout, size=window_size)

    layout = 1
    id_linia = 0
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
                    insert_przyjazd_polaczenie(get_last_polaczenie_id(cursor), get_last_przyjazd_id(cursor), cursor, conn)
                    output2 = window.find_element("aktualna_linia")
                    output2.update('')
                    output2.print(wyswietl_przystanki(get_last_linia_id(cursor), cursor))
                    window.find_element('id_przystanek').update('')
                    window.find_element('na_zadanie').update('')

                    sg.popup('Zapisano dane!!!')

            if event in ["kierowca_czyt", "autobus_czyt", "linia_czyt", "przystanek_czyt"]:            #wyświetlanie danych
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

    except Exception as e:
        sg.popup_error_with_traceback(f'An error happened.  Here is the info:', e)
    window.close()

if __name__ == "__main__":
    cur = conn.cursor()
    main(cur)
    cur.close()
    conn.close()



