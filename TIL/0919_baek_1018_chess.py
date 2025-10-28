# 백준 체스판 문제

N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7):
    for b in range(M-7):
        white = 0
        black = 0

        for i in range(a, a+8):
            for j in range(b, b+8):
                # 짝수 > 왼쪽 위와 같은 색
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        white += 1
                    if original[i][j] != 'B':
                        black += 1
                # 홀수 > 왼쪽 위와 반대색
                else:
                    # 왼쪽 위가 w라면 다음 줄은 반대색
                    if original[i][j] != 'B':
                        white += 1
                    # 왼쪽 위가 b라면 다음 줄은 반대색
                    if original[i][j] != 'W':
                        black += 1
        count.append(min(white, black))

print(min(count))