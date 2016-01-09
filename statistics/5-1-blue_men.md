[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 
```
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)
```
>>
```
dist.mean(), dist.std()
```
>>
```
low = dist.cdf(177.8)    # 5'10"
high = dist.cdf(185.4)   # 6'1"
low, high, high-low
```
>>
```0.48963902786483265, 0.83173371081078573, 0.34209468294595308```

>> 34% of thhe US population is between 5'10" and 6'1'
