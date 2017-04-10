[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> Python code:
import scipy.stats


dist=scipy.stats.norm(loc=mu, scale=sigma)
type(dist)


print ('Proportion of the U.S. male population that qualifies for Blue Men Group height-wise  is', abs( dist.cdf(177.8) - dist.cdf(185.4)))

Result: Roughly third (34.2%) of the U.S. male population falls in the range of 5'10" and 6'1" 
