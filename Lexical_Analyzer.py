import random
import nltk

with open("text.txt") as text:
    story = text.read()

#tokenize the text file
words = nltk.word_tokenize(story)
#print(words)

#create lists
noun_list=[]
det_list=[]
verb_list=[]
adj_list=[]
grammar_mark_list=[]

#list with sentences
sentence_list=[]

for i in words:
    if(i=="dog" or i=="cat" or i=="food"):        
        noun_list.append(i)
    elif(i=="the"):
        det_list.append(i)
    elif(i=="needs" or i=="hates" or i=="has" or i=="chased" or i=="is"):
        verb_list.append(i)
    elif(i=="scary"):      
        adj_list.append(i)
    elif(i=="."):
        grammar_mark_list.append(i)



#function that returns a new sentence
def NewSentence():

 mylist=[]

 #randomly choose elements from each list
 
 word=random.choice(det_list)

 word2=random.choice(noun_list)

 word3=random.choice(verb_list)

 word4=random.choice(adj_list)

 word5=random.choice(det_list)

 word6=random.choice(noun_list)

 word7=random.choice(grammar_mark_list)

 #create sentence
 if(word3=="is"):
   sentence = word + " " + word2 + " " + word3 + " " + word4 + word7
 else:
    sentence = word + " " + word2 + " " + word3 + " " + word5 + " " + word6 + word7

 #insert sentence into a list
 mylist.append(sentence)
 #insert list into another list
 sentence_list.append(mylist)

 return sentence_list


#create up to 5 sentences
number_of_sentences=random.randint(1,5)

#show the sentences
for i in range(number_of_sentences):
 GeneratedSentence=NewSentence()
 print(GeneratedSentence)
