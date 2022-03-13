# -*- coding: utf-8 -*-
# push: 최근꺼 넣기
# pop: 최근거 꺼내기

def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()




def greet2(name):
    print("how are you," + name +"?")
    

def bye():
    print("ok bye!")
    
    
greet("maggie")
