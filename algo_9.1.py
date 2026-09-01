# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
# [입력]
#
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
#
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
#
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
#
# [출력]
#
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
#
# T = int(input())
#
# for t in range(1,T+1):
#     N = int(input())
#     num = list(map(int, input().split()))
#
#     max = num[0]
#     min = num[0]
#     for i in range(len(num)):
#         if num[i] > max:
#             max = num[i]
#         if num[i] < min:
#             min = num[i]
#
# result = max - min
# print(f'#{t} {result}')

# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
'''
카드 장수 N, 그 값은 0~9 사이 K < 10
for문 카드 순회
card[i] ,
[4,9,6,7,6]
card_count = [0] * [9+1]

'''
