MOD = 10**9 + 7
N = 2 * 10**5 + 10

fact = [1] * N
inv = [1] * N

for i in range(2, N):
    fact[i] = fact[i - 1] * i % MOD
inv[N - 1] = pow(fact[N - 1], MOD - 2, MOD)
for i in range(N - 2, 0, -1):
    inv[i] = inv[i + 1] * (i + 1) % MOD

def comb(n, k, mod=MOD):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv[k] % mod * inv[n - k] % mod


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10 ** 9 + 7
        nochoice = pow(m - 1 , n - 1 - k , mod) 
        possibilities = comb(n - 1, k, mod)
        return (m % mod * nochoice % mod * possibilities % mod) % mod