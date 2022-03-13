# -*- coding: utf-8 -*-

graph  = {}

graph["you"] = ["alice","bob","claire"]

print(graph["you"])

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
print(graph["start"].keys())


graph["start"].keys()
print(graph["start"]["a"])#<-values
print(graph["start"]["b"]) #<-values

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}


infinity = float("inf")

costs = {} #가격에대한 표작성 
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {} #해시테이블 만드는 과
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []  #정점을 추적하기위한 배열도 존재해야함. 


    

#find_lowest_cost_node 함수 구현
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None 
    for node in costs: #모든저적을 확인
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost= cost
            lowest_cost_node = node
    return lowest_cost_node



node = find_lowest_cost_node(costs) #아직처리하지 않은 가장싼 정점을 찾는다
while node is not None: #모든정점 처리시 반복문 종료
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost +neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)










