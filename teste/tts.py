import pyttsx3
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice',voices[-2].id)

engine.say("acabou a água, toma banho de leite")
engine.runAndWait()