import random, copy


area_map = [
     [0,   66,  21,   3,    500,  26],
     [66,  0,   35,   115,  36,   65],
     [21,  35,  0,    450,  448,  846],
     [3,   115, 450,  0,    65,   478],
     [500, 36,  448,  65,   0,    258],
     [26,  65,  846,  478,  258,  0] ]


# In[21]:


# How to generate random chromosome
a=random.sample(range(0,6),6)
a


# In[22]:


#An example of fitnec calculation from a chromosome
ch1=[1,4,5,0,3,2]
# 36 + 258 + 26 + 3+ 450
sum=0
for i in range(len(ch1)-1):
    sum+=area_map[ch1[i]][ch1[i+1]]
sum

-> Each and every step is based on function i.e.
-> function for chromosome
-> functon for fitness calculation
-> function for population
-> crossover , mutation, main
Important Note: - Remember one thing do maintain that there must be unique cities in chromosome after crossover and mutation
# ### Q1 Solution

# In[23]:


class Q1:
    def __init__(self):
        self.populationSize = 20
        self.visited=[]
        self.combinations=[]
        self. area_map = [
        [0,   66,  21,   3,    500,  26],
        [66,  0,   35,   115,  36,   65],
        [21,  35,  0,    450,  448,  846],
        [3,   115, 450,  0,    65,   478],
        [500, 36,  448,  65,   0,    258],
        [26,  65,  846,  478,  258,  0] ]
        
    def generate_Chromosome(self):
        a=random.sample(range(0,6),6)
        
#         while a in self.visited:         unique chromosome check but code doesnt go further than 36 iterations with it
#             a=random.sample(range(0,6),6)
        self.visited.append(a)
        return a
    
    def fitness_func(self,ch1):
        sum=0
        for i in range(len(ch1)-1):
            sum+=area_map[ch1[i]][ch1[i+1]]
        return sum
    
    def Tornument_Selection(self):
        self.combinations = sorted(self.combinations, key=lambda tup: tup[1])
        return self.combinations[0],self.combinations[1]
    
    def CrossOver(self,ch1,ch2):
        newch1 = ch1
        newch2= ch2
        if newch1[3:] in ch2[3:]:
            newch1[3:]=ch2[3:]
        if newch2[3:] in ch1[3:]:
            newch2[3:]=ch1[3:]
        return newch1,newch2
    
    def Mutate(self,ch1):
        ch=copy.copy(ch1)
        x=random.randint(0,100)
        if x%6.5 == 0: #almost 15.33% probability
            n = random.randint(0,5)
            m = random.randint(0,5)
            while n==m:
                   m = random.randint(0,5)
            temp = ch[n]
            ch[n] = ch[m]
            ch[m]=temp
        return ch
    
    def main(self):
        for i in range(100):
            print ("\n\nIteration : ",i,"\n\n")
            for j in range(self.populationSize):
                k=self.generate_Chromosome()
                l=self.fitness_func(k)
                self.combinations.append((k,l))
            a,b = self.Tornument_Selection()
            a=a[0]
            b=b[0]
            c,d = self.CrossOver(a,b)
            e = self.Mutate(c)
            f = self.Mutate(d)
            c_fit = self.fitness_func(c)
            d_fit = self.fitness_func(d)
            e_fit = self.fitness_func(e)
            f_fit = self.fitness_func(f)
            if c_fit < self.fitness_func(a):
                print("Replacing with combination c ", (c,c_fit))
                self.combinations[0]=(c,c_fit)
            elif c_fit < self.fitness_func(b):
                print("Replacing with combination c ", (c,c_fit))
                self.combinations[1]=(c,c_fit)
            if d_fit < self.fitness_func(a):
                print("Replacing with combination d ", (d,d_fit))
                self.combinations[0]=(d,d_fit)
            elif d_fit < self.fitness_func(b):
                print("Replacing with combination d ", (d,d_fit))
                self.combinations[1]=(d,d_fit)
            if e_fit < self.fitness_func(a):
                print("Replacing with combination e ", (e,e_fit))
                self.combinations[0]=(e,e_fit)
            elif e_fit < self.fitness_func(b):
                print("Replacing with combination e ", (e,e_fit))
                self.combinations[1]=(e,e_fit)
            if f_fit < self.fitness_func(a):
                print("Replacing with combination f ", (f,f_fit))
                self.combinations[0]=(f,f_fit)
            elif f_fit < self.fitness_func(b):
                print("Replacing with combination f ", (f,f_fit))
                self.combinations[1]=(f,f_fit)
            print(self.combinations[0],self.combinations[1])
    


# In[24]:


x=Q1().main()