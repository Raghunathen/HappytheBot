from difflib import SequenceMatcher
import random
import speech_recognition as sr

# Clearing Files
file = open('communicator.txt', 'w')
file.write('')
file.close()
file = open('detail.txt', 'w')
file.write('')
file.close()
file = open('yes.txt', 'w')
file.write('')
file.close()

class klass:
	def song(name):
		file = open('communicator.txt', 'w')
		file.write('song')
		file.close()
		song = open('detail.txt', 'w')
		song.write(name)
		song.close()
		yes = open('yes.txt', 'w')
		yes.write('play')
		yes.close()
	def wikipedia(search):
		file = open('communicator.txt', 'w')
		file.write('wikipedia')
		file.close()
		song = open('detail.txt', 'w')
		song.write(search)
		song.close()
		yes = open('yes.txt', 'w')
		yes.write('wiki')
		yes.close()
		
		
	def google(search):
		file = open('communicator.txt', 'w')
		file.write('google')
		file.close()
		song = open('detail.txt', 'w')
		song.write(search)
		song.close()
		yes = open('yes.txt', 'w')
		yes.write('google')
		yes.close()
	



def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

def ytmusic(spoken):
	l = ('yes','no')
	
	if spoken != 'play':
		if 'play' in spoken:
			name = spoken.replace('play ', '')
			song = getattr(klass, 'song')
			song(name)
	else:
		yes = open('yes.txt', 'w')
		yes.write('play')
		yes.close()
	


def wiki(spoken):
	term = spoken.replace('wikipedia ', '')
	wikipedia = getattr(klass, 'wikipedia')
	wikipedia(term)

def jokes():
	file = open('communicator.txt', 'w')
	file.write('jokes')
	file.close()

def google(spoken):
	print('inside google')
	name = spoken.replace('google ', '')
	name = spoken.replace('Google ', '')
	google = getattr(klass, 'google')
	google(name)
def time():
	file = open('communicator.txt', 'w')
	file.write('time')
	file.close()
def news():
	file = open('communicator.txt', 'w')
	file.write('news')
	file.close()
def weather():
	file = open('communicator.txt', 'w')
	file.write('weather')
	file.close()

def sorter(spoken):
	if 'play' in spoken or 'Play' in spoken :
		print('resume')
		ytmusic(spoken)
	if 'pause' in spoken or 'Pause' in spoken:
		file = open('yes.txt', 'w')
		file.write('nope')
		file.close()
	if 'stop' in spoken or 'Stop' in spoken or 'top' in spoken:
		file = open('yes.txt', 'w')
		file.write('stop')
		file.close()
	if 'resume' in spoken or 'Resume' in spoken:
		file = open('yes.txt', 'w')
		file.write('play')
		file.close()
	if 'wikipedia' in spoken or 'Wikipedia' in spoken:
		wiki(spoken)
	if 'joke' in spoken or 'Joke' in spoken:
		jokes()
	if 'google' in spoken or 'Google' in spoken:
		google(spoken)
	if 'time' in spoken or 'Time' in spoken:
		time()
	if 'news' in spoken or 'News' in spoken:
		news()
	if 'weather' in spoken or 'Weather' in spoken:
		weather()


while True:
	print('loop')
	hot_word = ['Hey Happy', 'hey happy', 'hello happy', 'Hello Happy', 'Hey happy', 'hey Happy']
	r=sr.Recognizer()
	r.pause_threshold=1
	with sr.Microphone() as source:
		text=r.listen(source)
		try:
			text=r.recognize_google(text, language = 'en-IN')
			print(text)
		except sr.UnknownValueError:
			print('Im sorry I cant understand you')
		try:
			print('inside try')
			for i in hot_word:
				if i in text:
					print('hotword detected')
					r.pause_threshold=2
					with sr.Microphone() as source:
						text=r.listen(source)
					try:
						text=r.recognize_google(text, language = 'en-IN')
					except sr.UnknownValueError:
						pass
					print(text)
					sorter(text)
					break
		except TypeError:
			print('inside except')
			pass