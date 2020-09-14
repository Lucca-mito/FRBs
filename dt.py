import os

for filename in os.listdir('data'):
    if not filename.endswith(".txt"): continue
#    print(filename[:-4])
    with open('data/'+filename) as fp:
        t = [float(line.split()[0]) for line in fp.readlines()]
        print(filename[:-4] + ": " + str(t[1] - t[0]))
        
#        lines = fp.readlines()
#        prev = None
#        is_first = True
#        for line in lines:
#            time = float(line.split()[0])
#            if (is_first): is_first = False
#            else: print(time - prev)
#            prev = time
