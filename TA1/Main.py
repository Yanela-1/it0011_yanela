prompt = str(input("1. Enter a string: "))
x = 0
for characters in prompt:
  x += 1
print(x)


numbers = str(input("2. Enter a number: "))
intnum = int(numbers)
x = 0
for digits in numbers:
  intdigits = int(digits)
  x += intdigits
print(x)

numbers = input("3. Enter a number: ")
i = 0
for characters in numbers:
  i += 1
ii = int(i)

for iteration in range(1, i+1):
  print(" " * ii, end = "")
  ii -= 1
  for jiteration in range (0, iteration):
    print(numbers[jiteration], end = "")
  print()


numbers = input("3. Enter a number: ")
i = 0
for characters in numbers:
  i += 1

iteration = 0
while iteration < i:
  intnum = int(numbers[iteration])
  jiteration = 0
  while jiteration < intnum:
    print(intnum, end = "")
    jiteration += 1
  print()
  iteration += 1

input()