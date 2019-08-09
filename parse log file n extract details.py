f=open('C:\\Users\\HP\\Desktop\\mediif\\log.txt')
f.seek(0)
a=f.readlines()
result1 = [i for i in a if i.startswith('Errors')]
result2 = [i for i in a if i.startswith('warnings')]
finalist = result1 + result2
finalist
with open('output.txt', 'w') as f:
    for item in finalist:
        f.write("%s\n" % item)
