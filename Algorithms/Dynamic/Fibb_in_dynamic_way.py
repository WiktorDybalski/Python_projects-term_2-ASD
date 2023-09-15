# Finding the nth term of the Fibonacci sequence

def fibb1(n):
    a = 1
    b = 1
    for cnt in range(3, n + 1):
        a, b = b, a + b
    return b


def fibb2(n):
    F = [1] * (n + 1)
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n - 1]


print(fibb1(7))
print(fibb2(7))
