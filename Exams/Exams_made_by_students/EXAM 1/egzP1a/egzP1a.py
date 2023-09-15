from egzP1atesty import runtests
from math import inf


def f(word, to_use, dp, n):
    dp[len(word)] = 0
    for i in range(n - 1, -1, -1):
        for w in to_use:
            if word[i: i + len(w)] == w:
                dp[i] = min(dp[i], dp[i + len(w)] + 1)
    return dp[0]


def titanic(W, M, D):
    word = W
    morse_word = ""
    dict = M
    for letter in word:
        for i in range(len(dict)):
            if dict[i][0] is letter:
                morse_word = morse_word + dict[i][1]
                break
    to_use = []
    for i in range(len(D)):
        to_use.append(dict[D[i]][1])
    n = len(morse_word)
    dp = [inf for _ in range(n + 1)]
    minimum = f(morse_word, to_use, dp, n)
    return minimum


runtests(titanic, recursion=False)
