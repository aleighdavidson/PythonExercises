p = open('pelican.txt', 'a')
p.write("A wonderful bird is the pelican,\n")
p.write("His bill holds more than his belican.\n")
lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
p.writelines(lines)
