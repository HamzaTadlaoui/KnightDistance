import numpy 

ch = []
cvg = 20
for i in range(cvg+4):
  ch.append([])
  for j in range(cvg+4):
    ch[i].append(-1)
count =(cvg+4)*(cvg+4)-1
ch[2][2]=0
ch[3][3]=2
for v in range(cvg+7):
  if count ==0:
    break
  for x in range(cvg):
    i = x+2
    for z in range(cvg):
      j=z+2
      if ch[i][j]==v:
        #if(v!= numpy.ceil(max(x/2,z/2,(x+z)/3))):
          #print(str(x)+" "+str(z)+" "+ " = " +str(v) + " =/= " +str(numpy.ceil(max(x/2,z/2,(x+z)/3))))
        if ch[i+2][j+1]==-1:
          ch[i+2][j+1] = v+1
          count =count -1
        if(ch[i+2][j-1]==-1):
          ch[i+2][j-1] = v+1
          count =count -1
        if(ch[i-2][j+1]==-1):
          ch[i-2][j+1] = v+1
          count =count -1
        if(ch[i-2][j-1]==-1):
          ch[i-2][j-1] = v+1
          count =count -1
        if(ch[i+1][j+2]==-1):
          ch[i+1][j+2] = v+1
          count =count -1
        if(ch[i+1][j+-2]==-1):
          ch[i+1][j-2] = v+1
          count =count -1
        if(ch[i-1][j+2]==-1):
          ch[i-1][j+2] = v+1
          count =count -1
        if(ch[i-1][j-2]==-1):
          ch[i-1][j-2] = v+1
          count =count -1

for x in range(cvg):
  i = x+2
  for z in range(cvg):
    j=z+2
    if ch[i][j]<10:
      print(" ", end ="" )
    print(ch[i][j] , end ="|" )
  print("\n")
'''
f = open("doc.csv", "a")


for x in range(cvg):
  for z in range(cvg):
    f.write(str(x)+","+str(z)+","+str(ch[x+2][z+2])+"\n")


f.close()'''