# def myfun(l1,l2):
#     merge = l1+l2

#     unqlist= list(set(merge))

#     unqlist.sort()
#     return unqlist

# l1=[1,4,2,1,3,4]
# l2=[4,5,7,6,7,5]

# print(myfun(l1,l2))

# from math import sqrt
# def movierecom(userrating,ratingdataset):
#     common = set(userrating) & set(ratingdataset)
#     if not common:
#         return 0
    
#     sum1= sum(userrating[movie] for movie in common)
#     sum2 = sum(ratingdataset[movie] for movie in common)

#     sum1sq= sum(userrating[movie]**2 for movie in common)
#     sum2sq = sum(ratingdataset[movie]**2 for movie in common)

#     pro = sum(userrating[movie] * ratingdataset[movie] for movie in common)

#     numa = pro

#     deno = sqrt(sum1sq) * sqrt(sum2sq)

#     if not deno:
#         return 0
#     return numa/deno

# def myfun(userrating,dataset,recommand=5):
#     simi = []

#     for otheruser in dataset:
#         simila = movierecom(userrating,otheruser)
#         simi.append((simila,otheruser))

#     simi.sort(reverse=True,key= lambda x: x[0])

#     moviescore = {}
#     for simila,otheruser in simi:
#         if simila <=0:
#             continue
#         for movie,rating in otheruser.items():
#             if movie not in  userrating:
#                 if movie not in moviescore:
#                     moviescore[movie]=0
#                 moviescore[movie] += simila * rating
    
#     myfun1 = sorted(moviescore.items(), key = lambda x:x[1],reverse=True)

#     return [movie for movie, score in myfun1[:recommand]]


# userrating={
#     "Movie A": 5,
# }
# ratingdataset=[
#     {"Movie A": 5, "Movie B": 4, "Movie C": 1, "Movie D": 4},
#     {"Movie A": 5, "Movie B": 2, "Movie C": 1, "Movie E": 3},
#     {"Movie A": 5, "Movie B": 4, "Movie G": 3, "Movie F": 4},
#     {"Movie A": 5, "Movie B": 2, "Movie C": 1, "Movie G": 1},
# ]

# myfun1 = myfun(userrating,ratingdataset)
# print(myfun1)

# import pyttsx3
# from PyDictionary import PyDictionary
# class Speak:
#     def read(self,audio):
#         engine = pyttsx3.init('sapi5')
#         voices = engine.getProperty('voices')

#         engine.setProperty('voice',voices[0].id)
#         engine.say(audio)
#         engine.runAndWait()

# class Tell:
#     def dic(self):
#         speak = Speak()
#         dis= PyDictionary()
#         print("which word do u want to find the meaning")
#         speak.read("which word do u want to find the meaning")

#         inp=str(input())
#         word =dis.meaning(inp)
#         print(len(word))

#         for state in word:
#             print(word[state])
#             speak.read("the meaning is "+str(word[state]))
        
# if __name__ =="__main__":
#     Tell()
#     Tell.dic(self=None)

import PyPDF2
import pyttsx3

def Speak(path):
    try:
        with open(path,'rb') as file:
            pdfreader=PyPDF2.PdfReader(file)

            if len(pdfreader.pages)==0:
                print("this pdf is empty")
                return
            

            page = pdfreader.pages[0]
            text = page.extract_text()

            if text:
                speak = pyttsx3.init()
                speak.say(text)
                speak.runAndWait()
            else:
                print("not text found")
    except FileNotFoundError:
        print("file not found")
path = 'JS Notes.pdf'

Speak(path)