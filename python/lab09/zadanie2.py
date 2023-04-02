    # Funkcję sprawdzającą poprawność numeru PESEL, w przypadku stwierdzenia niepoprawności poszczególnych elementów proszę zgłosić odpowiedni wyjątek (3.5p)
    # Parametrami wejściowymi do funkcji są: Pesel, data urodzenia (datetime.date) oraz płeć.
    # Przykłady:

    #     02070803628, 8 lipca 1902, kobieta
    #     02270803624, 8 lipca 2002, kobieta
    #     02270812350, 8 lipca 2002, mężczyzna

    #     cyfry 1-2 to ostatnie dwie cyfry roku urodzenia
    #     cyfry 3-4 to dwie cyfry miesiąca urodzenia
    #     cyfry 5-6 to dwie cyfry dnia urodzenia
    #     cyfry 7-10 liczba porządkowa z oznaczeniem płci (liczba parzysta - kobieta, liczba nieparzysta - mężczyzna)
    #     cyfra 11 suma kontrolna

    # Do numeru miesiąca dodawane są następujące wartości w zależności od roku:

    #     dla lat 1800 - 1899 - 80
    #     dla lat 1900 - 1999 - 0
    #     dla lat 2000 - 2099 - 20
    #     dla lat 2100 - 2199 - 40
    #     dla lat 2200 - 2299 - 60

    # Suma kontrolna: każdą pozycję numeru ewidencyjnego mnoży się przez odpowiednią wagę, są to kolejno: 1 3 7 9 1 3 7 9 1 3 i sumuje.
    # Wynik dzieli się modulo 10 i otrzymaną wartość należy odjąć od 10 i znów podzielić modulo 10.
    # Otrzymana wartość powinna być zgodna z ostatnią cyfrą numeru PESEL.

def pesel(pes, date, plec):
    date = date.split()
    day = date[0]
    if int(day) < 10:
        day = '0' + day
    month = date[1]
    year = date[2]
    month_name = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 'wrzesnia', 'pazdziernika', 'listopada', 'grudnia']

    # year
    assert year[2]+year[3] == pes[0]+pes[1], "Error year"

    # day
    assert day == pes[4]+pes[5], "Error day"

    # month
    month = month_name.index(month)+1
    
    tmp = 0
    start = 19
    end = 20
    if start-1 <= int(year[0]+year[1]) < end-1:
        tmp = 80
    while start < int(year[0]+year[1]) < end:
        tmp += 20
        start += 1
        end += 1

    month += tmp 

    print(month)
    print(pes[2]+pes[3])

    # assert str(month) == pes[2]+pes[3], "Error month"

    



    






    return date


print(pesel('02070803628', '8 lipca 1902', 'kobieta'))
