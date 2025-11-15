'''
print("################ SALARY CALCULATION SYSTEM ##################################")
def empolyeenetsalary():
    netsal=0
    name=input("enter your name:")
    basicsal=int(input("enter the your basic salary:"))
    taxpercent=int(input("enter the tax percentage:"))
    taxdeduction=(basicsal)*(taxpercent/100)
    netsal=basicsal-taxdeduction
    return f"Hi,{name},your net salary is: {netsal}"
print(empolyeenetsalary())
#net salary after the tax deduatio
registeredUsers=[{"name":"vamsi","email":"vamsi@gmail.com","password":"1234"}]
def logout():
    print("you want to logout from the website")
def register():
    r_name=input("enter register name :-- ")
    r_email=input("enter register email :-- ")
    r_p=input("enter register password :-- ")
    r_c_p=input("enter registred confirm password")
    if r_p == r_c_p:
        registeredUsers.append({"name":r_name,"email":r_email,"password":r_p})
        print("registration done successfully.....")
        login()
    else:
        print("enter password and confirm password both same")
def login():
    l_email=input("enter login name :--  ")
    l_password=input("enter login pssword :-- ")
    for i in registeredUsers:
        if i["email"]==l_email and i["password"]==l_password:
            print("login successfully done....")
            dashboard()
        else:
            print("invalid credentials")
def notes():
    print("this is your notes book panel")
def attendance():
    print("yoyr attendance is 100%")
def projects():
    print("this is the project workplace")
def assignments():
    print("this is the assignments document")
    print("what is python?")
    ans=input("enter the answer of the what is the python")
    if ans=="interpreted language" or ans=="highlevelllanguage" or ans=="stronglytypedlanguage":
        print("your answer is correct")
    else:
        print("your answer is wrong please try again")
        assignments()
def dashboard():
    print(f"welcome the dashboard{"name"}")
    print("explore all features")
    assignments()
    projects()
    notes()
    attedance()
while True:
    print("1. register...")
    print("2. login....")
    print("3. logut")
    yrOption=int(input("enter yr choice from 1 r 2 r 3 :---  ")) #1 # 3
    if yrOption==1:
        register()
    if yrOption==2:
        login()
    if yrOption==3:
        logout()
        break
print()
def calculatetemperature():
    a=float(input("enter the temperatur value in the format of the celsius value"))
    a=str(a)
    print(a)
    a=int(a)
    franheit=(a*9/5)+32
    franheit=str(franheit)+"f"
    return franheit
print(calculatetemperature())
def billgeneration(i,q,d):
    billamount=0
    if i in d:
        gst=2
        billamount=billamount+(d[i]*q)+gst    
    else:
        print("your item not available in my market")
    print(f"your billamount is{billamount}")
print("prices of the kitchen tools/equipment as shown below")
print("this price of the kitchen tools/equipment on 1kg")
dailyneededitems= {
    "Eggs (6-pack)": 60,
    "Sunflower Oil (1L)": 130,
    "Groundnut Oil (1L)": 160,
    "Mustard Oil (500ml)": 90,
    "Ghee (500ml)": 280,
    "Salt (1kg)": 25,
    "Turmeric Powder (200g)":40,
    "Red Chili Powder (200g)": 60,
    "Coriander Powder (200g)": 55,
    "Garam Masala (100g)": 65,
    "Chicken Masala (100g)": 70,
    "Meat Masala (100g)": 75,
    "Pepper Powder (100g)": 85,
    "Cumin Seeds (Jeera, 100g)": 45,
    "Mustard Seeds (100g)": 30,
    "Bay Leaves (50g)": 25,
    "Cloves (50g)": 60,
    "Cinnamon Sticks (50g)": 55,
    "Cardamom (50g)": 120,
    "Kasuri Methi (50g)": 35,
    "Colgate Strong Teeth (100g)": 55,
    "Colgate MaxFresh Gel (150g)": 95,
    "Patanjali Dant Kanti (100g)": 45,
    "Close-Up Red Hot Gel (150g)": 65,
    "Sensodyne Fresh Mint (100g)": 120,
    "Pepsodent Germicheck (150g)": 70,
    "Himalaya Complete Care (150g)": 90,
    "Colgate ZigZag (Soft)": 25,
    "Oral-B All-Rounder (Medium)": 30,
    "Patanjali Herbal Toothbrush": 20,
    "Sensodyne Sensitive Brush (Soft)": 55,
    "Pepsodent Germi Check Brush": 25,
    "Himalaya Soft Toothbrush": 38
}'''
import random 
def billgeneration(n):
    for i in range(1,n+1,1):
        item=input("enter the kitchen tools/equipment name what you want")
        price=random.randint(10,100)
        quantatity=int(input("enter in the how many you can2"))
        gst=random.randint(1,10)
        totalbillamount=billamount+price*quantatity+gst
    print(f"enter the {item} price and total bill amount{totalbillamount}")
billamount=0
noofitems=int(input("enter the number of the items"))
billgeneration(noofitems)




 

