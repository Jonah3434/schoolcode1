'''
Jonah Belttari
12-18-19
''' 
print("What operation would you like the calculator to perform? ")
print("   + = addition ")
print("   - = subtraction ")
print("   * = multiplication ")
print("   / = Division ")
print("   % = Modulus  ")
sign=input("Enter the sign you want to use. \n ===>   ")
print("Enter the numbers you want.\n")
num1=int(input("number1  \n"))
num2=int(input("number2  \n"))
if sign == "+":
  final = int(num1 + num2)
  print( str(num1) + " added to "+ str(num2) + " equals " + str(final) +"\n")
elif sign == "-":
  final = int(num1 - num2)
  print( str(num1) + " minus "+ str(num2) + " equals " + str(final)+"\n")
elif sign == "*":
  final = int(num1 * num2)
  print( str(num1) + " multiplied by "+ str(num2) + " equals " + str(final) +"\n")
elif sign == "/":
  final = int(num1 / num2)
  print(str(num1) + " divided by "+ str(num2) + " equals " + str(final) + "\n")
elif sign == "%":
  final = int(num1 % num2)
  print( "The modulo of " + str(num1) + " and "+ str(num2) + " is equals to " + str(final) +"\n")