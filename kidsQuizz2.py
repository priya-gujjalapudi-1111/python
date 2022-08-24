import speech_recognition as sr
import pyttsx3
text_speech=pyttsx3.init()
listener=sr.Recognizer()
name=input("Enter your name: ")
age=int(input("What is your age:"))
aname=f"Hello {name} your age is {age}"
text_speech.say(aname)
text_speech.runAndWait()
print("Quiz will start in few seconds.......")
q1="Hii ,All the best for the quizz"
text_speech.say(q1)
text_speech.runAndWait()
print("Get")
print("Start")
print("Go!!!!! ")
countV=0
if age<=5:
    l1=["What is the spelling of apple ??","Trees are in which color ??","How many days do we have in a week?","Human has how many legs ??","Sun rises in which direction??","How many colors in rainbow??","Which festival is known as the festival of colors?","Sky is in which color??","Spell the daddy??","2 +2 ="]
    l1a=["apple","green","7","2","east","7","holi","blue","daddy","4"]
    for i in range(len(l1)):
         print(l1[i])
         text_speech.say(l1[i])
         text_speech.runAndWait()
         a=""
         with sr.Microphone() as source:
             voice=listener.listen(source)
             try:
                 a=listener.recognize_google(voice)
                 print(a)
             except:
                 pass
         if l1a[i]==a.lower():
             countV +=1

elif age>5 and age<=8:
    l2=["Which number comes after 10?","What is the shape of the Moon? ","What is 25/5?","How many hours are threr in a day? ","How many Alphabets  are there?","Which gas do humans release? ","What is the color of an Apple? ","How many minutes in one hour? ","What is the final result of 44+22?","How many colors are there in a rainbow?"]
    l2a=["11","circle","5","24","26","carbon dioxide","red","60","66","7"]
    for i in range(len(l1)):
         print(l2[i])
         text_speech.say(l2[i])
         text_speech.runAndWait()
         a=''
         with sr.Microphone() as source:
             voice=listener.listen(source)
             try:
                 a=listener.recognize_google(voice)
                 print(a)
             except:
                 pass
         if l2a[i]==a.lower():
             countV +=1

elif age>8 and age<=10:
    l3=["How many sides does the Pentagon have?","What is the origin of the Tapi river?","Which public sector bank is the largest in India?","How many hours are there in two days?","Which is the tallest mountain in the world?","Which is the largest ocean in the world?","Which country is home to the kangaroo?","Where is the World Health Organisation situated?","Where is Salim Ali National Park located?","In which direction does the sunrise?"]
    l3a=["5","satpura ranges","state bank of india","48","mount everest","pacific ocean","australia","Switzerland","jammu and kashmir","east"]
    for i in range(len(l3)):
         print(l3[i])
         text_speech.say(l3[i])
         text_speech.runAndWait()
         a=''
         with sr.Microphone() as source:
             voice=listener.listen(source)
             try:
                 a=listener.recognize_google(voice)
                 print(a)
             except:
                 pass
         if l1a[i]==a.lower():
             countV +=1

else:
    ans="Sorry this game is not for your age"
print("Your score is ",countV)
