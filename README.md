# Task_19
Задание ЕГЭ 19

def game(s,h): </br>
    if s<=13:</br>
        return h==2 or h==4</br>
    else:</br>
        if h>4:</br>
            return False</br>
    if h%2!=0:</br>
        return any([game(s-2,h+1),game(s//1.5,h+1)])</br>
    return all([game(s-2,h+1),game(s//1.5,h+1)])</br>
for s in range(14,1000):</br>
    if game(s,0): print(s)</br>
