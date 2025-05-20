def first_uniq_char(string: str) -> int: 
  d = {}

  for idx, ch in enumerate(string):
    if not d.get(ch):
      d[ch] = [idx, 1]
    else:
      d[ch][1] += 1

  for ch, val in d.items():
    if val[1] == 1:
      return val[0]

  return -1

test1 = "leetcode" # output expected: 0
test2 = "loveleetcode" # output expected: 2
test3 = "aabb" # output expected: -1

print(first_uniq_char(test1))
print(first_uniq_char(test2))
print(first_uniq_char(test3))

