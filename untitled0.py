e_score=input("enter your english score")
m_score=input("enter your masth score")
e_score=int(e_score)
m_score=int(m_score)
if not(e_score>=0 and e_score<=100)and (m_score>=0 and m_score<=100):
    print("enter a score between the scale of 0-100")#asking the user to reenter the score
elif(e_score>=90 and m_score >=90):
    print("you won money")
elif(e_score>=100 or m_score >=100):
    print("you won money")
else:
    print("you don't get money")