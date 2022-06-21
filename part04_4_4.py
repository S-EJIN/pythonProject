# 게임 개발 : N*M 크기의 맵안에서 움직이는 캐릭터
# 맵 각 칸은 (A, B) A는 북쪽으로부터 떨어진 칸 & B는 서쪽으로부터 떨어진 칸의 개수, 캐릭터는 상하좌우로 움직이며 바다로는 이동불가
# 1. 현재 위치에서 현재 방향기준 왼족방향부터 갈 곳을 정함
# 2.바로 왼쪽방향에 가보지 않은 칸이 존재하면 왼쪽방향으로 회전 후 왼쪽으로 한 칸 전진,
# 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 수앵하고 1단계로 돌아감
# 네 방향모두 가봤거나 바다칸인경우 바라보는 방향 유지 후 한 칸 뒤로가고 1단계로 돌아감.
# 이떄 뒤쪽이 바다면 움직이지 않음
#---------------------------------------------------------------------------
# 첫째 줄 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력(3<=N, M<=50)
# 둘째 줄에 게임 캐릭터가 있는 칸 좌표와 바라보는 방향이 각 서로 공백으로 구분하여 주어진다
# (0: 북, 1: 동, 2: 남, 3: 서)
# 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. 맵의 외각은 항상 바다로 되어있다
# (0: 육지, 1: 바다). 처음 캐릭터가 위치한 칸의 상태는 항상
# if 육지이다:
# 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다

n, m = map(int, input().split())

#방문 위치 저장을 위한 맵을 생성하고 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x, y좌표, 방향 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 #현재 좌표 방문 처리

#전체 맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

    #시뮬레이션 시작
    count = 1
    turn_time = 0
    while True:
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]

        #회전 후 정면에 가보지 않은 칸이 존재하는 경우
        if d[nx][ny] == 0 and array[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue

        #회전 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
        else:
            turn_time += 1

        # 네 방향 모두 갈 수 없는 경우
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]

            #뒤로 갈 수 있으면 이동
            if array[nx][ny] == 0:
                x = nx
                y = ny

            else:
                break
                turn_time = 0


        print(count)




