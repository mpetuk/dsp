import scipy.stats

mu=178
sigma=7.7

dist=scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

dist.cdf(mu-sigma)

print ('Proportion of the U.S. male population that qualifies for Blue Men Group height-wise  is', abs( dist.cdf(177.8) - dist.cdf(185.4))) 


