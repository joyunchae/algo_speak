# T 테스트케이스의 수, sudoku 데이터 , block , arr []

# 한 행 또는 한 블럭의 숫자(1~9)
#   > 겹치는 것이 없을 경우 1 출력
#   > 겹치는 것이 있을 경우 0 출력

# ans = 1
# 행검사 9번 반복
#   > 시작점은 0.0 > 이중 for문으로 돌기
#   > 해당 숫자가 리스트에 없을 경우 그 숫자는 리스트에 담고 계속 진행하기
#       > 만약 중복된 것이 있다면 0 - break

# 블럭검사 인덱스 7까지만 순회
#   시작점 설정
#       블럭 안에서 순회(range(3))
#       만약 중복 숫자가 리스트에 있다면 0출력 break

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    
    ans = 1
    # 행검사
    for i in range(9):
        # 행이 한 번 끝나면 리스트 초기화를 어떻게 하지?
        verify_list = []
        for j in range(9):
            if sudoku[i][j] not in verify_list:
                verify_list.append(sudoku[i][j])
            else:
                ans = 0
                break
        if ans == 0:
            break
    
    # 블럭검사
    for r in range(0,7,3):
        for c in range(0,7,3):
            # 블럭 사이즈
            verify_list = []
            for x in range(r, r+3):
                for y in range(c, c+3):
                    if sudoku[x][y] not in verify_list:
                        verify_list.append(sudoku[x][y])
            # print(verify_list)
                    else:
                        ans = 0
                        break
        if ans == 0:
            break

    # 열검사 : 이걸 빼먹음..
    for j in range(9):
        # 행이 한 번 끝나면 리스트 초기화를 어떻게 하지?
        verify_list = []
        for i in range(9):
            if sudoku[i][j] not in verify_list:
                verify_list.append(sudoku[i][j])
            else:
                ans = 0
                break
        if ans == 0:
            break

    print(f'#{tc} {ans}')



