import cv2
import numpy as np
import pyautogui as pg
import webbrowser
from time import sleep
import speech_recognition
import unidecode





def recognize_voice():
    recognizer = speech_recognition.Recognizer()
    speech_to_txt = ""
    with speech_recognition.Microphone() as src:
        try:
            audio = recognizer.adjust_for_ambient_noise(src)
            print("Threshold Value After calibration:" + str(recognizer.energy_threshold))
            print("Please speak:")
            audio = recognizer.listen(src)
            speech_to_txt = recognizer.recognize_google(audio_data = audio, language ="pt-BR").lower()
        except Exception as ex:
            print("Sorry. Could not understand.")
    return speech_to_txt

def nlp(speech):
    if "like" in speech or "gostei" in speech or "gostar" in speech:
        # move to center of screen and double click
        pg.moveTo(center_x, center_y)
        pg.doubleClick()
        return "like"
        
    elif "pula" in speech or "pular" in speech or "próximo" in speech or "próxima" in speech:
        # move to center of screen and scroll down
        pg.moveTo(center_x, center_y)
        pg.scroll(-1000)
        return "pular"


    elif "volta" in speech or "voltar" in speech or "anterior" in speech or "antes" in speech:
        # move to center of screen and scroll up
        pg.moveTo(center_x, center_y)
        pg.scroll(1000)
        return "voltar"

    elif "seguir" in speech:
        # detect follow button and click it
        follow = pg.locateOnScreen('follow.png', confidence=0.5)
        fx, fy = pg.center(follow)
        pg.click(fx, fy)
        return "seguir"
    
    elif "comentar" in speech:
        # detect comment button and click it
        comment_x, comment_y = x/1.4, y/1.075
        send_x, send_y = x/1.05, y/1.075
        pg.click(comment_x, comment_y)

        # type comment
        comment = speech.replace("comentar", "")
        comment = unidecode.unidecode(comment)
        pg.write(comment, interval=0.1)

        pg.click(send_x, send_y)
        return "comentar"

    elif "sair" in speech:
        print("sair")
        return False
# take a screenshot to store locally
#screenshot = pg.screenshot('screenshot.png')

# open tik tok in a web browser
webbrowser.open('https://www.tiktok.com/')

sleep(5)

# take a screenshot to locate objects on
screenshot = pg.screenshot()

# locate center and click
x,y = screenshot._size
center_x,center_y = x/2, y/2
pg.click(center_x, center_y)

sleep(2)

# adjust colors
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

while True:

    #sleep(0.5)

    # get user speech
    speech = recognize_voice()
    print(speech)

    action = nlp(speech)
    print(action)

    if action == False:
        break



# clean up windows
cv2.destroyAllWindows()