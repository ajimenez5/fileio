'''
Created on Feb 3, 2018

@author: ITAUser
'''

file="constituton.txt"
numberfile=open(file,"r")
text = numberfile.read()
words = text.split() 
print(len(words))
