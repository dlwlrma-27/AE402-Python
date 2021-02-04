d={}
print("Welcome to the translator")
print("please enter the option you want to use")
print("########################################")

while True:
    print('=>')
    print('1.add a word to dictionary')
    print('2.list out the words')
    print('3.english to chinese')
    print('4.chineseto english')
    print('5.test your self')
    print('6.exit')

    sel=input('Enter the option you want to use:')
    if sel=='1':
        while True:
            voc=input('enter the word(press 0 to exit)')
            if voc=='0':
                break
            if voc not in d:
                m=input('enter chinese')
                d[voc]=m
            else:print('the word is already exists')
    elif sel=='2':
        lk=sorted(d)
        for item in lk:
            print(item,'is',d[item])
    elif sel=='3':
        voc=input('enter english((press 0 to exit)')
        if voc=='0':
            break
        if voc in d:
            print(d[voc])
        else:
            print('no matching word in dictionary')
    elif sel=='4':
        got=False
        ch=input('enter Chinese(press 0 to exit)')
        if ch=='0':
            break
        for k,v in d.items():
            if ch==v:
                print(ch,'englih:', k)
                got=True
            if not got:
                print('sorry, no matching word')
    elif sel=='5':
        score=0
        print('the total score is',len(d), 'points')
        for k,v in d.items():
            print(v,':')       
            ans=input()
            if ans==k:
                score+=1
                print('coreect!you have',score,'points now')
            else:
                print('wrong! you have',score,'points now')
    elif sel=='6':
        break
    else:
        print('input invalid, renter')        