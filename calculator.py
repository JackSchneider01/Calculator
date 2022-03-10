numb = int(input("Pick a number   "))
oper = input("Pick an operator +, -, *, /, %, **.  ")
numb_two = int(input("Pick another number   "))

if oper == "+":
    answer = numb + numb_two

elif oper == "-":
    answer = numb - numb_two

elif oper == "*":
    answer = numb * numb_two

elif oper == "/":
    answer = numb / numb_two

elif oper == "%":
    answer = numb % numb_two

elif oper == "**":
    answer = numb ** numb_two

print (answer)