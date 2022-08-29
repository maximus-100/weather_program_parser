from tkinter import *
import requests
from datetime import datetime

key = '137d62f3c460fac41edca5930e84af7c'

parameters = {
    'appid': key,
    'units': 'metric',
    'lang': 'ru'
}


def get_weather():
    city = inp.get()
    print(city)
    parameters['q'] = city

    try:
        data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters).json()
        # pprint(data)
        temp = data['main']['temp']
        # print(temp)
        description = data['weather'][0]['description']
        wind = data['wind']['speed']

        timezone = data['timezone']

        sunrise = datetime.utcfromtimestamp(int(data['sys']['sunrise']) + int(timezone)).strftime('%H:%M:%S')
        sunset = datetime.utcfromtimestamp(int(data['sys']['sunset']) + int(timezone)).strftime('%H:%M:%S')
        text = f'''В городе {city} сейчас {description}
    Температура: {temp} °C
    Скорость ветра: {wind} м/с
    Сегодня рассвет в {sunrise}
    Закат в {sunset}
    '''
        print(text)
        lbl.configure(text=text)
    except:
        text = f'Вы ввели не корректный город {city}. Попробуйте снова'
        print(f'Вы ввели не корректный город {city}. Попробуйте снова')
        lbl.configure(text=text)


window = Tk()
window.geometry('500x400')
inp = Entry(window, width=50)
city = inp.get()
inp.grid(column=0, row=0)
btn = Button(window, text='Узнать погоду', command=get_weather)
btn.grid(column=1, row=0)

lbl = Label(window, text='')
lbl.grid(column=0, row=1)

window.mainloop()
