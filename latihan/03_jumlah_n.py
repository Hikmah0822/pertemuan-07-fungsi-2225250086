def jumlah_n(n):
  total = 0
  for i in range(1, n + 1):
    total += i
  return total


# Uji n = 1, 5, 10, dan 100 serta bandingkan dengan rumus n(n+1)/2
for n in [1, 5, 10, 100]:
  hasil_loop = jumlah_n(n)
  hasil_rumus = n * (n + 1) // 2
  print(f"n = {n} | Perulangan: {hasil_loop} | Rumus: {hasil_rumus}")