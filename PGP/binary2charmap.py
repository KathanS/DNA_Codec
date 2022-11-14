data = input()
mappingData = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F']
stream = data.split(" ")
need = len(stream)%5
need = 5-need
if(need !=0):
    for i in range(0,need):
        stream.append('0')
converted = []
for i in range(0,len(stream),5):
    ans = 0
   
    cnt = 0
    for j in range(i,i+5):
        print(j)
        ans += ((int)(stream[j]))*(pow(2,cnt))
        cnt +=1
    ans -=1
    converted.append(mappingData[ans])
print(converted)
    
