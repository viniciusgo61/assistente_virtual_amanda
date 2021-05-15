#Programa principal

import speech_recognition as sr

# Criar um reconhecedor
r=sr.Recognizar()

#Abrir o microfone para captura
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) # Define mic como fonte de áudio
        print(r.recognize_google(audio, language='pt')) # reconhecendo com o google em portugês
       
