import speech_recognition as sr
import pyttsx3
import time
import urllib.parse
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

engine = pyttsx3.init()

def speak(text):
    print(f"ABBY: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f" You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Network error.")
            return ""

def send_whatsapp_message_selenium(phone_number, message):
    try:
        options = webdriver.ChromeOptions()
        # Removed user-data-dir to avoid session persistence
        driver = webdriver.Chrome(options=options)
        driver.get("https://web.whatsapp.com")
        speak("Please scan the QR code on WhatsApp Web.")
        time.sleep(20)  # Time for user to scan QR code

        digits = ''.join(filter(str.isdigit, phone_number))
        url = f"https://web.whatsapp.com/send?phone={digits}&text={urllib.parse.quote(message)}"
        driver.get(url)

        time.sleep(10)  # Wait for chat to load
        send_button_xpath = '//button[@data-testid="compose-btn-send"]'
        send_button = driver.find_element(By.XPATH, send_button_xpath)
        send_button.click()

        speak(f"WhatsApp message sent to {phone_number}")
        time.sleep(5)
        driver.quit()
    except Exception as e:
        speak(f"Failed to send WhatsApp message: {e}")


def perform_task(command):
    if "send whatsapp" in command:
        match = re.search(r'to ([\+\d\s-]+) saying (.+)', command)
        if not match:
            speak("Please say the command as: send whatsapp message to [number] saying [message]")
            return
        phone = match.group(1)
        message = match.group(2)
        send_whatsapp_message_selenium(phone, message)
    elif command:
        speak("Sorry, I don't recognize that command yet.")

def main():

    speak("Hello! You can say commands like 'send whatsapp message to number saying text .Say 'exit' to quit.")

    while True:
        command = listen_command()
        if not command:
            continue
        if command in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break
        perform_task(command)

if __name__ == "__main__":
    main()
