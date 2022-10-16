import random
import deepface
from youtubesearchpython import VideosSearch
import pafy
import vlc
import time
import wikipedia
import pyjokes as pj
import random
import webbrowser
import datetime as dt
import requests, json
from gtts import gTTS
import os
from pygame import mixer
import time


d = {0: "(oh)",
	 1: "one",
	 2: "two",
	 3: "three",
	 4: "four",
	 5: "five",
	 6: "six",
	 7: "seven",
	 8: "eight",
	 9: "nine",
	 10: "ten",
	 11: "eleven",
	 12: "twelve",
	 13: "thirteen",
	 14: "fourteen",
	 15: "fifteen",
	 16: "sixteen",
	 17: "seventeen",
	 18: "eighteen",
	 19: "nineteen",
	 20: "twenty",
	 30: "thirty",
	 40: "forty",
	 50: "fifty",
	 60: "sixty"}

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
try:
	os.remove('audio.mp3')
except FileNotFoundError:
	pass


def display_time(t):
	print('insde display_time')
	Hour = d[int( t[0:2])] if t[0:2] != "00" else d[12]
	Suffix = 'a.m.' if d[int( t[7:9])] == Hour else 'p.m.'

	if  t[3] == "0":
		if  t[4] == "0":
			Minute = ""
		else:
			Minute = d[0] + " " + d[int(t[4])]
	else:
		Minute = d[int(t[3])*10] + '-' + d[int(t[4])]
	print('The time is', Hour, Minute, Suffix)

class klass():
	def song():
		name = open('detail.txt', 'r')
		asd = name.read()
		print(asd)
		videosSearch = VideosSearch(asd, limit = 1)
		name.close()
		tmp = str(videosSearch.result().get('result')[0])
		id = tmp[0:36]
		id = id[25:]
		url = "https://www.youtube.com/watch?v=" + id
		video = pafy.new(url)
		best = video.getbestaudio()
		playurl = best.url
		Instance = vlc.Instance()
		player = Instance.media_player_new()
		Media = Instance.media_new(playurl)
		Media.get_mrl()
		player.set_media(Media)
		tmp = 0
		while True:
			file = open('yes.txt','r')
			asd = file.read()
			print(asd)
			print('inloop')
			print(tmp)
			if asd == 'play':
				print('inside if')
				if tmp == 0:
					print('play')
					player.play()
					tmp = tmp + 1
					print('temp = 0')
				else:
					op = player.get_state()
					print(str(op) + ' = op')
					if op == 6:
						break
					else:
						print('player running')
						player.play()
						print('temp = 1')	
						
			elif asd == 'nope':
				if player.can_pause() == 1:
					player.set_pause(1)
					print('inside')
			elif asd == 'stop':
				player.stop()
				break
			elif asd == '':
				player.play()
			else:
				print('else')
				print(asd)
				player.stop()
				break

			file.close()
	def wikipedia():
		name = open('detail.txt', 'r')
		name = name.read()
		print(name)
		wiki = wikipedia.summary(name, sentences=1, auto_suggest=False, redirect=True)
		print(wiki)
	def jokes():
		joke = pj.get_joke()
		print(joke)
	def google():
		print('inside google')
		name = open('detail.txt', 'r')
		name = name.read()
		print(name)
		url = 'https://www.google.com/search?q=' + name
		print(url)
		
		webbrowser.open(url, new = 2)
	def time():
		display_time(dt.datetime.now().strftime('%I %M %H'))
	def news():
		query_params = {
			"source": "bbc-news",
			"sortBy": "top",
			"apiKey": "b16f6e9eb7e34b09b871a9807fd28207"
			}
			
		main_url = "https://newsapi.org/v1/articles"

			# fetching data in json format
		res = requests.get(main_url, params=query_params)
		open_bbc_page = res.json()
		
			# getting all articles in a string article
		article = open_bbc_page["articles"]
		
		# empty list which will
			# contain all trending news
		results = []
			 
		for ar in article:
			results.append(ar["title"])
				 
		for i in range(len(results)):
			 
			# printing all trending news
			print(i + 1, results[i])
	def weather():
		api_key = "928bdbdac38fcffa6baba3e59e833f14"
		  
		# base_url variable to store url
		base_url = "http://api.openweathermap.org/data/2.5/weather?"
		  
		# Give city name
		city_name = 'chennai'
		  
		# complete_url variable to store
		# complete url address
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name
		  
		# get method of requests module
		# return response object
		response = requests.get(complete_url)
		  
		# json method of response object 
		# convert json format data into
		# python format data
		x = response.json()
		  
		# Now x contains list of nested dictionaries
		# Check the value of "cod" key is equal to
		# "404", means city is found otherwise,
		# city is not found
		if x["cod"] != "404":
		  
			# store the value of "main"
			# key in variable y
			y = x["main"]
		  
			# to the "temp" key of y
			current_temperature = y["temp"]
			current_temperature = current_temperature - 273.15
			current_temperature = round(current_temperature)
			# to the "humidity" key of y
			current_humidiy = y["humidity"]
		  
			# store the value of "weather"
			# key in variable z
			z = x["weather"]
		  
			# store the value corresponding 
			# to the "description" key at 
			# the 0th index of z
			weather_description = z[0]["description"]
		  
			weather = "Temperature is " + str(current_temperature) + " degrees. " + str(current_humidiy) + " Percent of Humidity in the air. " "and you might experience " + str(weather_description)
			print(weather)
			myobj = gTTS(text=weather, lang='en', slow=False)

			# Saving the converted audio in a mp3 file named
				# welcome 
			while True:	
				try:
					myobj.save("audio.mp3")
					break
				except PermissionError:
					pass	
				

			mixer.init()
			mixer.music.load('audio.mp3')
			mixer.music.play()
			try:
				os.remove('audio.mp3')
				
			except PermissionError:
				pass

		else:
			myobj = gTTS(text='Nope', lang='en', slow=False)

			myobj.save("audio.mp3")
			

			mixer.init()
			mixer.music.load('audio.mp3')
			mixer.music.play()
			try:
				os.remove('audio.mp3')
			except PermissionError:
				pass

			
global l
l = ['yes', 'no']

while True:
	print('loop')
	op = len(l)
	if op == 10:
		l = ['yes', 'no']
	file = open('communicator.txt', 'r')
	asd = file.read()
	file.close()
	if asd != '':
			call = getattr(klass, asd)
			file = open('communicator.txt', 'w')
			file.write('')
			file.close()
			if (callable(call)):

				print(asd)
				call()
				
				
			file = open('communicator.txt', 'w')
			file.write('')
			file.close()
		
		

