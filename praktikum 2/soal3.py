n = int(input("Masukkan panjang sisi persegi: "))

print('#' * n)

for i in range(n - 2):
  print('#' + ' ' * (n - 2) + '#')

print('#' * n)
