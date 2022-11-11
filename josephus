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
