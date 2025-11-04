# n : 배열판크기, m: 스프레이
# arr : 배열판

# # 상하좌우
# r = [-1, 1, 0, 0]
# c = [0, 0, -1, 1]

# # 좌상, 우상, 우하, 좌하
# x = [-1, -1, 1, 1]
# y = [-1, 1, 1, -1]

T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_fly = 0

    # 시작점 설정
    for i in range(n):
        for j in range(n):
            cnt_fly = 0
            cnt_fly += arr[i][j]
            # + 방향으로 파리 더해서 범위 넘어가기 전까지만 진행하기, 기존 max 보다 높으면 갱신
            
                    


            

            # x 방향으로 파리 더해서 범위 넘어가기 전까지 진행, 기존 max보다 높으면 갱신
            

