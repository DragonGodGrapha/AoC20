from collections import deque

def war(deck1,deck2):
    while not (len(deck1)==0 or len(deck2)==0):
        s=deck1.popleft()
        o=deck2.popleft()
        
        
        #print(f'Player 1 plays: {s}\nPlayer 2 plays: {o}')
        if s>o:
            #print('Player 1 wins the round!')
            deck1.append(s)
            deck1.append(o)
            
        elif o>s:
            #print('Player 2 wins the round!')
            deck2.append(o)
            deck2.append(s)
            
        else:
            print('something broke')
    if len(deck1)==0:winner=2
    elif len(deck2)==0:winner=1
    else:winner=-1
    return deck1,deck2,winner


def score(deck):
    score=0
    for i,c in enumerate(reversed(deck)):
        score+=((i+1)*c)
    return(score)


def recwar(deck1,deck2):
    
    sharedlog=set()
    while not (len(deck1)==0 or len(deck2)==0):
        #print(len(deck1),len(deck2))
        
        if (tuple(deck1),tuple(deck2)) in sharedlog:
            return deck1,deck2,1
        sharedlog.add((tuple(deck1), tuple(deck2)))
        
        s=deck1.popleft()
        o=deck2.popleft()
        
        if len(deck1)>=s and len(deck2)>=o:
            d1=deque(list(deck1)[:s])
            d2=deque(list(deck2)[:o])
            winner=recwar(d1,d2)[2]
        
        elif s>o:winner=1
        elif s<o:winner=2
        
        if winner==1:
            deck1.append(s)
            deck1.append(o)
        elif winner==2:
            deck2.append(o)
            deck2.append(s)
            
    if len(deck1)==0:winner=2
    elif len(deck2)==0:winner=1
    else:winner=-1
    return deck1,deck2,winner

        
with open('22.txt') as deck:
    self,opp=deck.read().split('\n\n')    

self=deque(map(int,self.splitlines()[1:]))
opp=deque(map(int,opp.splitlines()[1:]))
s,o,w=war(self.copy(),opp.copy())

print(f'Part A: {score(s)}')

t1=deque([9,2,6,3,1])
t2=deque([5,8,4,7,10])

s,o,w=recwar(self.copy(),opp.copy())

print(f'Part B: {score([s,o][w-1])}')



                                     

