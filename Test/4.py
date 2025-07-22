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


# problem 3
import re

def checkDigitsInName(name):
    if type(name) is str:
        if re.search(r'\d', name):
            return True
        else:
            return False
    else:
        return "Invalid Input"
pro3 = checkDigitsInName("myname55")
print(pro3)


# problem 4
def  calculateFinalScore(obj):
    if type(obj['name']) is str and isinstance(obj["testScore"], (int, float)) and isinstance(obj["schoolGrade"], (int, float)) :
        # set variable
        Profession = 0;
        TestScore = obj["testScore"];
        IsFFamily = obj["isFFamily"];
        SchoolGrade = obj["schoolGrade"];

        # cake is father farmer
        if type(IsFFamily) == bool:
            Profession = 20;
        else :
            Profession = 0;

        # sum the data
        sum = Profession + TestScore + SchoolGrade

        # print the number
        print(Profession,TestScore,SchoolGrade,IsFFamily)

        if (sum >= 80) :
            return True
        else :
            return False
    else: 
        return "Invalid Input"
pro4 = calculateFinalScore({ "name": "Rajib", "testScore": 45, "schoolGrade": 5,"isFFamily" : True })
print(pro4)

# problem 5
def waitingTime(waitingTimes , serialNumber):
    if len(waitingTimes) and isinstance(serialNumber, (int, float)):
        # set variable
        Time = waitingTimes
        Serial = serialNumber - 1
        interviewer = len(Time)

        total_sum = sum(Time)
        average = total_sum / interviewer
        print(total_sum,average)

        netPeople =  Serial - interviewer
        netTime = netPeople*average

        return netTime
    else :
        return "Invalid Input"
WaitingTime = waitingTime([13, 2], 6 )
print(WaitingTime)    



