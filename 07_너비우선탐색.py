# -*- coding: utf-8 -*-

graph = dict() #or graph= {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
 
from collections import deque
search_queue = deque()
search_queue += graph["you"]


# def person_is_seller(name):
#     return name[-1] == "m"

# while search_queue:
#     person = search_queue.popleft() #큐의 첫번째사람을 꺼냄
#     if person_is_seller(person): #끝자리가 m으로 끝나면 망고셀러이다. 
#         print(person+"is a mango seller!")
#     else:
#         search_queue += graph[person]
#     return False




def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searchd = [] #배열은 이미 확인한 사람 추적위한 배열 
    while search_enqueue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + "is a mango seller!")
                return True 
            else:
                search_enqueue += graph[person]
                searched.append(person)
    return False



search("you")

