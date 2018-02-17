'''
Created on Feb 3, 2018

@author: ITAUser
'''

"""file="constituton.txt"
numberfile=open(file,"r")
text = numberfile.read()
words = text.split() 
print(len(words))"""


fname="constituton.txt"
f=open(fname,"r+")


for line in f: 
    words=line.split()
    num_words = len(words)
    for word in words: 
        I += word.count("p")
        