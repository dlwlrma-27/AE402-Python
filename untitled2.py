mathscore=input("enter math score")
englishscore=input("enter english score")
mathscore=int(mathscore)
englishscore=int(englishscore)
if (englishscore>=90 and mathscore>=90):
    print("reward")
elif(englishscore>=90 and mathscore<=90):
    print("pass")
elif(englishscore<=90 and mathscore>=90):
     print("pass")
elif(englishscore<=90 and mathscore<=90):
    print("fail")
