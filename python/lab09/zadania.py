class IncorrectYear(Exception):
    """ Powstaje kiedy rok jest podany niepoprawnie """
    pass

class IncorrectDay(Exception):
    """ Powstaje kiedy dzien jest podany niepoprawnie """
    pass

class IncorrectMonth(Exception):
    """ Powstaje kiedy miesiac jest podany niepoprawnie """
    pass

class IncorrectPlec(Exception):
    """ Powstaje kiedy plec jest podana niepoprawnie """
    pass

class IncorrectControlNumber(Exception):
    """ Powstaje kiedy liczba controlna jest podana niepoprawnie """
    pass


def pesel(pes, date, plec):
    """ Funkcja sprawdza poprawność numeru PESEL"""
    date = date.split()
    day = date[0]
    if int(day) < 10:
        day = '0' + day
    month = date[1]
    year = date[2]
    month_name = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 'wrzesnia', 'pazdziernika', 'listopada', 'grudnia']

    # year
    if year[2]+year[3] != pes[0]+pes[1]:
        raise IncorrectYear()

    # day
    if day != pes[4]+pes[5]:
        raise IncorrectDay()

    # month
    month = month_name.index(month)+1
    
    tmp = 0
    start = 19
    end = 20
    if start-1 <= int(year[0]+year[1]) < end-1:
        tmp = 80
    else:
        while not start <= int(year[0]+year[1]) < end:
            tmp += 20
            start += 1
            end += 1

    month += tmp 

    if month != int(pes[2]+pes[3]):
        raise IncorrectMonth()

    # plec
    if plec == ("kobieta"and int(pes[9])%2==1) or (plec == "mezczyzna" and int(pes[9])%2==0):
        raise IncorrectPlec()

    # liczba kontrolna
    weight = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    contrl = 0
    for i in range(len(pes)-1):
        contrl += int(pes[i])*weight[i]
    contrl %= 10
    contrl = 10 - contrl
    contrl %= 10

    assert contrl == int(pes[10]), "Error control number"
    if contrl != int(pes[10]):
        raise IncorrectControlNumber()


    return "Numer PESEL jest poprawny"



class IncorrectMode(Exception):
    """ Powstaje kiedy tryb jest podany niepoprawnie """
    pass

class IncorrectNumberOfElements(Exception):
    """ Powstaje kiedy w linijce jest za malo elementow"""
    pass

class IncorrectNumberOfDays(Exception):
    """ Powstaje kiedy liczba dni w miesiacu sie nie zgadza"""
    pass


def aver_age(filename, mode):
    """ Funkcja zwraca średni wiek osób, który daty urodzenia zapisane są w pliku """
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    suma = 0
    num = 0
    
    curr_day = 9
    curr_month = 5
    curr_year = 2022

    with open(filename) as f:
        if mode == 'r':
            for line in f: 
                if len(line) != 3:
                    # pass
                    raise IncorrectNumberOfElements()
                else:
                    day = int(line[0])
                    month = int(line[1])
                    year = int(line[2])

                    if year % 4 == 0 and (year % 100 != 0 or year % 400 != 0):
                        months[1] = 29
                    else:
                        months[1] = 28

                    if day > months[month - 1]:
                        raise IncorrectNumberOfDays()

        elif mode == 'l':
            for line in f:
                line = line.split()

                if len(line) == 3:
                    day = int(line[0])
                    month = int(line[1])
                    year = int(line[2])

                    if year % 4 == 0 and (year % 100 != 0 or year % 400 != 0):
                        months[1] = 29
                    else:
                        months[1] = 28

                    if day <= months[month - 1]:
                        if month < curr_month:
                            suma += curr_year - year
                        elif month > curr_month:
                            suma += curr_year - year - 1
                        else:
                            if day <= curr_day:
                                suma += curr_year - year
                            else:
                                suma += curr_year - year - 1
                        num += 1
                        
            return round(suma / num, 2)

        else:
            raise IncorrectMode()





if __name__ == '__main__':
    pass