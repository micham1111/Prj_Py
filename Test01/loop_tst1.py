# Loop_Tst1.py  Last updated: 21_09_17

#range:
print("range(5):")
for i in range(5):
     print(i)     
print()

print("range(5,10):")
for i in range(5,10):
     print(i)     
print()


print("range(0,10,3):")
for i in range(0,10,3):
     print(i)     
print()

print("range(-10,-100,-30):")
for i in range(-10,-100,-30):
     print(i)     
print()


print(f"sum(range(4)) = {sum(range(4))}")    # 0 + 1 + 2 + 3
print()

for num in range(2, 8):
    if num % 2 == 0:
        print(f"Found an even number = {num}")
        continue
    print(f"Found a number = {num}")
print()

#While loop 
print("while > 0:")
n = 5
while (n > 0):
    if n == 2:
        break
    else:
        print(n)
        n = n - 1


i = 1
while i <= 10:
    # If a number is even don't print it
    if (i % 2) == 0:
        i += 1
        continue

    # If i equals 15 stop looping
    if i == 7:
        break

    # Print the odds
    print("Odd : ", i)
    # Increment i
    i += 1

