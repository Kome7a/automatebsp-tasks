s = str(input('Enter a string\n'))
chars = list(s)
s_len = len(s)
reversed_str = ['' for i in range(s_len)]

for i in range(0, s_len // 2):
    opposite_idx = s_len - i - 1
    reversed_str[opposite_idx] = s[i]
    reversed_str[i] = s[opposite_idx]

if s_len % 2 != 0:
    mid = s_len // 2
    reversed_str.insert(mid, s[mid])

print(''.join(reversed_str))
