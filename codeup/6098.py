m = [list(map(int, input().split())) for _ in range(10)]
#이동
i =0
x =1
y =1

m[x][y] = 9
for i in range(100):
    if m[x][y+1] == 0:
            m[x][y+1] = 9
            y= y+1

    elif m[x][y+1] == 1 :
        if m[x+1][y]==0 :
            m[x+1][y] = 9
            x = x+1
        elif m[x+1][y] ==2:
            m[x+1][y] = 9
            break
        else:
            break
    else:
        m[x][y+1] = 9
        break

# 미로 출력
for i in range(10):
    for j in range(10):
        print(m[i][j],end=' ')
    print()