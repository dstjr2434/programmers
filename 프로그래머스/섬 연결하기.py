# # 0번 섬과 1번섬.. 비용 1
# arr = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

# # 배열을 i-2번째에 있는 값을 토대로 배열을 정렬한다.
# arr.sort(key=lambda x: x[2])
# arr.sort(key=)
# key= 등호 뒤에있는것을 기준으로 나누겠다. 

# print(arr)

def solution(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # 집합
    while len(routes)!=n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return ans

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))