score=input("enter the score")
score=int(score)
if(not(score>0 and score<100)):
    print("enter a score between the number 0-100")
elif(score>=90 and score<=100):
    print("A")
elif(score>=80 and score<=89):
     print("B")
elif(score>=70 and score<=79):
    print("C")
elif(score>=60 and score<=69):
    print("D")
elif(score>=59 and score<=0):
    print("F")