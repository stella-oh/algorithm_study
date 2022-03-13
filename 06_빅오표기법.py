# -*- coding: utf-8 -*-

from time import sleep


def print_items(list):
    for item in list:
        print(item)
        
        
def print_items2(list):
    for item in list:
        sleep(1)
        print(item)
        
        
list = [2,3,3,4,5,5,3]

# print_items2(list)

# print(print_items(list))

#hash function

book = dict() #same as exp book = {}

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.38

# print(book)


# print(book["avocado"])



voted = {}
value = voted.get("tom") #get :dictionary 안에 tom이있으면 반환해라..

def check_voter(name):
    if voted.get(name):
        print("투표했습니다.")
    else:
        voted[name] = True
        print("투표하세요.")
        
        
name = {'jake', 'trudy'}


check_voter('tom')