#왕실의 나이트
# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동  7 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
# 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오

# 현재 위치를 기준으로 아래쪽, 오른쪽은 양수의 값 & 위쪽, 왼쪽은 음수의 값을 대입
input_data = input() #현재 나이트의 위치 입력받기
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:

    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)


