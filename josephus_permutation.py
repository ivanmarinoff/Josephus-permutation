"""
This problem takes its name by arguably the most important event in the life of the ancient historian Josephus:
 according to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege.
 Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: t
 hey formed a circle and proceeded to kill one man every three, until one last man was left
 (and that it was supposed to kill himself to end the act).
 Well, Josephus and another man were the last two and, as we now know every detail of the story,
 you may have correctly guessed that they did not exactly follow through the original idea.
You are now to create a program that prints a Josephus permutation,
receiving two lines of code (the list itself (string with elements separated by a single space) and a number k)
 as if they were in a circle and counted out every k places until none remained.
Input
1 2 3 4 5 6 7
3

Output
[3,6,2,7,5,1,4]
"""

place = [int(n) for n in input().split()]
index, new_place, count = -1, [], int(input())
while len(place) > 0:
    for _ in range(count):
        index += 1
        if index == len(place):
            index = 0

    new_place.append(place.pop(index))
    index -= 1

dead_place = repr(new_place).replace(" ", "")
print(dead_place)

# def josephus(numbers, index):
#     if numbers == 1:
#         return 1
#     else:
#         return (josephus(numbers - 1, index) + index - 1) % numbers + 1
#
#
# numbers = 7
# index = 3
# print("The chosen place is ", josephus(numbers, index))
