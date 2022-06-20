n =int(input())
x, y = 1, 1
plans = input().split()

#L, R, U, D 이동항뱡
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

        #공간을 벗어나는 경우 무시한다. 좌표가 마이너스 이거나 입력 범위를 넘어선 경우
        if nx <1 or ny <1 or nx > n or ny > n:
            continue

        x, y = nx, ny   #이동으로 더한 좌표값 저장

    print(x, y)
