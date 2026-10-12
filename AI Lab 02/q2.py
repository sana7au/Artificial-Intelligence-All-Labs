numbers = []

for i in range(1, 16):
    numbers.append(i)
    
print("Numbers: ", numbers)

even_numbers = []
odd_numbers = []

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)   

print("\nEven Numbers: ", even_numbers)
print("Odd Numbers: ", odd_numbers)

numbers.sort(reverse=True)
print("\nDescending: ", numbers)

print("\nMiddle five: ", numbers[5:10])