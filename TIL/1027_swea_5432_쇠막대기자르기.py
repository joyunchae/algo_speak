# 결국 ai의 도움을 받았다..

# 레이저 : ()
# 쇠막대기 왼쪽 끝은(   오른쪽 끝은 닫힌 괄호 )
# 잘라진 쇠막대기를 구하는 프로그램을 작성하라

() ((( () () )( () ) () ))( () )
# 괄호를 연 순간부터 쇠막대기 시작, ()를 만나면 자르기(: 표현을 어떻게 하지?)
# 3 + 2 + 2
# 5 + 5
# 언제 카운트하지...
# 레이저를 만나기까지 '('를 스택에 쌓던가 카운트 하는 것이 직관적이지 않아서 어려웠다..

# currents_bars = 현재 쌓인 막대기 수, 스택의 크기
# total_pieces = 잘린 조각의 총합
# ( 를 만났을 때
#   > 막대기인지, 레이저인지 모르므로 쇠막대기라고 생각하고 스택에 쌓기
#   > currents_bars += 1
# ) 를 만났을 때
#   > 판단 기준 : 바로 직전 문자 s[i-1]이 ( 이라면 레이저
#   > s[i-1] == '('
#       > current_bars -= 1
#       > total_pieces += current_bars <----이 부분이 이해가 안 됨
#   > s[i-1] == ')'
#       > 쇠막대기가 끝난 것임, 막대기의 마지막 한 조각이 생긴다는 것?
#       > current_bars -= 1 그래서 왜 한 조각을 빼는지 이해가 안 감
#       > total_pieces += 1 그리고 왜 한 조각을 추가하는지 이해가 안 감(잘려진 거여서 그런가)

T = int(input())

for tc in range(1, T+1):
    s = input()

    currents_bars = 0
    total_pieces = 0

    for i in range(len(s)):
        if s[i] == "(":
            currents_bars += 1
        else:
            #s[i] == ")"
            currents_bars -= 1
            # 레이저일 경우
            if s[i-1] == "(":
                total_pieces += currents_bars
            # 계속 막대기일 경우
            else:
                # s[i-1] == ")"
                total_pieces += 1 # 꼬다리 잘린 것 하나 추가

    print(f'#{tc} {total_pieces}')



