fin = open("f.txt", "rt")
str = fin.read()
str = str.replace('pyton', 'python')
fin.close()
fin = open("f.txt", "wt")
fin.write(str)
fin.close()
