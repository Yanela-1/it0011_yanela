def divide(a, b):
  if b == 0:
    print("The second number of denominator must not be equal to zero")
    return None
  return a / b

def exponentiate(a, b):
  return a ** b

def remainder(a, b):
  if b == 0:
    print("The second number or denominator must not be equal to zero")
    return None
  return a % b

def summation(a, b):
  if a > b:
    print("The second number must be greater than the first number")
    return None
  return sum(range(a, b + 1))

while True:
  print("\nMathematical Operations:")
  print("[D] - Divide")
  print("[E] - Exponentiation")
  print("[R] - Remainder")
  print("[F] - Summation")

  choice = input("Enter your choice: ").strip().upper()

  if choice in ['D', 'E', 'R', 'F']:
    try:
      a = float(input("Enter the first number: "))
      b = float(input("Enter the second number: "))
 
      result = None
      if choice == 'D':
        result = divide(a, b)
      elif choice == 'E':
        result = exponentiate(a, b)
      elif choice == 'R':
        result = remainder(a, b)
      elif choice == 'F':
        result = summation(int(a), int(b))
    
      if result is not None:
        print(f"Result: {result}")
    except ValueError:
      print("Only input numbers.")
  else:
    print("Invalid choice.")
