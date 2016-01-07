[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> Had to google how to generate random numbers in the range asked for. Used the ThinkStats.Pmf and .Cdf functions to calculate each. 
>> Used the Thinkplot function to generate the charts. The following is the code chunk used to solved this problem

```
import random
x = [random.random() for _ in range(1000)]
pmf= thinkstats2.Pmf(x)
cdf= thinkstats2.Cdf(x)

thinkplot.Pmf(pmf, linewidth=0.1, label='pmf')
thinkplot.Cdf(cdf, label='cdf'
```

>> Since the plot for cdf is more of a straight line, I would say the distribution is in fact uniform. 
