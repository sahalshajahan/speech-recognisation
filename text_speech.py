import pyttsx3
txt_sp=pyttsx3.init()# creates an object using init class()
text=input('enter your text.....\n')
voices=txt_sp.getProperty('voices')
for voice in voices:
    print("ID:",voice.id)
txt_sp.setProperty('voice',voices[1].id)
txt_sp.say(text) #say function is inside the init function and is used to say the text
txt_sp.runAndWait() 