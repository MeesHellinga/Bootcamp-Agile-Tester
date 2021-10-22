

with open("woorden.txt", "rt") as f: #opent een context manager
    f_contents = f.read(100)
    print(f.tell())

    f.seek(0)


    #while len(f_contents) >0:
    #    print(f_contents, end='')
    #    f_contents = f.read(100)


    #for line in f:
    #    print(line, end='')
    
    #f_contents = f.readline()
    #print (f_contents)
    #f_contents = f.readline()
    #print (f_contents)



