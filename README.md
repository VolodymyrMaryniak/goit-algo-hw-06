# Homework 6

## Task 2

Ось приклад виконнаня скрипта task2.py

.../goit-algo-hw-06/task2.py  
DFS:  
FL GA NC TN TX AZ CA NV MT WA ID MN IA CO KS MO OH MI NY  
BFS:  
FL GA NC TN TX OH MO NY AZ KS CO MI IA CA MT NV MN WA ID  


### Conclusions
Як бачимо, DFS алгоритм працює як і очікувалось: "провалюється" по графу аж допоки не обійде його повністю. 
FL -> GA -> NC -> TN -> TX -> AZ -> CA ... 

Натомість BFS опрацьовує граф "по рівнях". У нашому прикладі:
1 рівень - FL
2 рівень - GA
3 рівень - NC, TN, TX
4 рівень - OH, MO, NY, AZ, KS, CO
...
