
import sys

v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i


# find 연산
def find_parent(parent, x):
    # 부모노드와 자식노드 같지 않다면 = 부모노드가 따로 있는 의미니까!
    if parent[x] != x:
        return find_parent(parent, parent[x])  # 그 부모노드를 자식으로 하는 또 다른 부모노드를 재귀적으로 탐색
    # 부모 노드 = 자식노드 -> 해당 노드 리턴
    return x


def union_parent(parent, a, b):
    # a, b 각 부모노드 탐색 - Find 연산
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 각 부모노드 비교 후 부모-자식 관계 형성 - Union 연산
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)


# 각 원소의 루트 노드 출력
print('# 각 원소의 루트 노드들: ', end='')
for i in range(1, v+1):
    root = find_parent(parent, i)
    print(root, end=' ')
print()
# 부모 테이블 출력(직계 부모노드를 의미)
print('# 각 원소의 직계 부모 노드들: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')














import sys

v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        # 부모 테이블에 바로 갱신
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('# 각 원소의 루트노드 출력:', end='')
for i in range(1, v+1):
    root = find_parent(parent, i)
    print(root, end=' ')
print()
print('# 위 find 연산 후 업데이트된 부모 테이블 출력:', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')