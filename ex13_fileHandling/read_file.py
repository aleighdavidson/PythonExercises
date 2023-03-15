p = open("pelican.txt", 'r')
# slurp = p.read()
# print(slurp)
# print(type(slurp))

p_lines = p.readlines()
# print(p_lines)
# print(len(p_lines))

for line in p_lines:
    print(line, end="")
