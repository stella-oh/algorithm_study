# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 01:29:01 2022

@author: yoonjung
"""

# def look_for_key(main_box):
#     pile = main_box.make_a_pile_to_look_through()
#     while pile is not empty:
#         box = pile.grab_a_box()
#         for item in box:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print("find a key!")

# #sudo code

# #재귀: recurrsion : calling itselfs

# def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item) #자기함수 자체를 다시 호출하여 위의 반복구문을 생략
#         elif item.is_a_key():
#             print("fina a key!")
    

#간단한 재귀함수를 만들어보자
# def countdown(i):
#     print(i)
#     return countdown(i-1)
    
    
# i =65
# print(countdown(i))

#문제발생...계속 돌아간다

# def countdown(i):
#     print(i)
#     if i<=1:
#         return
#     else:
#         countdown(i-1)

# i = 65

# print(countdown(i)) #자동 for item in len(i)

def countdown(i):
    while True:
        if i<=1:
            return
        else:
            i-=1
        

i = 65

print(countdown(i))
       
            
        
        
        