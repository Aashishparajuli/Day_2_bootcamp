with open('sample.txt','w+') as file:
    #pass
    content = file.readlines()
    for line in content:
        print(line.strip().capitalize())
        file.write(line)
   # print(content)