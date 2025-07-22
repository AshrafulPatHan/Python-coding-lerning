#  python3 4.py
print("""
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
""")

# problem 1

def calculateTax(income,expenses):
    if (income < expenses ):
        return "Invalid Input"
    elif(income <= 0):
        return "Invalid Input"
    elif(expenses <= 0):
        return "Invalid Input" 
    def sum(income,expenses):
        Deferent = income - expenses
        Tax = Deferent*.20
        return Tax
    return sum(income,expenses)
    
pro1 = calculateTax( 10000,3000 )
print(pro1)

# problem 2

def sendNotication(email):
    if "@" in email :
        if "." in email :
            array = email.split("@");
            name = array[0]
            web = array[1]
            data = name + " sent you an email from " + web
            return data
        else:
            return "Invalid Email"
    else :
        return "Invalid Email"

pro2 = sendNotication("ash@gmail.com")
print(pro2)
