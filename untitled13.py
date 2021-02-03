n=int(input("How many people? "))
name=[]
score=[]
lowest=100
highest=0
highestname=""
lowestname=""
summath=0
def lowest(i):
for i in range(0,2*n):
   mathscore=input("")
   score.append(mathscore)
   print(score)
   if i%2==1:
       score[i]=int(score[i])
       summath=summath+sscorecore[1]
       if highest<[i]:
           highest=score[i]
           highestname=sc:ore[i-1]
       if lowest>score[i]
           lowest=score[i]
           lowestname=score[i-1]

print(score)
print("Highest is " , highest," who is " , highestname)
print("Lowest is " , lowest," who is " , lowestname)
print("Class average is " , summath/n)