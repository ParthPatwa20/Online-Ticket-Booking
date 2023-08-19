import random
import os
import datetime
from PIL import Image, ImageDraw, ImageFont

def ticketGenrate():
    image = Image.new('RGB', (1920, 720), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial', size=45)

    os.system("Title ID CARD")
    list1 = ["Gomti Exp.", "Lichhwi Exp.", "Hamsafar Exp.", "Poorva Exp,.", "Janta Exp.", "Durnto Exp.", "Shatabdi Exp."]

    print('\n\nWe Require Some Details of you')


    (x, y) = (560, 50)

    title = 'Indian Railways Wishing You A Happy Journey'
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial', size=42)
    draw.text((x, y), title, fill=color, font=font)

    (x, y) = (700, 95)

    subtitle = 'This is online generated ticket'
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial', size=38)
    draw.text((x, y), subtitle, fill=color, font=font)

    (x, y) = (50, 250)
    idno = random.randint(1000, 9000)
    message = str('19220' + str(idno))
    color = 'rgb(0, 0, 0)' # black color
    font = ImageFont.truetype('arial', size=30)
    draw.text((x, y), 'PNR No. ' + message, fill=color, font=font)

    rdate = str(date.strftime("%d-%m-%Y %I:%M:%S %p"))
    color = 'rgb(0, 0, 0)'# black color
    (x, y) = (500, 250)
    draw.text((x, y), 'Reservation date-' + date.strftime("%d-%m-%Y %I:%M:%S %p"), fill=color, font=font)

    (x, y) = (50, 300)
    name = input('Enter Your Full Name: ')
    color = 'rgb(0, 0, 0)'# black color
    font = ImageFont.truetype('arial', size=30)
    draw.text((x, y), 'Name - ' + name, fill=color, font=font)

    (x, y) = (500, 300)
    jfrom = 'Mumbai'
    color = 'rgb(0, 0, 0)'# black color
    draw.text((x, y), "Journey from-"+jfrom, fill=color, font=font)

    (x, y) = (50, 350)
    Gender = input('Enter Your Gender: ')
    color = 'rgb(0, 0, 0)'# black color
    draw.text((x, y), 'Gender-' + Gender, fill=color, font=font)

    (x, y) = (500, 350)
    jto = input('Enter your destination : ')
    color = 'rgb(0, 0, 0)'# black color
    draw.text((x, y), 'Journey to-' +jto, fill=color, font=font)

    (x, y) = (50, 400)
    dob = input('Enter Your age: ')
    color = 'rgb(0, 0, 0)'# black color
    draw.text((x, y), 'Age-' + dob, fill=color, font=font)

    (x, y) = (500, 400)
    price = str(len(jto) * 35);
    color = 'rgb(0, 0, 0)'# black color
    draw.text((x, y), 'Fare-' + price, fill=color, font=font)

    (x, y) = (50, 450)
    bg = input('Enter Your Blood Group: ')
    color = 'rgb(255, 0, 0)'# black color
    draw.text((x, y), 'Blood Group-' + bg, fill=color, font=font)

    (x, y) = (500, 450)
    tno = str(len(jto) * 35 + idno);
    color = 'rgb(0, 0, 0)'# black color
    draw.text((x, y), 'Train No.-' + tno, fill=color, font=font)

    (x, y) = (50, 500)
    mob = input('Enter Your Mobile Number: ')
    color = 'rgb(0, 0, 0)'# black color
    draw.text((x, y), 'Mobile-' + mob, fill=color, font=font)

    (x, y) = (500, 500)
    tn = str(random.choice(list1));
    color = 'rgb(0, 0, 0)'# black color
    draw.text((x, y), 'Train Name.-' + tn, fill=color, font=font)

    (x, y) = (50, 550)
    cn = str(random.randint(11000, 91000))
    color = 'rgb(0, 0, 0)'# black color
    draw.text((x, y), 'Coach No.-' + cn, fill=color, font=font)

    (x, y) = (500, 550)
    sn = str(random.randint(10, 100))
    color = 'rgb(0, 0, 0)'# black color
    draw.text((x, y), 'Seat No.-' + sn, fill=color, font=font)

    (x, y) = (500, 600)
    doj = datetime.datetime.today() + datetime.timedelta(days=random.randint(5, 30))
    doj = str(doj.strftime("%d/%m/%Y%I:%M %p"))
    color = 'rgb(0, 0, 0)'# black color
    draw.text((x, y), 'Date & time of Journey.-' + doj, fill=color, font=font)

    (x, y) = (50, 600)
    Address = input('Enter Your Address: ')
    color = 'rgb(0, 0, 0)'# black color
    draw.text((x, y), 'Address-' + Address, fill=color, font=font)

    image.save(str(name) + '.png')

    til = Image.open(name + '.png')

    til.save(name + message + '.png')

    print('\nYour Ticket Successfully generated in a PNG file ' + name + message + '.png')
    img = Image.open(name + message + '.png')
    img.show()
    input('\nPress any key to main menu')# use input yo hold the screen

print("\n\nWelcome! To Ticket Booking System\n")
date = datetime.datetime.now()
formatdate = date.strftime("%d-%m-%Y\t\t\tTicket Reservation System\t\t\t%I:%M:%S %p")
print('***********************************************************************************')
print(formatdate)

restart = ('Y')
while restart != ('N', 'NO', 'n', 'no'):

    print("\n\n")
    print("1.Ticket Reservation")
    print("2.Exit")
    option = int(input("\nEnter your option : "))

    if option == 1:
        ticketGenrate()

    elif option == 0:
        exit()