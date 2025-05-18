# s = "Let's take LeetCode contest"
s = "Mr Ding"

def reverseWords(s):
    res = ''
    l, r = 0, 0

    while r < len(s):
        if s[r] != ' ':
            r += 1
        else:
            res += s[l:r+1][::-1]
            r += 1
            l = r

    res += ' '
    res += s[l:r + 2][::-1]
    return res[1:]

print(reverseWords(s))
# print('Hello'[::-1]) para inverter uma string