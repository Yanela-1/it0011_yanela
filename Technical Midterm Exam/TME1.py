sum_list = []
f = open("numbers.txt", "r")
line = f.readline()
label = 1
while line!= '':
  line = line.strip()
  line = line.split(",")
  original_line = line
  numbers = [int(num) for num in line]
  line_sum = sum(numbers)
  sum_list.append(line_sum)
  line = f.readline()
  for elements in sum_list:
    x = 0
    string_elements = str(elements)
    for digit in string_elements:
      if x == 0:
        a = digit
      x += 1
    b = digit
    c = f"{a} - {b}"

    if eval(c) == 0:
      palendrome = True
    else:
      palendrome = False
  print(f"Line {label}: {','.join(original_line)} (sum {line_sum}) - {'Palindrome' if palendrome == True else 'Not a palindrome'}")
  label += 1