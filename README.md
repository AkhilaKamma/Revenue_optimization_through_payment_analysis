# Revenue_optimization_through_payment_analysis

## Problem Statement
In the fast-paced taxi booking sector, making most of the revenue is essential for long term success and driver hapiness. Our goal is to use data driven insights to maximise revenue streams for taxi drivers inorder to meet this need. Our research aims to determine whether payment menthods have an impact on fare pricing by focusing on the relationship between payement type and fare amount.

## Objective
The project main goal is to run a A/B test to examine the relationship between the total fare and method of paymnet. We use python hypothesis testing and descriptive statistics to extract useful information that can help taxi drivers generate more cash. In particular, we want to find out if there is a big difference in the fares for those who pay credit cards verses those who pay with cash.

## Research Question

Is there a relationship between total fare amount and paymnet type and can we nudge customers toward paymnet methods that generate higher revenue for drivers, without negatively impacting customer experience?

## Hypothesis Testing

**Null hypothesis:** there is no difference in average fare between customers who use credit cards and customers who use cash.

**Alternate hypothesis:** There is a difference in average fare between customers who use credit cards and customers who use cash

![image](https://github.com/AkhilaKamma/Revenue_optimization_through_payment_analysis/assets/22701124/3f6ce464-58f5-427f-958e-96a15940f040)

From QQ plot it is very evident that the data is not normally distributed. So performed T-test and the values are as below:

```bash
T statistic 165.6989722565007 p-value 0.0
p < 0.05(significance value) so reject Null hypothesis
```



