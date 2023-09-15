# Cesarzowa Bajtocji zgubiła w napisie s swój ulubiony palindrom. Cesarzowa nikomu nie mówiła jaki
# jest jej ulubiony palindrom i wiadomo jedynie, że jest bardzo długi oraz składa się z nieparzystej
# liczby liter alfabetu łacińskiego. Postanowiono odnaleźć zaginiony palindrom cesarzowej. W tym
# celu należy zaimplementować funkcję:
# def ceasar( s )
# która na wejściu otrzymuje słowo s (składające się wyłącznie z małych liter alfabetu łacińskiego)
# i zwraca długość najdłuższego spójnego podsłowa, które jest palindromem i którego długość
# jest nieparzysta. Użyty algorytm powinien być możliwie jak najszybszy. Proszę uzasadnić jego
# poprawność i oszacować złożoność obliczeniową.
# Przykład. Dla słowa:
# akontnoknonabcddcba
# wynikiem jest 7 (kontnok; proszę zwrócić uwagę, że abcddcba jest dłuższym palindromem, ale jest
# długości parzystej więc na pewno nie jest zagubionym palindromem cesarzowej).

def ceasar(s):
    n = len(s)
    the_biggest = 0
    for i in range(1, n - 1):
        len_pal = 1
        for j in range(1, min(i - 0 + 1, n - i)):
            if s[i - j] == s[i + j]:
                len_pal += 2
                the_biggest = max(the_biggest, len_pal)
            else:
                break
    return the_biggest


s = "uzozuestbofefobtseqkaitwqkuyxyukqwtiakq"
print(ceasar(s))
