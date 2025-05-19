#  Voice Assistant for WhatsApp Automation

This is a simple desktop voice assistant built with Python. It uses voice commands to automate sending WhatsApp messages via WhatsApp Web using Selenium and Chrome. The assistant can also speak responses using `pyttsx3`.

##  Features

- Voice-based interaction using `speech_recognition`
- Text-to-speech using `pyttsx3`
- WhatsApp message automation via Selenium
- Easy to use via GUI or CLI
- Packaged into `.exe` for easy sharing

##  Requirements

Install dependencies from `requirements.txt`:

pip install -r requirements.txt

## Summary:
- iOS cannot run Selenium or ChromeDriver, making your current automation code incompatible.
- WhatsApp Desktop app lacks APIs and automation hooks for programmatically sending messages.

CAN BE ONLY RUN ON Desktop and whatsapp web.

FUTURE SCOPE:
Add direct contact list so that no need to say long numbers.
