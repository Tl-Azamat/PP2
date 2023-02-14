spy_game = [1,2,4,0,0,7,5]
def sspy_gamwe(spy_game):
    for i in spy_game:
        if i = 7:
            spy_game = spy_game[:spy_game.index(i)]
    if len(spy_game) == len(spy_game):
        return False
    cnt = 0
    for i in spy_game:
        if  i = '3':
            cnt += 1
    if cnt >= 2:
        return True
    else:
        return False 
