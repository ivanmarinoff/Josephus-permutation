def josephus(numbers, index):
    if numbers == 1:
        return 1
    else:
        return (josephus(numbers - 1, index) + index - 1) % numbers + 1


numbers = 7
index = 3
print("The chosen place is ", josephus(numbers, index))
