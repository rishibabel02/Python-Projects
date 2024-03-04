import pyttsx3  # used to achieve text to speech functionality in windows



if __name__ == '__main__':
    print("Welcome to Rishi's speaker 1.01 ")
    x = input("Enter what you want me to pronounce:\n")
    # initialise the text -to -speech engine
    engine = pyttsx3.init()

    engine.say(x)
    engine.runAndWait()
    