[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> Python code:
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

Results:
First babies average weight 7.201094430437772
Other babies average weight 7.325855614973262
Difference in weight between first and other babies, in oz: -1.9961789525678455
Difference in weight between first and other babies, % : -1.7030254361073112
First babies variance 2.0180273009157768
Other babies variance 1.9437810258964572
Cohen d for weight -0.088672927072602
Manual Cohen d for weight -0.088672927072602
Cohen d for pregnancy length 0.028879044654449883


Explanantion: Average weight of first babies is 7.2 lb; average weight of other babies is 7.33 lb. The difference is 2oz, or 1.7%, in favor of other babies. Cohen's d for baby weight between these two groups is -0.09. So, first babies are more likely to be lighter than other babies, although difference in weights is relatively small. Cohen d between these groups in terms of pregnancy length is 0.029, which is negligible. The impact of birth order on baby weight is three time tha on pregnancy length. 
