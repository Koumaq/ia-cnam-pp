# EX1
list = [10, 4, 6, 3, 89, 45]
list.sort()
newlist = []

for n in list:
    newlist.append((n ** 2))

print(newlist)


# EX2
def is_palindrom(chaine: str):
    return chaine == chaine[::-1]

mot = "radar"
print(is_palindrom(mot))

mot = "python"
print(is_palindrom(mot))


def min_max(inputlist):
    return (min(inputlist), max(inputlist))
print(min_max(list))