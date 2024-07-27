from collections import deque
import sys 

num = int(input())
queue = deque([])
# queue = []
# 양방향 큐인 deque로 append, pop 속도 개선

for i in range(num):
  # command = input().split()
  # 참고 : https://yeomss.tistory.com/120
  command = sys.stdin.readline().split()

  if command[0] == 'push': queue.append(command[1])
  elif command[0] == 'pop':
    if len(queue) > 0:
      # 그냥 pop하면 맨 마지막 값을 삭제, pop(index) 해도 시간을 초과
      print(queue.popleft())  
    else:
      print(-1)
  elif command[0] == 'front':
    print(queue[0] if len(queue) > 0 else -1)
  elif command[0] == 'back':
    print(queue[-1] if len(queue) > 0 else -1)
  elif command[0] == 'size':
    print(len(queue))
  elif command[0] == 'empty':
    print(0 if len(queue) > 0 else 1)
