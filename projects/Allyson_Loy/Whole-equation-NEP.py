
# coding: utf-8

# In[2]:

#whole epuation
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np

beta = .01 #
delta = 1 #lambda
theta = .25 #flushing
alpha = .0063 #infectivity 63/10,000 
n = 2400
m = 400
gamma = n/m #gallery ratio



def IM(x):
    pi = 0.0045 #fraction infected
    answer=[]
    total_infection = n*pi
    i=0
    while i<x:
        if n >= total_infection:
            di = (delta * gamma * pi) - (delta * gamma * beta)*(1-(1-pi)*(1-theta))
            infected_rate = di*alpha
            infected_ppl = infected_rate * n
            total_infection += infected_ppl
            answer.append(total_infection)
            pi = total_infection / n
            i+=1
        else:
            print("total infection exceeds total number of people")
            print(answer)
            print("Completed " + str(i) + " cycles")
            break
    print(total_infection)
    return answer


days= 111
days_list=list(range(1, days+1))
plt.xlabel('Days')
plt.ylabel('Number of Infected Individuals')
y = IM(days)
t = np.array(days_list)
plt.plot(t, y)
plt.ylim([0, 300])
plt.savefig('NoNEP.jpg')


# In[8]:

#whole***********NEP
#March 26
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np

beta = .01 #
delta = 1 #lambda
theta = .25 #flushing
alpha = .0063 #infectivity 63/10,000 
n = 2400
m = 400
gamma = n/m #gallery ratio
n2 = 1610
gamma2 = n2/m



def IM(x):
    pi = 0.0045 #fraction infected
    answer=[]
    total_infection = n*pi
    i=0
    while i<x:
        if n >= total_infection:
            di = (delta * gamma * pi) - (delta * gamma * beta)*(1-(1-pi)*(1-theta))
            infected_rate = di*alpha
            infected_ppl = infected_rate * n
            total_infection += infected_ppl
            answer.append(total_infection)
            pi = total_infection / n
            i+=1
        else:
            print("total infection exceeds total number of people")
            print(answer)
            print("Completed " + str(i) + " cycles")
            break
    print(total_infection)
    return answer



def IM_nep(x):
    total_infection2 = 78.61421051203561
    pi = total_infection2 / n2 #fraction infected
    answer=[]
    i=0
    while i<x:
        if n2 >= total_infection2:
            di = (delta * gamma2 * pi) - (delta * gamma2 * beta)*(1-(1-pi)*(1-theta))
            infected_rate = di*alpha
            infected_ppl = infected_rate * n2
            total_infection2 += infected_ppl
            answer.append(total_infection2)
            pi = total_infection2 / n2
            i+=1
        else:
            print("total infection exceeds total number of people")
            print(answer)
            print("Completed " + str(i) + " cycles")
            break
    print(total_infection2)
    return np.array(answer)

days= 74 #days between jan 11 and march 26
days_list=list(range(1, days+1))

nep = 37 #days between march 26 and may 2
nep_days = list(range(75, 112))



y = IM(days)
t = np.array(days_list)
plt.xlabel('Days')
plt.ylabel('Number of Infected Individuals')
plt.plot(t, y)
y_nep= IM_nep(nep)
t_nep = np.array(nep_days)
plt.plot(t_nep, y_nep)
plt.ylim([0, 300])
plt.savefig("March.jpg")





# In[ ]:




# In[7]:

#whole***********NEP
#Jan 26
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np

beta = .01 #
delta = 1 #lambda
theta = .25 #flushing
alpha = .0063 #infectivity 63/10,000 
n = 2400
m = 400
gamma = n/m #gallery ratio
n2 = 1610
gamma2 = n2/m



def IM(x):
    pi = 0.0045 #fraction infected
    answer=[]
    total_infection = n*pi
    i=0
    while i<x:
        if n >= total_infection:
            di = (delta * gamma * pi) - (delta * gamma * beta)*(1-(1-pi)*(1-theta))
            infected_rate = di*alpha
            infected_ppl = infected_rate * n
            total_infection += infected_ppl
            answer.append(total_infection)
            pi = total_infection / n
            i+=1
        else:
            print("total infection exceeds total number of people")
            print(answer)
            print("Completed " + str(i) + " cycles")
            break
    print(total_infection)
    return answer



def IM_nep(x):
    total_infection2 = 14.306568740702692
    pi = total_infection2 / n2 #fraction infected
    answer=[]
    i=0
    while i<x:
        if n2 >= total_infection2:
            di = (delta * gamma2 * pi) - (delta * gamma2 * beta)*(1-(1-pi)*(1-theta))
            infected_rate = di*alpha
            infected_ppl = infected_rate * n2
            total_infection2 += infected_ppl
            answer.append(total_infection2)
            pi = total_infection2 / n2
            i+=1
        else:
            print("total infection exceeds total number of people")
            print(answer)
            print("Completed " + str(i) + " cycles")
            break
    print(total_infection2)
    return np.array(answer)

days= 15 #days between jan 11 and jan 26
days_list=list(range(1, days+1))

nep = 96 #days between jan 26 and may 2
nep_days = list(range(16, 112))



