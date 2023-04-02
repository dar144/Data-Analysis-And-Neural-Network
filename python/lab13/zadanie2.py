# Proszę utworzyć

#     klasy opisujące pracowników i oferty pracy, z polami odpowiednio: nazwisko, wiek i wykształcenie oraz opis, wiek i wykształcenie (można rozszerzyć wg własnego pomysłu) (1p),
#     funkcję wczytującą bazy osób i ofert, jeśli istnieją odpowiednie pliki json oraz dającą możliwość ich uzupełnienia po uruchomieniu programu, przy wczytywaniu proszę skorzystać z konstrukcji match-case (3p).
#     Potrzebne będą:
#         os.path.isfile(nazwa_pliku)
#         json.load(plik)
#         json.dump(lista_obiektów, plik, cls=EnhancedJSONEncoder), gdzie:
#         class EnhancedJSONEncoder(json.JSONEncoder):
#             def default(self, o):
#                 if dataclasses.is_dataclass(o):
#                     return dataclasses.asdict(o)
#                 return super().default(o)

# funkcję wyszukującą oferty pasujące do danej osoby/osoby pasujące do danej oferty (2p).

from dataclasses import dataclass

@dataclass
class Employees:
    sec_name: str
    age: int
    education: str

emp1 = Employees('Ala', '20', 'AGH')
