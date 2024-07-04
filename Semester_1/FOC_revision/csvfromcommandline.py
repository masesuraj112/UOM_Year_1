import sys
print(f"sys.argv[0] = {sys.argv[0]}")
print(f"sys. argv [1] = {sys.argv[1]}")
print(f"sys. argv [2] = {sys.argv[2]}")
fp = open(sys.argv[1])
stuff = fp.readlines()
fp.close()
print(f"stuff has {len(stuff)} lines")
print(stuff)
