#!/usr/bin/env python
# coding: utf-8

# In[8]:


from pulp import *
advisors = ['A','B','C','D','E', 'F', 'G']

# arbitrary weight score for each advisory, the objective is to talk to as many advisors as possible which increases max score.
advisory_weight      = dict( zip( advisors, [100, 80, 10, 30, 75, 90, 100] ) )
advisory_cost      = dict( zip( advisors, [10, 20, 80, 90, 100, 100, 100] ) )

n           = len( advisors )
tw = 10 
max_cost_per_allowed = 200

x     = pulp.LpVariable.dicts( "x", indexs = advisors, cat='Binary', indexStart=[] )
prob  = pulp.LpProblem( "Minimalist_example", pulp.LpMaximize )
prob += pulp.lpSum( [ x[i]*advisory_weight[i] for i in advisors ]  ), " Objective is maximize overall weightage  "
prob += pulp.lpSum( [ x[i]*advisory_weight[i] for i in advisors ] ) >= 50 # minimum advisory weight to use is 50. 
prob += pulp.lpSum( [ x[i]*advisory_cost[i] for i in advisors ] ) >= 0
prob += pulp.lpSum( [ x[i]*advisory_cost[i] for i in advisors ] ) <=  max_cost_per_allowed
              
prob.solve()

print("Status:", LpStatus[prob.status])

     
for v in prob.variables():    
    print(v.name +"---"+str(v.varValue))         


# In[ ]:




