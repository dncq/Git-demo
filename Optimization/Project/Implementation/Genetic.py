import random
import time
import copy
with open (r"C:\Users\DELL\OneDrive\Máy tính\Test data\N_5_K_2.txt") as f:
    f=f.read()
    lines=f.split("\n")
nk=[int(i) for i in lines[0].split(" ")]
n,k = nk[0],nk[1]
repair_time=[i for i in lines[1].split(" ")]
t=[int(repair_time[i]) for i in range(n)]
c=[[j for j in lines[i+2].split(" ") ]for i in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        c[i][j]=int(c[i][j])
        
def working_time_func(emp,i):
    cus_list=emp[i]
    route=[0]+emp[i]+[0]
    mt=0
    trt=0
    for i in cus_list:
        mt+=t[i-1]
    for i in range(len(route)-1):
        trt+=c[route[i]][route[i+1]]
    return mt+trt
def working_time_matrix(emp):
    f=[working_time_func(emp,i) for i in range(len(emp))]
    return f
def fitness_func(emp):
    f=copy.deepcopy(working_time_matrix(emp))
    f.sort()
    return f[-1]
def best_emp(emp):
    return emp[working_time_matrix(emp).index(fitness_func(emp))]
def remove_duplicate(l):
    queue=[]
    for i in l: 
        if i not in queue:
            queue.append(i)
    return queue
def choose2point(k):
    l=list(range(k))
    twopoint=[]
    for i in range(2):
        p=random.choice(l)
        twopoint.append(p)
        l.remove(p)
    twopoint.sort()
    return twopoint
def pick2(m):
    n=copy.deepcopy(m)
    l=len(n)
    list_of_pairs=[]
    while l>1:
        pair=[]
        for i in range(2):
            invi=random.choice(n)
            pair.append(invi)
            n.remove(invi)
        list_of_pairs.append(pair)
        l=len(n)
    return list_of_pairs
def shuffle_k_sum_n(k,n):
    list=[]
    while k>1:
        if n>0:
            x=int(n*random.random())
            list.append(x)
            n=n-x
            k=k-1
        else:
            list.append(0)
            k=k-1
    list.append(n)
    return list
class chromosome:
    def __init__(self,n=None,k=None,gene_code=[]):
        self.n=n
        self.k=k
        self.gene_code=gene_code
    def splitcode(self):
        return [self.gene_code[:self.n],self.gene_code[self.n:]]
    def decode(self):
        emp=[[] for i in range(self.k)]
        control_code=[]
        cus_order,emp_list=self.splitcode()
        for i in range(self.k):
            for j in range(emp_list[i]):
                control_code.append(i)
        for i in range(self.n):
            emp[control_code[i]].append(cus_order[i])
        return emp
class Genetic_algorithm:
    def __init__(self,n_customer,k_employees,num_inv,fitness_func=None,iter_num=0,rate=0.8):
        self.n_customer=n_customer
        self.k_employees=k_employees
        self.num_inv=num_inv
        self.fitness_function=fitness_func
        self.iter=iter_num
        self.rate=rate
        population_list=[]
        for j in range(num_inv):
         while True:
            cus_order=list(range(1,n_customer+1))
            random.shuffle(cus_order)
            emp_list=shuffle_k_sum_n(k_employees,n_customer)
            inv=cus_order+emp_list
            if inv not in population_list:
                population_list.append(inv)
                break
        self.population=population_list
        self.remember=copy.deepcopy(self.population)
    def get_fitness_scores(self):
        self.chromo=[chromosome(self.n_customer,self.k_employees,self.population[i]) for i in range(len(self.population))]
        self.emps=[i.decode() for i in self.chromo]
        fitness_values=[self.fitness_function(i) for i in self.emps]
        return fitness_values

    def update_population(self):
        n1=self.num_inv
        list_of_invs=[(self.population[i],self.get_fitness_scores()[i]) for i in range(len(self.population))]
        list_of_invs.sort(key=lambda x: x[1])
        remove=list_of_invs[n1:]
        remove_part=[i[0] for i in remove]
        for i in remove_part:
            self.population.remove(i)
            self.remember.append(i)
        return list_of_invs[0]
    def selection(self):
        self.copy_fitness_scores=copy.deepcopy(self.get_fitness_scores())
        sel_num=int(self.num_inv*0.5)
        if sel_num==0:
            sel_num+=1
        self.copy_fitness_scores.sort()
        selection=self.copy_fitness_scores[:sel_num]
        selection_ind=[self.get_fitness_scores().index(i) for i in selection]
        return remove_duplicate(selection_ind)
    @staticmethod
    def crossover(par1,par2,n,k):
        code1=chromosome(n,k,par1)
        code2=chromosome(n,k,par2)
        cus_order1,emp_list1=code1.splitcode()
        cus_order2,emp_list2=code2.splitcode()
        copy_cus_order1=copy.deepcopy(cus_order1)
        copy_emp_list2=copy.deepcopy(emp_list2)
        
        child=copy_cus_order1+copy_emp_list2
        return child
    @staticmethod
    def mutation1(par,n,k):
        code=chromosome(n,k,par)
        decode=code.splitcode()
        cus_order=decode[0]
        emp_list=decode[1]
        copy_emp=copy.deepcopy(emp_list)
        copy_emp_ori=copy.deepcopy(emp_list)
        copy_emp.sort()
        if copy_emp[0]==copy_emp[-1]:
         x=emp_list.index(copy_emp[0])
         y=emp_list.index(copy_emp[-1])+1
        else:
         x=emp_list.index(copy_emp[0])
         y=emp_list.index(copy_emp[-1])
        sum=copy_emp_ori[x]+copy_emp_ori[y]
        rate=random.random()
        copy_emp_ori[x]=int(sum*rate)
        copy_emp_ori[y]=sum-copy_emp_ori[x]
        child=cus_order+copy_emp_ori
        return child
    @staticmethod
    def mutaion2(par,n,k):
        code=chromosome(n,k,par)
        decode=code.splitcode()
        cus_order=decode[0]
        emp_list=decode[1]
        copy_cus_order=copy.deepcopy(cus_order)
        random.shuffle(copy_cus_order)
        child=copy_cus_order+emp_list
        return child
    def make_new_population(self):
        select_list=[self.population[i] for i in self.selection()]
        n=len(select_list)
        cross_num=int(n*self.rate)
        child=[]
        childcross=[]  
        if cross_num>1:
            parents=pick2(select_list[:cross_num])
           
            for pair in parents:
             new_child1=self.crossover(pair[0],pair[1],self.n_customer,self.k_employees) 
             if new_child1 not in self.remember:
                 childcross.append(new_child1)
        if childcross!=[]:
            child+=childcross
        else:
            cross_num=0
        if cross_num%2!=0:
            mutate_invs=select_list[cross_num-1:]
        else:
            mutate_invs=select_list[cross_num:]
        if mutate_invs !=[]:
            childmutate=[]
            for inv in mutate_invs:
             new_child2=self.mutation1(inv,self.n_customer,self.k_employees) 
             new_child3=self.mutaion2(inv,self.n_customer,self.k_employees) 
             if new_child2 not in self.remember:
                 childmutate.append(new_child2)
             if new_child3 not in self.remember:
                childmutate.append(new_child3)
            child+=childmutate
        new_population=self.population+child
        return new_population
    def iterations(self):
        evolve=[]
        for i in range(self.iter):
            self.population=self.make_new_population()
            evolve.append(self.update_population())
        return evolve[-1]
ga = Genetic_algorithm(n,k,100,fitness_func,1000)
print(ga.iterations())
