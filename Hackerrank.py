
# coding: utf-8

# # HACKER RANK 
# 
# 
# ### MATRIX DIAGONAL SUMMATION PROBLEM

# In[ ]:


n = input()
m =[]
for i in range(int(n)):
    inp = list(map(int,input().split()))
    m.append(inp)
s1 = 0
for i,j in zip(range(len(m)),range(len(m))):
    if( i == j):
        s1 += m[i][j]
s2 =0
for i,j in zip(range(len(m)),range(len(m)-1,-1,-1)):
    s2 += m[i][j]

print(abs(s1-s2))


# ### Precision handling Problem

# In[1]:


n = input()
inp = list(map(int,input().split()))
p=0.0
n=0.0
z=0.0
l = float(len(inp))
for i in inp:
    if(i > 0):
        p +=1
    elif(i < 0):
        n +=1
    elif(i == 0):
        z +=1
print("%.6f"%(p/l),"%6f"%(n/l),"%.6f"%(z/l))


# ### Min Max Problem

# In[18]:


inp = list(map(int,input().split()))
l1 = sorted(inp)
sum_mini = 0
for i in range(0,len(l1)-1):
    sum_mini += l1[i]

sum_maxi = 0
for i in range(1,len(l1)):
    sum_maxi += l1[i]
print(sum_mini,end=' ')
print(sum_maxi)


# ### Cake Candle Problem

# In[4]:


n = input()
inp = list(map(int,input().split()))
m =max(inp)
sort_inp = sorted(inp)
c =0 
for i in range((len(inp))-1,-1,-1):
    if(sort_inp[i] == m):
        c +=1
    elif(inp[i]<m):
        break
print(c)


# ### Grading Problem

# In[2]:


n = input()
inp =[]
for i in range(int(n)):
    i = input()
    inp.append(int(i))
for i in range(len(inp)):
    f = int(inp[i]/5)+1
    sub = (f*5) - (inp[i])
    if(sub > 2):
        print(inp[i])
    elif(inp[i]<38):
        print(inp[i])
    else:
        print(f*5)
    


# ## Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# 
# ## Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
# 
# 

# In[5]:


n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
s = 0
for i in student_marks.keys():
    if query_name == i:
        for j in student_marks[query_name]:
            s+=j
        avg = s/len(student_marks[name])
print("%.2f" % round(avg,2))

