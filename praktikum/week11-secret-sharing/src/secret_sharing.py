from random import randint

# Fungsi untuk membagi rahasia (Shamir Secret Sharing)
def split_secret(secret, k, n, prime=208351617316091241234326746312124448251235562226470491514186331217050270460481):
    secret_int = int.from_bytes(secret.encode(), 'big')
    coeffs = [secret_int] + [randint(0, prime-1) for _ in range(k-1)]

    def f(x):
        return sum(coeffs[i] * (x ** i) for i in range(k)) % prime

    shares = [(i, f(i)) for i in range(1, n+1)]
    return shares

# Fungsi untuk rekonstruksi rahasia
def recover_secret(shares, prime=208351617316091241234326746312124448251235562226470491514186331217050270460481):
    def lagrange(x, xs, ys):
        total = 0
        for i in range(len(xs)):
            xi, yi = xs[i], ys[i]
            prod = yi
            for j in range(len(xs)):
                if i != j:
                    xj = xs[j]
                    prod *= (x - xj) * pow(xi - xj, -1, prime)
                    prod %= prime
            total += prod
        return total % prime

    xs, ys = zip(*shares)
    secret_int = lagrange(0, xs, ys)
    return secret_int.to_bytes((secret_int.bit_length() + 7) // 8, 'big').decode()

# =======================
# Program Utama
# =======================
secret = "KriptografiUPB2025"

shares = split_secret(secret, 3, 5)
print("Shares:")
for s in shares:
    print(s)

recovered = recover_secret(shares[:3])
print("\nRecovered secret:", recovered)