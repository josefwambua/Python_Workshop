#lists
numbers = [2,3,4,5,6,7]
for number in numbers.copy():
    print(number)
    if number == 4:
        numbers.remove(number)

## range does not iterate
