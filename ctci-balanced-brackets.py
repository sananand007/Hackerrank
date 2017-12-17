'''
CTCI-Hacker Rank bracket match - passed All TCs [18]
https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem
Uses recurssion

5
}][}}(}][))]
[](){()}
()
({}([][]))[]()
{)[](}]}]}))}(())(

NO
YES
YES
YES
NO

'''
from collections import deque
def is_matched(expression):
    hashmap = {"{":"}","(":")","[":"]"}
    dq,size=deque(expression),len(expression)
    if expression=="":return True
    if size%2!=0: return False
    while dq:
        l,store,countl=dq.popleft(),None,0
        for idx, x in enumerate(dq):
            if l not in hashmap:return False
            if x==l:countl+=1
            elif x==hashmap[l] and countl==0:
                store=idx
                break
            elif x==hashmap[l] and countl!=0:countl-=1
        if store is not None:
            exp = [dq.popleft() for i in range(0,store)]
            exp = "".join(exp)
            dq.popleft()
            if is_matched(exp):
                continue
            else:
                return False
        elif not store:
            return False
    return True

t = int(input().strip())

for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
