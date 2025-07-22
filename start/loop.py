# loop

languages = ['Swift', 'Python', 'Go']

# access elements of the list one by one
for lang in languages:
    print(lang)


# ----
# iterate from i = 0 to i = 3
for i in range(0, 10):
    print(i)

# ----
for i in range(5):  
    print("😁🤩😄😅😅😅😅")

# wile loop

number = 1

while number <= 3:
    print(number)
    number = number + 1

# break-----
for i in range(5):
    if i == 3:
        break
    print(i)


# continue
for i in range(5):
    if i == 3:
        continue
    print(i)


