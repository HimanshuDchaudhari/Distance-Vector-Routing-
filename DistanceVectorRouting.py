import numpy as np

node = int(input("Enter Node :-"))

graph = np.full((node,node),-1)
ch=['A','B','C','D','E','F','G']

for i in range(node):
    for j in range(node):
        if i==j:
            graph[i][j]=0;
            
        if graph[i][j]==-1:
            print("\nEnter the Distance Between ",ch[i],' - ',ch[j]," : ")
            t = int(input())
            graph[i][j]=graph[j][i]=t


via = np.full((node,node),-1)

print("\n After Initialization")
    # Display table initialization 
for i in range(node):
    print("\n",ch[i]," Table")
    print("\nNode\tDist\tVia");
    for j in range(node):
        print("\n",ch[j],"\t",graph[i][j],"\t",via[i][j])

sh = np.full((node,node,node),-1)
for i in range(node):
    for j in range(node):  
        for k in range(node):
            # Check if edge is present or not
            if (graph[i][j]>-1) and (graph[j][k]>-1):
                sh[i][j][k]=graph[j][k]+graph[i][j];    
            else:
                sh[i][j][k]=-1;

for i in range(node):
    print("\n\n For ",ch[i])
    for j in range(node):
        print("\n From  ",ch[j])
        for k in range(node):
            print("\n ",ch[k]," ",sh[i][j][k])

final = np.full((node,node),-1)
for i in range(node):
    for j in range(node):
        #copy initial value from input graph
        final[i][j]=graph[i][j]
        via[i][j] = i
        
        for k in range(node):
            if (final[i][j]>sh[i][k][j]) or (final[i][j] == -1):
                if sh[i][k][j]>-1:
                    final[i][j] = sh[i][k][j]
                    via[i][j]=k
        if final[i][j] == -1:
            for k in range(node):
                if (final[i][k]!=-1) or (final[k][j]!=-1):
                    if (final[i][j]==-1) or ((final[i][j]!=-1) and (final[i][j]>final[i][k]+final[k][j])):
                        if (final[i][k]+final[k][j])>-1:
                            final[i][j] = final[i][j] + final[k][j]
                            via[i][j]=k
                        


print("\n After Update :")
# Display table Updation 
for i in range(node):
    print("\n",ch[i]," Table")
    print("\nNode\tDist\tVia")
    for j in range(node):
        print("\n",ch[j],"\t",final[i][j],"\t",end="")
        if(i==via[i][j]):
            print("-")
        else:
            print(ch[via[i][j]])
