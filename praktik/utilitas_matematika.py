def luas_persegi_panjang(p, l):
  return p * l


def luas_segitiga(a, t):
  return 0.5 * a * t


def jumlah_n(n):
  if not isinstance(n, int) or n < 0:
    raise ValueError("n harus berupa bilangan bulat nonnegatif.")
  total = 0
  for i in range(1, n + 1):
    total += i
  return total


def faktorial(n):
  if not isinstance(n, int) or n < 0:
    raise ValueError("n harus berupa bilangan bulat nonnegatif.")
  hasil = 1
  for i in range(2, n + 1):
    hasil *= i
  return hasil


def tampilkan_menu():
  print("\n--- MENU UTILITAS MATEMATIKA ---")
  print("1. Luas persegi panjang")
  print("2. Luas segitiga")
  print("3. Jumlah 1 sampai n")
  print("4. Faktorial")
  print("5. Keluar")


def main():
  while True:
    tampilkan_menu()
    pilihan = input("Pilih operasi (1-5): ")

    if pilihan == "1":
      p = float(input("Masukkan panjang: "))
      l = float(input("Masukkan lebar: "))
      print(f"Hasil: {luas_persegi_panjang(p, l)}")
    elif pilihan == "2":
      a = float(input("Masukkan alas: "))
      t = float(input("Masukkan tinggi: "))
      print(f"Hasil: {luas_segitiga(a, t)}")
    elif pilihan == "3":
      try:
        n = int(input("Masukkan nilai n (bulat nonnegatif): "))
        print(f"Hasil: {jumlah_n(n)}")
      except ValueError as e:
        print(f"Input tidak valid: {e}")
    elif pilihan == "4":
      try:
        n = int(input("Masukkan nilai n (bulat nonnegatif): "))
        print(f"Hasil: {faktorial(n)}")
      except ValueError as e:
        print(f"Input tidak valid: {e}")
    elif pilihan == "5":
      print("Keluar dari program. Terima kasih!")
      break
    else:
      print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
  main()