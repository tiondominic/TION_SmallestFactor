numberInput = eval(input("Enter a num >2: "))

for number in range(2, numberInput + 1): #adding 1 so the end will be the same as the number inputted
    remainder = numberInput % number
    if remainder > 0:
        continue
    else:
        break

print("The lowest factor is", number)