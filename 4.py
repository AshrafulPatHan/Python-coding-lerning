# python 4.py
print("Hello World")

a = 2
b = 3
c = 4.2
d = -5
result = a + b 

print(result)

def show_equal(): 
    print(str(10) + " This is the equal")

show_equal()
# ----

print(type(d))

# ---------
number = 10
string = "Hello"

def Condition(num):
	if num == 10:
		print("The number is macth 😀")

Condition(number)

def ChakString (lster):
	if lster == "Hello":
		print("The Leter is macth 😀")
	elif isinstance(lster, str) :
		print("The Leter is not macth 😭")
	else :
		print("The is not Leter 😭")

ChakString(string)

# ---------
languages = ['Swift', 'Python', 'Go']

# access elements of the list one by one
for lang in languages:
    print(lang)

# ---------
number = 1

while number <= 3:
    print(number)
    number = number + 1
# --------



hello = "hello"
cod = 125
print(f"this is {hello}")


