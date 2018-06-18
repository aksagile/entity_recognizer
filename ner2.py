# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:21:43 2018

@author: USER
"""

import re

fooddict = {'splendar +':'bike','hudson': 'place','oreo shakes':'shake','pan pizzas':'pizza','momos sizzler':'sizzler','arrabiata pasta':'pasta','hazelnut cold coffee':'coffee','cheese steak':'steak','peri peri sauce':'sauce','peri peri chicken':'chicken','hudson lane':'place','gtb nagar':'metro','samsung HD TV':'product','mobile phone':'phone',' Micromax Canvas 6':'phone','flipkart':'company','aluminium condencer':'condencer','copper condencer':'condencer','bank account':'bank','phonepe':'app','order id':'id','consumer court':'court','voxya':'company','jeans':'cloth','sneakers':'shoes','lime road':'company','limeroad':'company','curefit':'company','cure fit':'company','curefits':'company','butter chicken':'chicken','chana':'food',}
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def entity_recognizer(sentence):
    listofWords = re.findall(r"[\w']+|[.,!?;]", sentence)
    copyofWords=[]
    customentitiesDict = {}
    for l in listofWords:
        copyofWords.append(l)
    originalpos3 =[]
#trigram
    i=-1
    j=-1
    while(i<len(listofWords)):
        i=i+1
        j=j+1
        originalpos3.append(i)
        if (i <len(listofWords)-2):
            s3 = listofWords[i]+' '+listofWords[i+1]+' '+listofWords[i+2]
            if (s3 in fooddict.keys()):

                originalpos3.pop()
                customentitiesDict[i,i+1,i+2] = s3
                copyofWords[j:j+3] = [fooddict[s3]]
                i=i+2
                originalpos3.append(i)
  
    print(originalpos3)
    print(copyofWords)
    print(customentitiesDict)
#bigram
    i=-1
    j=-1
    copyofWords2  =[]
    originalpos2 = []
    for w in copyofWords:
        copyofWords2.append(w)
    while(i<len(copyofWords)):
        i=i+1
        j=j+1
        originalpos2.append(originalpos3[i])
        if i<len(copyofWords)-1:
            s2 = copyofWords[i]+' '+copyofWords[i+1]
            if s2 in fooddict.keys():
                originalpos2.pop()
                customentitiesDict[originalpos3[i],originalpos3[i+1]] = s2
                copyofWords2[j:j+2] = [fooddict[s2]]
                i=i+1
                originalpos2.append(originalpos3[i])
                
    print(originalpos2)
    print(copyofWords2)
    print(customentitiesDict)
    i=0
#unigram
    #if not copyofWords2:
     #   for l in listofWords:
      #      copyofWords2.apppend(l)
       # print ("yes")
            
    while (i<len(copyofWords2)):
        
        if copyofWords2[i] in fooddict.keys():
            customentitiesDict[originalpos2[i]]= copyofWords2[i]
            copyofWords2[i] = fooddict[copyofWords2[i]]
        i=i+1
            
                
    print(originalpos2)
    print(copyofWords2)
    print(customentitiesDict)
        
    #while()
            
        
        
sent = "the pan pizzas, momos sizzler, the arrabiata pasta, the hazelnut cold coffee, mojitos, cottage cheese steak in peri peri sauce All time favourite."
entity_recognizer(sent2)

















































































































































































