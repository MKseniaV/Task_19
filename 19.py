def game(s,h):
    if s<=13:
        return h==2 or h==4
    else:
        if h>4:
            return False
    if h%2!=0:
        return any([game(s-2,h+1),game(s//1.5,h+1)])
    return all([game(s-2,h+1),game(s//1.5,h+1)])
for s in range(14,1000):
    if game(s,0): print(s)