y = IM(days)
t = np.array(days_list)
plt.xlabel('Days')
plt.ylabel('Number of Infected Individuals')
plt.plot(t, y)
y_nep= IM_nep(nep)
t_nep = np.array(nep_days)
plt.plot(t_nep, y_nep)
plt.ylim([0, 300])
plt.savefig("Jan.jpg")


# In[4]:

#whole***********NEP
#Feb 26
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np

beta = .01 #
delta = 1 #lambda
theta = .25 #flushing
alpha = .0063 #infectivity 63/10,000 
n = 2400
m = 400
gamma = n/m #gallery ratio
n2 = 1610
gamma2 = n2/m



def IM(x):
    pi = 0.0045 #fraction infected
    answer=[]
    total_infection = n*pi
    i=0
    while i<x:
        if n >= total_infection:
            di = (delta * gamma * pi) - (delta * gamma * beta)*(1-(1-pi)*(1-theta))
            infected_rate = di*alpha
            infected_ppl = infected_rate * n
            total_infection += infected_ppl
            answer.append(total_infection)
            pi = total_infection / n
            i+=1
        else:
            print("total infection exceeds total number of people")
            print(answer)
            print("Completed " + str(i) + " cycles")
            break
    print(total_infection)
    return answer



def IM_nep(x):
    total_infection2 = 31.920915818804634
    pi = total_infection2 / n2 #fraction infected
    answer=[]
    i=0
    while i<x:
        if n2 >= total_infection2:
            di = (delta * gamma2 * pi) - (delta * gamma2 * beta)*(1-(1-pi)*(1-theta))
            infected_rate = di*alpha
            infected_ppl = infected_rate * n2
            total_infection2 += infected_ppl
            answer.append(total_infection2)
            pi = total_infection2 / n2
            i+=1
        else:
            print("total infection exceeds total number of people")
            print(answer)
            print("Completed " + str(i) + " cycles")
            break
    print(total_infection2)
    return np.array(answer)

days= 46 #days between jan 11 and feb 26
days_list=list(range(1, days+1))

nep = 65 #days between feb 26 and may 2
nep_days = list(range(47, 112))



y = IM(days)
t = np.array(days_list)
plt.xlabel('Days')
plt.ylabel('Number of Infected Individuals')
plt.plot(t, y)
y_nep= IM_nep(nep)
t_nep = np.array(nep_days)
plt.plot(t_nep, y_nep)
plt.ylim([0, 300])
plt.savefig('Feb.jpg')


# In[5]:

#whole***********NEP
#April 26
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np

beta = .01 #
delta = 1 #lambda
theta = .25 #flushing
alpha = .0063 #infectivity 63/10,000 
n = 2400
m = 400
gamma = n/m #gallery ratio
n2 = 1610
gamma2 = n2/m



def IM(x):
    pi = 0.0045 #fraction infected
    answer=[]
    total_infection = n*pi
    i=0
    while i<x:
        if n >= total_infection:
            di = (delta * gamma * pi) - (delta * gamma * beta)*(1-(1-pi)*(1-theta))
            infected_rate = di*alpha
            infected_ppl = infected_rate * n
            total_infection += infected_ppl
            answer.append(total_infection)
            pi = total_infection / n
            i+=1
        else:
            print("total infection exceeds total number of people")
            print(answer)
            print("Completed " + str(i) + " cycles")
            break
    print(total_infection)
    return answer



def IM_nep(x):
    total_infection2 = 233.3434062882629
    pi = total_infection2 / n2 #fraction infected
    answer=[]
    i=0
    while i<x:
        if n2 >= total_infection2:
            di = (delta * gamma2 * pi) - (delta * gamma2 * beta)*(1-(1-pi)*(1-theta))
            infected_rate = di*alpha
            infected_ppl = infected_rate * n2
            total_infection2 += infected_ppl
            answer.append(total_infection2)
            pi = total_infection2 / n2
            i+=1
        else:
            print("total infection exceeds total number of people")
            print(answer)
            print("Completed " + str(i) + " cycles")
            break
    print(total_infection2)
    return np.array(answer)

days= 105 #days between april 26 and march 26
days_list=list(range(1, days+1))

nep = 6
nep_days = list(range(106, 112))



y = IM(days)
t = np.array(days_list)
plt.xlabel('Days')
plt.ylabel('Number of Infected Individuals')
plt.plot(t, y)
y_nep= IM_nep(nep)
t_nep = np.array(nep_days)
plt.plot(t_nep, y_nep)
plt.ylim([0, 300])
plt.savefig('April.jpg')


# In[6]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np


plt.xlabel('Days')
plt.ylabel('Number of Infected Individuals')

jan = np.array([14,116])
t_j=np.array([15, 111])
plt.plot(t_j, jan, 'b-', label = 'Jan')

feb = np.array([32,144])
t_f=np.array([46, 111])
plt.plot(t_f, feb, 'r-', label = 'Feb')

march = np.array([79, 191])
t_m=np.array([74, 111])
plt.plot(t_m, march, 'g-', label = 'March')

april = np.array([233, 270])
t_a=np.array([105, 111])
plt.plot(t_a, april, 'y-', label = 'April')

may = np.array([290])
t_may=np.array([111])
plt.plot(t_may, may, 'p-', label = 'May')
plt.ylim([0, 300])
plt.legend(loc = 0)
plt.savefig('Totals.jpg')


# In[ ]:



