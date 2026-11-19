u = -3
n = int(input("Donner n="))
for k in range(n):
    print("u(", k, ")=", u)
    u = (3 + u) / 2

    from math import *
    # Définition de la suite (Un)
    # Terme U_n = 1/0! + 1/1! + ... + 1/n
    def u(n):
        return sum(1/factorial(k) for k in range(n+1))
# Définition de la suite (Vn)
    # Terme V_n = U_n + 1/1! + ... + 1/n
    def V(n):
        return U(n)+1/(factorial(n)*n)

    n = int(input("Entrer un entier n>=1 :" ))
    print(f" {'n':>4} | {'U_n':>20} | {'V_n':>20} | {'V_n - U_n':>14} ")
    print("-" * 70)
    for k in range(1,n+1):
        Uk, Vk = U(k), V(k)
         print(f" {k:>4} | {Uk:>20.10f} | {Vk:>20.10} | {Vk - Uk:>14.6e} ")
        