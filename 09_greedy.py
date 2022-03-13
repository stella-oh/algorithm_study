# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 03:52:37 2022

@author: yoonjung
"""

states_needed = set(['mt','wa','or','id','nv','ut','ca','az'])


arr = [1,2,2,2,3,3,3]

print(set(arr)) # {1,2,3} query distinct 개념

stations = dict()
stations["kone"] = set(['id','nv','ut'])
stations['ktwo'] = set(['wa','id','mt'])
stations['kthree'] = set(['or','nv','ca'])
stations['kfour'] = set(['nv','ut'])
stations['kfive'] = set(['ca','az'])

final_stations = set() #마지막으로 방문할 방송국의 목록을 저장할 집합을 생성 


while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station #교집합 구하는 공식
        if len(covered) > len(states_covered):
            best_station = station 
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
        
#합집합 |, 교집합 & 차집합 -

print(final_stations)