import speech_recognition as sr
import os
import sys
audio="not"
while True:
	try:
		print("speak now")
		r=sr.Recognizer()
		with sr.Microphone() as source:
		    audio1=r.listen(source)
		audio=r.recognize_google(audio1)
		print(audio)
		if audio == "malaria" :
			os.system("malaria.mp3")
		elif audio == "Madraseye" or audio=="Madras eye":
			os.system("madraseye.mp3")
		elif audio == "Exit":
			break       
		else:
			print("speak again")
			continue
	except:
		#print(sys.exc_info[0])
		continue
		


#import speech_recognition as sr
import os
from gtts import gTTS
import webbrowser
import speech_recognition as sr
malaria ='Moderate to severe shaking chills High fever Sweating Headache Vomiting Diarrhea'
dengue="Sudden, high fever Severe headaches Pain behind the eyes Severe joint and muscle pain Fatigue Nausea Vomiting Skin rash, which appears two to five days after the onset of fever Mild bleeding (such a nose bleed, bleeding gums, or easy bruising)"
madraseye='Reddish eye scratchiness yellowish green substance'
swineflu=' fever, lethargy, sneezing, coughing, difficulty breathing sneezing coughing difficulty n breathing'
chikungunya='high fever, joint pain, and rash joint pain rash' 
language ='en'
tell=gTTS(text=malaria,lang=language,slow=False)
tell.save('malaria.mp3')
tell1=gTTS(text=madraseye,lang=language,slow=False)
tell1.save('madraseye.mp3')
tell2=gTTS(text=swineflu,lang=language,slow=False)
tell2.save('swineflu.mp3')
tell3=gTTS(text=chikungunya,lang=language,slow=False)
tell3.save('chikungunya.mp3')
tell4=gTTS(text=dengue,lang=language,slow=False)
tell4.save('dengue.mp3')
b=''
try:
	while(b!='0'):
		b=input()
		if(b=='malaria'):
			os.system('malaria.mp3')
		elif(b=='madraseye'):
			os.system('madrasee.mp3')
		elif(b=='swineflu'):
			os.system('swineflu.mp3')
		elif(b=='chikungunya'):
			os.system('chikungunya.mp3')
		elif(b=='dengue'):
			os.system('dengue.mp3')
		else:
			break
except:
	print("give proper input")
		  	 





import speech_recognition as sr
try: 	
	while True:
		r=sr.Recognizer()
	    	with sr.Microphone() as source:
	        	print("Say Something")
	        	audio1=r.listen(source)
	    audio=r.recognize_google(audio1)
	    if audio == "Malaria" :
			os.system("malaria.mp3")
		elif audio == "Madraseye":
			os.system("madraseye.mp3")
		elif audio == "Exit":
			break
		else:
			continue       
        
    except:
        pass