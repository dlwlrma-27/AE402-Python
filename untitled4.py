lst = []
num = int(input('How many people: '))
for n in range(num):
    numbers = int(input('Enter their score:'))
    lst.append(numbers)
def Average(lst): 
    return sum(lst) / len(lst)
average=Average(lst)
def Highestscore(lst):
    return max(lst)
def Lowestscore(lst):
    return min(lst) 
print("Highest score:", Highestscore(lst), "lowest score:", Lowestscore(lst))
print("Average:", round(average, 2))