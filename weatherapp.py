from tkinter import *
from PIL import Image, ImageTk
import requests
import json
from tkinter import messagebox
import traceback
from io import BytesIO
from os import getcwd

#Creating main window
root = Tk()
root.title(" Weather Application")
root.geometry("400x400")
root.configure(bg="#0a1f44")
root.iconbitmap(r"C:\Users\user\OneDrive\Desktop\Python Projects\icon.ico")
ApiKey = "116ef70bdff1050eaac92c972d87a1ed"

def CurrentWeather(City_Name):
    global imgIcon , Temperature , description , Country, icon
    url2 = f"http://api.openweathermap.org/geo/1.0/direct?q={City_Name}&limit=&appid={ApiKey}" #Api to retrieve lat lon
    req = requests.get(url2)
    data = req.text
    json_load = (json.loads(data))

    lat = json_load[0]["lat"]
    lon = json_load[0]["lon"]

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={ApiKey}&units=metric' #Api to retrieve info
    req = requests.get(url)
    data = req.text
    json_load = (json.loads(data))
    for items in json_load['weather']:
        description = items['description']
        icon = items['icon']
    Temperature = round(json_load['main']['temp'],1)
    Country = json_load['sys']['country']
    url2 = f'http://openweathermap.org/img/w/{icon}.png' #url of weather ocpn
    #GetDir = getcwd()            #Gets the current working directory of process
    GetDir = r"C:\Users\user\OneDrive\Desktop\Python Projects"
    response = requests.get(url2)
    with Image.open(BytesIO(response.content)) as im:
        filepath = GetDir + icon + ".png"
        
        im.save(filepath)

    img = Image.open(filepath)
    new_img = img.resize((100,100)) #resized the weather icon
    imgIcon = ImageTk.PhotoImage(new_img)

    return Temperature , description ,City_Name , Country


#Displays the weather info
def ShowInfo():
    global MyLabel , MyFrame
    MyLabel.grid_forget()
    MyFrame.grid_forget()

    try:
        MyFrame = LabelFrame(root)
        MyFrame.grid(row=3, column =1,columnspan=3)
        Display = CurrentWeather(CityBox.get())
        MyLabel = Label(MyFrame,text=CityBox.get().capitalize() + " , "+ Country, font="Times 20 bold")  #City and Country label
        MyLabel.grid(row= 0 , column= 1 , columnspan=3, pady=10 ,padx=10)
        MyLabel2 = Label(MyFrame, text= str(round(Temperature)) + "°C", font = "Helvetica 20 bold") #Temperature
        MyLabel2.grid(row=2, column=1 ,columnspan=3,pady= 10 , padx=10)
        ImgLabel = Label(MyFrame,image=imgIcon)                                                     #Image
        ImgLabel.grid(row=4, column=1,columnspan=3,pady=10, padx=10)
        MyLabel3 = Label(MyFrame, text= description.capitalize(), font="Times 20 bold")             #Description
        MyLabel3.grid(row=6, column=1 , columnspan=3,pady=10, padx=10)

    except IndexError as err:
        messagebox.showerror("Error", "City Name is incorrect or doesnt exist")


#Creating the search box
CityBox = Entry(root,width=40)
CityBox.insert(0,"Enter the City name")
CityBox.grid(row=2, column=1, ipadx=20, sticky=W,columnspan=2,pady=20,ipady=5,padx=10)
CityBox.configure(state=DISABLED)

#to apply the place holder when app open
def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')

#to apply  the placeholder on foucs out
def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')

x_focus_in = CityBox.bind('<Button-1>', lambda x: on_focus_in(CityBox))
x_focus_out = CityBox.bind(
    '<FocusOut>', lambda x: on_focus_out(CityBox, "Enter the City name"))


MyLabel = Label(root) #so that it is referenced before showinfo
MyFrame = LabelFrame(root) #so that it is referenced before showinfo

#Creating the submit
Sumbit_Button = Button(root, text="Submit", command= ShowInfo,padx=10,pady=4,bg="#ff1e42",fg="#f1f1f1",font="Helvetica 9 bold")
Sumbit_Button.grid(row=2, column=3,ipadx=10)


root.mainloop()
