new_score = 18
f = open('highScore.txt', 'r+')
original_score = int(f.readline())
f.seek(0)
if new_score > original_score:
    f.writelines(str(new_score))
