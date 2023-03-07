import tkinter as tk
import phonenumbers
from phonenumbers import geocoder

def tracker():
    #Tracking Phone number loaction
    number = box1.get()
    ch_number = phonenumbers.parse(number,"CH")
    location.set(geocoder.description_for_number(ch_number,"en"))
    #Service provider of given phone number
    from phonenumbers import carrier
    service_nmber = phonenumbers.parse(number, "RO")
    serviceProvider.set(carrier.name_for_number(service_nmber, "en"))  

def reset():
    box1.delete(0,tk.END)
    
app = tk.Tk()  #for making application we will use app keyword
app.title("Number Tracker")
app.geometry("500x500")  #for deciding dimension
app.resizable(False,False)

location = tk.StringVar()
location.set("")
serviceProvider = tk.StringVar()
serviceProvider.set("")

label1 = tk.Label(app, text="Phone Number :", font=("Arial",15))
label1.place(x=20, y=20)
label2 = tk.Label(app, text="Location :", font=("Arial",15))
label2.place(x=20, y=80)
label3 = tk.Label(app, text="Service Provider :", font=("Arial",15))
label3.place(x=20, y=140)

box1 = tk.Entry(app, font=("Arial,25"))
box1.place(x=200, y=20) 
box2 = tk.Entry(app, font=("Arial,25"))
box2 = tk.Label(app, textvariable=location, font=("Arial,25"))
box2.place(x=200, y=80) 
box3 = tk.Entry(app, font=("Arial,25"))
box3 = tk.Label(app, textvariable=serviceProvider, font=("Arial,25"))
box3.place(x=200, y=140) 

button1 = tk.Button(app, text="Trace",font=("Arial,25"), bg = "bisque", command=tracker)
button1.place(x=200,y=200,width=80)
button2 = tk.Button(app, text="Reset",font=("Arial,25"), bg = "bisque",command=reset)
button2.place(x=300,y=200,width=80)

app.mainloop()