# MinMax Multiple Traveling Salesman Problem
# import sys

# def input():
#     [n, M] = [int(x) for x in sys.stdin.readline().split()]
#     s = [int(x) for x in sys.stdin.readline().split()]
#     return n, M, s

# def main():
#     n, M, s = input()
#     seen = set()
#     Q = 0
#     for i in range(n):
#         complement = M - s[i]
#         if complement in seen:
#             Q += 1
#         else:
#             seen.add(s[i])
#     print(Q)

# if __name__ == "__main__":
#     main()

# def compute_hash(s, m):
#     k = len(s)
#     h = 0
#     for i in range(k):
#         h = (h * 256 + ord(s[i])) % m
#     return h

# n, m = map(int, input().split())
# hash_codes = []

# for _ in range(n):
#     s = input().strip()
#     hash_code = compute_hash(s, m)
#     hash_codes.append(hash_code)

# for code in hash_codes:
#     print(code)


# def compute_hash(s, m):

#     hash_code = 0
#     for c in s:
#         hash_code = (hash_code * 256 + ord(c)) % m
#     return hash_code


# def main():

#     n, m = map(int, input().split())
#     hash_codes = []

#     powers_of_256 = [1]
#     for i in range(1, 201):
#         powers_of_256.append((powers_of_256[-1] * 256) % m)

#     for _ in range(n):
#         s = input().strip()
#         hash_code = 0
#         for i in range(len(s)):
#             hash_code = (hash_code + powers_of_256[len(s) - i - 1] * ord(s[i])) % m
#         hash_codes.append(hash_code)

#     for hash_code in hash_codes:
#         print(hash_code)


# if __name__ == '__main__':

