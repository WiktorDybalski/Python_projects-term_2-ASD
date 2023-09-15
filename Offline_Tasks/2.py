# System chłodzenia serwerów na pewnej uczelni wymaga stałych dostaw śniegu. Grupa zmotywowanych profesorów odnalazła
# w wysokich górach wąwóz, z którego można przywieźć śnieg. Wąwóz jest podzielony na n obszarów i ma wjazdy z zachodu i
# wschodu. Na każdym obszarze wąwozu znajduje się pewna ilość śniegu, opisana w tablicy S. W szczególności S[0]
# to liczba metrów sześciennych śniegu bezpośrednio przy zachodnim wjeździe, S[1] to liczba metrów sześciennych
# śniegu na kolejnym obszarze, a S[n−1] to liczba metrów sześciennych śniegu przy wjeździe wschodnim (wiadomo,
# że zawartość tablicy S to liczby naturalne). Profesorowie dysponują maszyną, która danego dnia może zebrać śnieg
# ze wskazanego obszaru, wjeżdżając odpowiednio z zachodu lub wschodu. Niestety, są trzy komplikacje:
#
# 1. Po drodze do danego obszaru maszyna topi cały śnieg na tych obszarach, po których przejeżdża
# (o ile nie został wcześniej zebrany). Na przykład jadąc z zachodu do obszaru 2 zeruje wartości S[0] oraz S[1]
# (bo po nich przejeżdża) oraz S[2] (bo ten śnieg zbiera).

# 2. Każdego dnia maszyna może zebrać śnieg tylko z jednego, dowolnie wybranego obszaru, wjeżdzając albo z zachodu albo
# ze wschodu.

# 3. Ze względu na wysoką temperaturę, po każdym dniu na każdym obszarze topi się dokładnie jeden metr sześcienny
# śniegu.
# Zadanie polega na zaimplementowaniu funkcji:
# def snow( S ) która zwraca ile metrów sześciennych maksmalnie można zebrać z wąwozu (zebrany śnieg jest zabezpieczany
# i już się nie topi).

# Rozważmy następujące dane:
# S = [1,7,3,4,1]
# wywołanie snow(S) powinno zwrócić liczbę 11. Możliwy plan zbierania śniegu to: zebranie 7m3 pierwszego dnia z obszaru
# 1 wjeżdżając z zachodu, zebranie 3m3 drugiego dnia z obszaru 3 wjeżdżając ze wschodu (1m3 się stopił po pierwszym
# dniu), oraz zebranie 1m3 trzeciego dnia z obszaru 2 wjeżdżając z dowolnego kierunku (po dwóch dniach ilość śniegu
# na tym obszarze zmniejszy się z 3m3 do 1m3).
# Zadanie można rozwiązać w czasie O(nlog n), gdzie n to rozmiar wąwozu.

def Counting_Sort(array):
    n = len(array)
    k = max(array)
    amount_of_el = [0 for _ in range(k + 1)]
    sorted_array = [0 for z in range(n)]
    for i in range(n):
        amount_of_el[array[i]] += 1

    for j in range(1, k + 1):
        amount_of_el[j] += amount_of_el[j - 1]

    for s in range(n):
        sorted_array[amount_of_el[array[s]] - 1] = array[s]
        amount_of_el[array[s]] -= 1
    return sorted_array


def snow(S):
    n = len(S)
    S = Counting_Sort(S)
    suma = 0
    amount_of_day = 0
    for i in range(n - 1, -1, -1):
        if S[i] - amount_of_day <= 0:
            return suma
        suma += S[i] - amount_of_day
        amount_of_day += 1
    return suma
