import tkinter as tk
import requests
from PIL import Image,ImageTk 

root=tk.Tk()

root.title("Weather App")
root.geometry("600x500")



#52c5cb08987025ad8043607c8078b0db
#https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
def format_response(weather):
    try:
        city=weather['name']
        condition=weather['weather'][0]['description']
        temp=weather['main']['temp']
        temp_c = (temp - 32) * 5/9
        final_str = 'City: {}\nCondition: {}\nTemperature: {:.1f}°F / {:.1f}°C'.format(city, condition, temp, temp_c)
    except:
        final_str='There was a problem retrieving that information'
    return final_str



def get_weather(city):
    weather_keys = '52c5cb08987025ad8043607c8078b0db'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_keys, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params)
    weather = response.json()
   
    if 'weather' not in weather:
        print(f"Error: Missing 'weather' key in response: {weather}")
        return
    
    result['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size=int(frame_two.winfo_height()*0.25)
    img=ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size,size)))   
    weather_icon.delete('all')
    weather_icon.create_image(0,0,anchor='nw',image=img)
    weather_icon.image=img



img=Image.open('./bg.jpg')
img = img.resize((600, 500), Image.Resampling.LANCZOS)
img_photo=ImageTk.PhotoImage(img)

bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

heading_title=tk.Label(bg_lbl,text="Current weather information of over 2,00,000 cities!",font=('times new roman',18,'bold'),fg='white',bg='#964B00')
heading_title.place(x=30,y=18)
frame_one=tk.Frame(bg_lbl,bg="#F5DEB3",bd=5)
frame_one.place(x=80,y=50,width=450,height=50)

txt_box=tk.Entry(frame_one,font=('times new roman',25),width=17)
txt_box.grid(row=0,column=0,sticky='w')

btn=tk.Button(frame_one,text='Get Weather',fg='black',font=('times new roman',16,'bold'),command=lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=10)


frame_two=tk. Frame(bg_lbl,bg="#F5DEB3" , bd=5)
frame_two.place(x=80,y=130, width=450, height=300)


result=tk. Label(frame_two, font=40, bg= 'white',justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)

weather_icon=tk.Canvas(result,bg='white',bd=0, highlightthickness=0)
weather_icon.place(relx=.75,rely=0, relwidth=1, relheight=0.5)



root.mainloop()