# O(n) time | O(1) space
# def firstUniqueChar(s):
#     hash_table = {}
#     for char in s:
#         if char in hash_table:
#             hash_table[char] += 1
#         else:
#             hash_table[char] = 1
#
#     for i, char in enumerate(s):
#         if hash_table[char] == 1:
#             return i
#
#     return -1

# O(n^2) time
def firstUniqueChar(s):
    for i, char in enumerate(s):
        if s.index(char) == s.rindex(char):
            return i
    return -1

print(firstUniqueChar('aaron'))
