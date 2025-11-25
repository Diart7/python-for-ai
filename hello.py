string="My name is Dave"

first_name="Dave"
last_name="Ebbelar"

full_name= first_name + "" + last_name

long_dash = "-"*10

print(full_name)
print(long_dash)
len(first_name)

age=16

can_vote= age>=18

print()
age=25
has_license=True
drunk=False
can_drive= age>=16 and has_license and not drunk

print(can_drive)

score=10
score +=5

name="Dave"
string=f"Hi there my name is {name}!"
name.lower()
name.upper()
sentence ="hi my name is Dave"

temperature=26
if temperature>30:
    print("its very hot outside")
elif temperature>25:
    print("its hot outside")
else:
    print("its not that hot outside")

has_ticket=True
age=15

if has_ticket:
    if age>=18:
        print("you can enter the cinema")
    else:
        print("you are too young to enter the cinema")
else:
    print("Please buy a ticket")

for i in range(5):
    print("Hello World")

for i in range(1,6):
    print(i)

for i in range(2,11,2):
    print(i)

age1=25
has_license1=False
my_list=["Allice",25,age1,True,has_license1]

name1=my_list[0]
age1=my_list[1]
has_license1=my_list[-1]

my_list[0]="Bob"
my_list.append("New Item")
my_list.remove("Bob")

# proper insert example:
my_list.insert(1, "Bob")

# dictionary
person={
    "name2":"Dave",
    "age2":30,
    "city":"New York"
}

person["name2"]="David"
person["license"]=True
del person["age2"]

person1={"name3":"Dabe","age3":30,"city3":"New York"}

print(person1.keys())
print(person1.values())
print(person1.items())

if "name3" in person1:
    print("Name found")

person1.update({"age3":31,"job":"Engineer"})

empty=()
point=(3,5)
colors=("red","green","blue")

empty_set=set()

fruits=set(["apple","banana","orange"])
scores=[85,90,85,90]
unique_scores=set(scores)

print(unique_scores)

def greet():
    print("Hello")

greet()
greet()

def check_weather():
    temperature1=28
    if temperature1>25:
        print("Its hot ")
    else:
        print("Its not that hot")

check_weather()

def greet3(first_name5,last_name5="Nika"):
    print(f"Hello {first_name5} {last_name5}")

greet3(first_name5="Dave",last_name5="Ebbelar")
greet3("Alice","Smith")

def calculate_total(price, tax_rate, discount):
   tax_rate=0.1
   discount=5
   tax=price*tax_rate
   final_price=price+tax-discount
   print(f"Total: ${final_price}")

def add_print(c,d):
    print(c+d)

add_print(5,10)

def add_return(c,d):
    return c+d

result1=add_return(5,10)
result1+5

def calculate_area(width,height):
    area=width*height
    area=area*1.1
    return area

room_area=calculate_area(10,12)
print(f"Room size: {room_area}sq ft")

def double(number):
    return number*2

result=double(5)
total3=double(5)+double(3)

print(double(10))

if double(3)>10:
    print("Big number")

def simple_function():
    numbers=[1,2,3,4,5]
    first_number=numbers[0]
    last_number=numbers[-1]
    return first_number,last_number

f,l=simple_function()

print(f)
print(l)

from math import sqrt,pi
sqrt(16)

import random

number = random.randint(1,10)
choice = random.choice(["rock","paper","scissors"])

import json
data='{"name7":"Dave7","age7":30,"city7":"New York"}'
person7=json.loads(data)
print(person7["name7"])

import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")

from datetime import datetime, timedelta

today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)