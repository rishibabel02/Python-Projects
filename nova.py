import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia 
import webbrowser 
import os
import smtplib
import json
import requests
import random
import platform
# import socket 
# import psutil
# import pyautogui

# from forex_python.converter import CurrecnyRates
engine = pyttsx3.init('sapi5')  #sapi5 is used to take windows inbuilt voice via an api.
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)  #voice 1 is for female (there are 2 inbuilt voices)
# print(voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() # used to stop the engine after speaking once 

def WishMe():
    hour = int(datetime.datetime.now().hour) 
    # speak("Enter Your Name:")
    name = input("Enter Your Name: ")

    if hour >=0 and hour < 12:
        speak(f"Good Morning {name}")
    elif hour>=12 and hour<=18:
        speak(f"Good Afternoon {name}")
    else:
        speak(f"Good Evening {name}")
    speak(" I am nova , Your Personal Assistant , How may I help you ?")

    engine.setProperty('rate', 150)  # Adjust the rate as needed
    # engine.setProperty('voice', voices[1].id)  # Assuming the first voice is an Indian accent


def takecommand():
    '''It takes microphone input and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # by default it is 0.8 but we have increased it to 1 
        # pause threshold = seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold = 100 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")
    
    except Exception as e:
        print(f"Error:{e}")
        print("I didn't hear... Please Say that again!")
        speak("I didn't hear... Please Say that again!")
        return "None"  #returning a none string 
    return query

def sendEmail(to , content):
    app_password = "tenq dmfc ctzd omcp"
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login('rishi.babel4@gmail.com' , app_password)
    server.sendmail('rishi.babel4@gmail.com', to , content)
    server.close()

def setAlarm(alarm_time):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    while current_time != alarm_time:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
    
    print("Alarm Ringing")
    speak("It's time to wake up! , Hope you had a nice sleep")

def weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=d37b0c9e5d784503a0b142701240403&q={city}"
    r = requests.get(url)
    w_dict = json.loads(r.text)
    w = w_dict["current"]["temp_c"]
    print(f"The current weather in {city} is {w} degrees")
    speak(f"The current weather in {city} is {w} degrees")
   
def tell_jokes():
    url = "https://v2.jokeapi.dev/joke/Programming"
    response = requests.get(url)
    joke_data = json.loads(response.text)

    if joke_data["type"] == "twopart":
        joke = f"{joke_data['setup']} {joke_data['delivery']}"
    else:
        joke = joke_data["joke"]

    print(joke)
    speak(joke)

def news(api):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api}"
    response = requests.get(url) 
    news_data = json.loads(response.text)

    if news_data["status"] == "ok" and news_data["totalResults"]>0:
        articles = news_data["articles"][:3]
        speak("Today's Headlines are:")
        for index , article in enumerate(articles):
            title = article["title"]
            print(f"News{index+1}:{ title}")
            speak(f"News{index+1}:{ title}")

    else:
        speak("Sorry There was some error fetching the news")

def system_info():
    info = f"System Information:\n"
    info += f"Operating System: {platform.system()} {platform.version()}\n"
    info += f"Processor: {platform.processor()}\n"
    # info +=f"Machine: {platform.machine}\n"

    print(info)
    speak(info)


def games():
    print("\n1.Tic Tac Toe \n2.Stone Paper Scissors \n3.Guess name \n4.Encode-Decode \n5.Secret auction)?")
    speak("Which Game do you want to play")
    choice = takecommand().lower()

    # if 'tac' in choice or 'tic' in choice or 'toe' in choice:
    #     import tic_tac

    # elif 'stone' in choice or 'paper' in choice or'scissor' in choice:
    #     import stone_paper_scissor

    # elif 'name' in choice:
    #     import guess

    # elif 'encode' in choice or 'decode' in choice:
    #     import encode_decode
    
    # elif 'secret' in choice or 'auction' in choice:
    #     import secret_auction
       
    # else:
    #     print("Invalid choice.")
    #     speak("Invalid choice.")

def dice():
    while(True):
        number = random.randint(1,6)
        print("The number is ",number)
        speak(f"The number is {number}")
        speak("Do you want to roll the dice again (yes/no)?\n")
        another_roll = takecommand().lower()
        if another_roll =='yes':
            continue
        else:
            break
    

#battery percentage
# def get_battery_percentage():
#     battery = psutil.sensors_battery()
#     percent = battery.percent
#     return percent
# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

#translator 
# from googletrans import Translator
# def translate_text(text, dest_language='hi'):
#     translator = Translator()
#     translated_text = translator.translate(text, dest=dest_language)
#     return translated_text.text
# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()


# #conversion of dollars to rupees
# def convert_usd_to_inr(amount, exchange_rate=83.30):
#     converted_amount = amount * exchange_rate
#     return converted_amount

# # def speak(text):
# #     engine = pyttsx3.init()
# #     engine.say(text)
# #     engine.runAndWait()


# #screenshot
# def take_screenshot():
#     # Capture the screen and save the screenshot
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     screenshot_path = r"C:\Users\teesh\OneDrive\Pictures\Screenshots"
#     screenshot_name = f"screenshot_{timestamp}.png"
#     pyautogui.screenshot(screenshot_name)
#     print(f"Screenshot saved as {screenshot_name} in your library.")


# def increase_volume():
#     pyautogui.press('volumeup')
#     speak("Volume increased")

# def decrease_volume():
#     pyautogui.press('volumedown')
    speak("Volume decreased")



if __name__ =='__main__':
   api = "de3ddc4e46954483a499a7bee92ff76b"
   
   WishMe()
   
   while True:
   
    query = takecommand().lower()

    #code for executing tasks based on query.
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query  = query.replace("Wikipedia" ,"")
        results = wikipedia.summary(query , sentences = 2)  #it wiwll return 2 sentences
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open geeksforgeeks' in query:
        webbrowser.open("geeksforgeeks.org")

    elif 'play music' in query:
        music_sifra = 'D:\\songs_nova'
        songs = os.listdir(music_sifra) #lists all the songs
        print(songs)
        os.startfile(os.path.join(music_sifra , songs[0]))

    elif 'time' in query:
        Time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {Time}")
        print(f"The time is {Time}")


    elif 'email to rishi' in query:
        
        try:
            speak("What Should I Say?")
            content = takecommand()
            to = "rishibabel02@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("Sorry my friend rishi . I am unable to send this email")

    elif 'alarm' in query:
        print("Please specify the time for the alarm in 24-hour format, for example, 'Set alarm for 08:00:00'.")
        speak("Please specify the time for the alarm in 24-hour format, for example, 'Set alarm for 08:00:00'.")
        alarm_time = input("Specify alarm time (HH:MM:SS): ")
        setAlarm(alarm_time)

    elif 'weather' in query:
        speak("Enter the city")
        city = input("Enter the city: ")
        weather(city)

    elif 'joke' in query:
        tell_jokes()

    elif 'news' in query:
        news(api)

    elif 'system info' in query:
        system_info()

    elif 'game' in query:
        games()
    
    elif 'dice' in query:
        dice()


    # elif 'battery' in query:
    #     battery_percent = get_battery_percentage()
    #     speak(f"Your current battery percentage is {battery_percent} percent.")

    # elif 'translate' in query:
    #     speak("Please say the English text to translate to Hindi.")
    #     text_to_translate = takecommand()
    #     if text_to_translate:
    #         translated_text = translate_text(text_to_translate)
    #         print(f"The translated text in Hindi is: {translated_text}")
    #         speak(f"The translated text in Hindi is: {translated_text}")

    # elif 'convert' in query:
    #         speak("Please write amount in USD")
    #         amount_text = float(input("Amount= "))
    #         if amount_text:
    #             try:
    #                 converted_amount = convert_usd_to_inr(amount_text)
    #                 speak(f"{amount_text} US dollars is equal to {converted_amount:.2f} Indian rupees.")
    #             except ValueError:
    #                 print("Please enter a valid amount.")
            
    # elif 'screenshot' in query:
    #     input("Press Enter to take a screenshot...")
    #     take_screenshot()


    # elif 'increase volume' in query:
    #         increase_volume()
    # elif 'decrease volume' in query:
    #         decrease_volume()

    elif 'stop' in query:
        exit()

    
   
