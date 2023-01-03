n = int(input("Masukkan banyaknya angka: "))

total = 0

for i in range(n):
  x = float(input("Masukkan angka: "))
  total += x

rata_rata = total / n
print("Rata-rata:", rata_rata)
