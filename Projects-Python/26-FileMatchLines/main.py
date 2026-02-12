with open('file1.txt','r') as f1, open('file2.txt','r') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

result = [int(num.strip('\n')) for num in lines1 if num in lines2]
print(result)