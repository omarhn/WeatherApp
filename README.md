# WeatherApp
A Weather Application


## Video Demo: https://youtu.be/bqxUQZvGvoU

## Description: This is a weather applicaiton created using python. 



We are using the **openweathermap** api to retrieve all the weather information that the applicaton is gonna use.



the tkinter library is used to create the user interface for the application and Pillow for creating the weather icons to be displayed



*full list of libraries used is below:* 

```
from tkinter import *
from PIL import Image, ImageTk
import requests
import json
from tkinter import messagebox
from io import BytesIO

```



The **request** libary in python is used to make a call to the API and retrieve the *Longitude* and the *latitude* of the city we just entered.


Using the *Longitude* and *latitude* we make another call to the api to retrieve the temperature, a description of the weather, the country and an icon of the weather, the icon is saved in the same repository. All of this -is returned after the funcition is exectued. 


Afterwards, using the **Tkinter** libary in python We created a simple ui to display the information in a more user-friendly way. The UI consists of a window with a search bar in which you input the name of the city  and a -search button to execute the search. If the name of the city is correct a frame appears which has four labels attached in a column. The name of the place, the temperature , image and a small description.


[Example](https://github.com/omarhn/WeatherApp/assets/80461981/c2df65cd-b477-4a95-ba73-3d05353c0476)

If the name of the city is incorrect a pop-up window appears with an error message 
>City name is incorrect or doesnt exist !







