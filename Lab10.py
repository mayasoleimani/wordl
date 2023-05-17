import random
from matplotlib.axis import XAxis
import matplotlib.pyplot as plt

allletters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

try:
    with open("Lab10answers.txt","r+") as my_file:
        readinglines=my_file.read()
        wordListRead=readinglines.split()
        threeWordsRandom=random.sample(wordListRead,3) #grabs 3 random words
        print(threeWordsRandom)
        splitWordList=[] #15 letters for 3 words
        position1,position2,position3,position4,position5=[],[],[],[],[]
        word1=threeWordsRandom[:1]
        word1chars=list(word1[0])
        word2=threeWordsRandom[1:2]
        word2chars=list(word2[0])
        word3=threeWordsRandom[2:3]
        word3chars=list(word3[0])

        #creating position lists
        for x in word1chars:
            position1.append(word1chars[0])
            position2.append(word1chars[1])
            position3.append(word1chars[2])
            position4.append(word1chars[3])
            position5.append(word1chars[4])
            break
            
        for x in word2chars:
            position1.append(word2chars[0])
            position2.append(word2chars[1])
            position3.append(word2chars[2])
            position4.append(word2chars[3])
            position5.append(word2chars[4])
            break

        for x in word3chars:
            position1.append(word3chars[0])
            position2.append(word3chars[1])
            position3.append(word3chars[2])
            position4.append(word3chars[3])
            position5.append(word3chars[4])
            break
    
        
        for word in threeWordsRandom:
            for letter in word:
                word=letter.split()
                splitWordList.append(letter) #['w','o','r','d','s','w','o','r','d','s']
        
        letterInAnswerButWrongSpot1=[]
        for letter in (position1):
            if (letter in (position2[:])):
                letterInAnswerButWrongSpot1.append(letter)
            if (letter in position3[:]):
                letterInAnswerButWrongSpot1.append(letter)
            if (letter in position4[:]):
                letterInAnswerButWrongSpot1.append(letter)
            if (letter in position5[:]):
                letterInAnswerButWrongSpot1.append(letter)

        letterInAnswerButWrongSpot2=[]
        for letter in (position2):
            if (letter in (position1[:])):
                letterInAnswerButWrongSpot2.append(letter)
            if (letter in position3[:]):
                letterInAnswerButWrongSpot2.append(letter)
            if (letter in position4[:]):
                letterInAnswerButWrongSpot2.append(letter)
            if (letter in position5[:]):
                letterInAnswerButWrongSpot2.append(letter)

        letterInAnswerButWrongSpot3=[]
        for letter in (position3):
            if (letter in (position1[:])):
                letterInAnswerButWrongSpot3.append(letter)
            if (letter in position2[:]):
                letterInAnswerButWrongSpot3.append(letter)
            if (letter in position4[:]):
                letterInAnswerButWrongSpot3.append(letter)
            if (letter in position5[:]):
                letterInAnswerButWrongSpot3.append(letter)

        letterInAnswerButWrongSpot4=[]
        for letter in (position4):
            if (letter in (position1[:])):
                letterInAnswerButWrongSpot4.append(letter)
            if (letter in position2[:]):
                letterInAnswerButWrongSpot4.append(letter)
            if (letter in position3[:]):
                letterInAnswerButWrongSpot4.append(letter)
            if (letter in position5[:]):
                letterInAnswerButWrongSpot4.append(letter)

        letterInAnswerButWrongSpot5=[]
        for letter in (position5):
            if (letter in (position1[:])):
                letterInAnswerButWrongSpot5.append(letter)
            if (letter in position2[:]):
                letterInAnswerButWrongSpot5.append(letter)
            if (letter in position3[:]):
                letterInAnswerButWrongSpot5.append(letter)
            if (letter in position4[:]):
                letterInAnswerButWrongSpot5.append(letter)

        #ONE COLOR, NOT IN ANY SPOTS
        lettersNotUsed=list(filter(lambda x: x not in splitWordList,allletters)) #letters NOT used
        

finally:
    plt.hist(allletters,color='w')
    plt.hist(position1,color='r',edgecolor="black", label="Position 1")
    plt.hist(position2,color='y',edgecolor="black", label="Position 2")
    plt.hist(position3,color='b',edgecolor="black", label="Position 3")
    plt.hist(position4,color='g',edgecolor="black", label="Position 4")
    plt.hist(position5,color='m',edgecolor="black", label="Position 5")
    plt.hist(letterInAnswerButWrongSpot1,color='r',alpha=.35,label="Wrong Spot Position 1")
    plt.hist(letterInAnswerButWrongSpot2,color='y',alpha=.35,label="Wrong Spot Position 2")
    plt.hist(letterInAnswerButWrongSpot3,color='b',alpha=.35,label="Wrong Spot Position 3")
    plt.hist(letterInAnswerButWrongSpot4,color='g',alpha=.35,label="Wrong Spot Position 4")
    plt.hist(letterInAnswerButWrongSpot5,color='m',alpha=.35,label="Wrong Spot Position 5")
    plt.title("Position Statistics")
    plt.ylabel("Frequency")
    plt.xlabel("Letters")
    plt.legend()
    plt.show()
