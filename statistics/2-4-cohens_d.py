import math, thinkstats2, nsfg
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome==1]

firsts = live[live.birthord==1]
others = live[live.birthord!=1]

mean_f=firsts.totalwgt_lb.mean()
mean_o=others.totalwgt_lb.mean()

var_f=firsts.totalwgt_lb.var()
var_o=others.totalwgt_lb.var()

d=thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

print('First babies average weight', mean_f)
print('Other babies average weight', mean_o)

print('Difference in weight between first and other babies, in oz:',(mean_f-mean_o)*16)

print('Difference in weight between first and other babies, % :',(mean_f-mean_o)*100/mean_o)

print('First babies variance', var_f)
print('Other babies variance', var_o)


print('Cohen d for weight', d)

n_f=len(firsts)
n_o=len(others)

pooled_var=(n_f*var_f + n_o*var_o)/(n_f+n_o)

d2=(mean_f - mean_o)/math.sqrt(pooled_var)

print('Manual Cohen d for weight', d2)


d3=thinkstats2.CohenEffectSize(firsts.prglngth, others.prglngth)
print('Cohen d for pregnancy length', d3)

