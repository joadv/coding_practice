# 백준 자료구조 문제집 - 10828 스택
import sys
stack = []
order = ""
num_order = int(sys.stdin.readline().rstrip())
for i in range(num_order):
    order = sys.stdin.readline().rstrip()
    order = order.split(" ")
    if order[0] == "push":
        stack.append(int(order[1]))
    elif order[0] == "pop":
        if stack == []:
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        if stack == []:
            print(1)
        else:
            print(0)
    elif order[0] == "top":
        if stack == []:
            print(-1)
        else:
            print(stack[-1:][0])
# 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다.
# 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.
# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.



