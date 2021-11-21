# List_Tst01.txt   Last updated: 21_09_27

#List
l = [2,5,1,4,3]
print(f"l = {l}")
print(f"len(l) = {len(l)}")  # len(l) = 5
print(f"l[3] = {l[3]}")  # l[3] = 4

# Sort a list
l.sort()
print(f"l.sort() = {l} ")   # l.sort() = [1, 2, 3, 4, 5]

# Reverse a list
l.reverse()
print(f"l.reverse() = {l} ")  # l.reverse() = [5, 4, 3, 2, 1]

# Create a list with range
list0_4 = list(range(5))
list1_4 = list(range(1,5))     # list1_4 = [1, 2, 3, 4]
print(f"list0_4 = {list0_4}")  # list0_4 = [0, 1, 2, 3, 4]

list2 = ["string", 1.234, 3]
print(f"list2 = {list2}")  # list2 = ['string', 1.234, 3]

# Append a value to the end of a list
list2.append("Another")
print(f"list2 = {list2}")  # list2 = ['string', 1.234, 3, 'Another']

# Combine lists
combine_list = list0_4 + list2
print(f"combine_list = {combine_list}")  # combine_list = [0, 1, 2, 3, 4, 'string', 1.234, 3, 'Another']

# Find out how many times an item is in the list
c = combine_list.count(3)
print(f"combine_list.count(3) = {c}")  # combine_list.count(3) = 2



planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(f"planets = {planets}")
print(f"planets[1] = {planets[1]}")
print(f"planets[-1] = {planets[-1]}")
print(f"planets[-2] = {planets[-2]}")
print(f"planets[0:3] = {planets[0:3]}")
print(f"planets[1:-1] = {planets[1:-1]}")
print(f"planets[3:] = {planets[3:]}")
print(f"planets[-3:] = {planets[-3:]}")
print(f"planets.index('Earth')= {planets.index('Earth')}")
b = "Earth" in planets
print(f"b = {b}")

print("in planets:")
for planet in planets:
    print(planet, end=' ') # print all on same line
print()

for planet in planets:
    print(f"{ planets.index(planet) }-{ planet }", end=',  ') # print all and the index on same line
                   #0-Mercury,  1-Venus,  2-Earth,  3-Mars,  4-Jupiter,  5-Saturn,  6-Uranus,  7-Neptune,
print()

planets.append('Pluto')
print(f"len(planets) = {len(planets)}")
print(f"planets = {planets}")

planets.pop()
print(f"len(planets) = {len(planets)}")
print(f"planets = {planets}")

short_planets = [planet for planet in planets if len(planet) < 6]
print(f"short_planets = {short_planets}")

# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(f"loud_short_planets = {loud_short_planets}")

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
print(f"hands = {hands}")   # hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

#my_favourite_things = [32, 'raindrops on roses', help]
#print(f"my_favourite_things = {my_favourite_things}")

primes = [2, 3, 5, 7]
print(f"sum(primes) = {sum(primes)}")
print(f"max(primes) = {max(primes)}")
# list1 = primes(range(3)) fail
# print(f"primes(range(0,4,2)) = {list1}")


s = [9, 2, 3, 5, 7, 1, 6]
ss = sorted(s)
print(f"sorted(s) = {ss}")   # sorted(s) = [1, 2, 3, 5, 6, 7, 9]


x = 12
print(f"x.bit_length = {x.bit_length()}")  # x.bit_length = 4
print(f"bin(x) = {bin(x)}")                # bin(x) = 0b1100

squares = [n**2 for n in range(10)]
print(f"squares(range) = {squares}")   # squares(range) = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = []
for n in range(10):
    squares.append(n**2)
print(f"squares = {squares}")  # squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

