import os
import random
import time

class Node:
    def __repr__(self) -> str:
        return f"{self.val}"

    def __init__(self,val,prev_n=None,next_n=None) -> None:
        self.prev = prev_n
        self.next = next_n
        self.val = val

m = [Node(val=i) for i in range(1,13)]

for idx,node in enumerate(m):
    if idx != 11:
        node.next = m[idx+1]
    #for 12th element
    else:
        node.next = m[0]

m.reverse()

for idx,node in enumerate(m):
    if idx != 11:
        node.prev = m[idx+1]
    #for 12th element
    else:
        node.prev = m[0]


head = m[0]
curr = head
count = 0
appear_list = [head]
count_dict = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    10:0,
    11:0,
    12:0
    }
probablity_dict = {
    1:0.0,
    2:0.0,
    3:0.0,
    4:0.0,
    5:0.0,
    6:0.0,
    7:0.0,
    8:0.0,
    9:0.0,
    10:0.0,
    11:0.0,
    12:0.0
    }


options = [0,1]
try:
    while True:
        if len(appear_list) != 12:
            if curr not in appear_list:
                appear_list.append(curr)
            choice = random.choice(options)
            
            if choice == 0:
                curr = curr.prev
            else:
                curr = curr.next

        else:
            os.system("clear")
            count += 1
            count_dict[appear_list[-1].val] += 1
            for k,v in count_dict.items():
                probablity_dict[k] = v/count
            appear_list = [head]
            text = f"""
    Current node: {curr}
    Loop counts: {count}
    Counts: {count_dict}
    Probablity: {probablity_dict}
    """
            print(text)
            curr = head
except KeyboardInterrupt:
        text = f"""
Current node: {curr}
Loop counts: {count}
Counts: {count_dict}
Probablity: {probablity_dict}
"""
        print(text)