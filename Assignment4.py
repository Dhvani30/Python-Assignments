# Break
for num in range(1, 6):
    if num == 3:
        print("Break")
        break
    print(num)
else:
    print("without break statement")

# Pass
for l in 'Dhvani':
    if l == 'i':
        pass
    print(l)
else:
    print("Loop completed")

# Continue
for num in range(1, 10):
    if num == 9:
        print("Skipping the iteration")
        continue
    print(num)
else:
    print("Loop completed")

# For...with else
for num in range(1, 6):
    print(num)
else:
    print("Loop completed")

# While...with else
count = 0
while count <= 5:
    print(count)
    count += 1
else:
    print("Loop completed")
