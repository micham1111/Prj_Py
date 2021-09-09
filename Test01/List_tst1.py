# List_Tst01.txt  Last updated: 

#List
l = [1,2,3,4,5]
print(l)
print(l[2])



planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(f"len(planets) = {len(planets)}")
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
print(f"hands = {hands}")

my_favourite_things = [32, 'raindrops on roses', help]
print(f"my_favourite_things = {my_favourite_things}")

primes = [2, 3, 5, 7]
print(f"sum(primes) = {sum(primes)}")
print(f"max(primes) = {max(primes)}")
list1 = primes(range(3))
print(f"primes(range(0,4,2)) = {list1}")


s = [9, 2, 3, 5, 7, 1, 6]
ss = sorted(s)
print(f"sorted(s) = {ss}")


x = 12
print(f"x.bit_length = {x.bit_length()}")
print(f"bin(x) = {bin(x)}")

squares = [n**2 for n in range(10)]
print(f"squares(range) = {squares}")

squares = []
for n in range(10):
    squares.append(n**2)
print(f"squares = {squares}")

