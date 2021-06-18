import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',125)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<18:
		speak("Good Morning!")
	elif hour>=12 and hour <4:
		speak("Good Afternoon!")
	else:
		speak("Good Evening!")
	speak("I am Shinigami created by Abhinav sir!!! How may i help you")

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.adjust_for_ambient_noise(source)
		#r.pause_threshold = 0.5
		audio = r.listen(source)

	try:
		print("Recognizing...")
		#For offline CMUSphinx
		query = r.recognize_google(audio, language='en-in')
		print("User said :{}\n".format(query))

	except Exception as e:
		print("Say it again...")
		return "None"
	return query

def sendEmail(to,content):
	#Allow less secured apps
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('abhiaakash007@gmail.com','kiet#005')
	server.sendmail('abhiaakash007@gmail',to,content)
	server.close()


def works(query):
	if "wikipedia" in query:
		try:
			speak("searching in wikipedia my sir")
			query = query.replace("wikipedia","")
			results = wikipedia.summary(query,sentences = 2)
			speak("According to wikipedia")
			print(results)
			speak(results)
		except:
			print("please say it again...")

	elif "open youtube" in query:
		webbrowser.open("youtube.com")

	elif "open google" in query:
		webbrowser.open("google.com")

	elif "open moodle" in query:
		webbrowser.open("moodle.kiet.edu/moodle")

	elif "play music" in query:
		m_dir = 'E:\\Songs'
		songs = os.listdir(m_dir)
		os.startfile(os.path.join(m_dir,songs[random.randint(0,len(songs)-1)]))

	elif "the time" in query:
		strTime = datetime.datetime.now().strftime("%H:%M:%S")
		speak("The Time is {}".format(strTime))

	elif "send email to abhinav" in query:
		try:
			speak("What should I say?")
			content = takeCommand()
			to = "kesherwaniabhinav@gmail.com"
			sendEmail(to,content)
			speak("Email has been sent!")
		except Exception as e:
			speak("Unable to send Email")



if __name__ == '__main__':
	wishMe()
	query = takeCommand().lower()
	while not("close" in query):
		works(query)
		query = takeCommand().lower()


