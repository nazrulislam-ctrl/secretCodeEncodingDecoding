# Problem:
#Write a python program to translate a message into secret code language. Use the rules below to translate normal Engalish to secret code language.

# Code:
# If the word contains at least 3 characters, remove the first letter and append it at the end.
# now append three random characters at the starting and the end.
# Else: 
#     Simply reverse the string 

# Decoding:
#     if the word contains less than three characters, reverse it. 
# else: 
#     remove 3 random charaters from start and end. now remove the last letter and append to the begging.

# Solve:


st= input("Enter your message: ")
words= st.split(" ")
coding= input("1 for coding or 0 for decoding: ")
coding=True if (coding=="1") else False
if (coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1="rsg"
            r2="hlk"
            stnew= r1+word[1:] +word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stnew= word[3:-3]
            stnew= stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))