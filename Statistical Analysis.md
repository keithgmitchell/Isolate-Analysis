### TYPES OF DATA:
The type of variable you have dictates the types of statistical tests you would run. There are two types of variables:

***Numeric***: The variable can be expressed as a number (ie, Temperature, Elevation, pH)

***Categorical***: The variable cannot be expressed as a number, but is instead a qualitative category (ie, Gender, season)

Statistical tests are run to compare two or more variables. In an experiment, researchers manipulate the ***independent variable*** to see if there is a change in the ***dependent variable***, which is the variable measured in the experiment. 

### STATISTICAL TEST 1: CHI SQUARED TEST

If both the independent and the dependent variable are categorical, a **chi-squared** test can be used. When both variables are categorical, the *frequencies* of the variables can be compared by constructing a *contingency* table. The chi-squared test is then run on the contingency table. 

For example, consider the following sample purity contingency table constructed by counting the number of isolates in Field 10 and 11 that were Pure or Not Pure:
The null hypothesis of the chi-squared test is that the two variables *purity* and *field number* are *independent* from each other. In other words, if you know the identity of one variable, say, *purity*, you gain no additional information about the other variable. The alternative hypothesis is that the two variables are related to each other, so that information about one variable can help you predict the value of the other variable.

The assumptions of the chi-squared test are as follows:
- Simple random sampling
- Sufficiently large sample size (so that the central limit theorem holds and the sampling distribution is normal)
- Observations are independent of one another

The **odds ratio** is a measure of the **effect size** of this comparison. It is good practice to report both the p-value and the corresponding effect size of statistical comparisons. 

**Fisher's Exact Test** works similarly to the chi-squared test but is accurate even with small sample sizes, so it is recommended when comparing two categorical variables when working with a small sample size. We'll be using Fisher's Exact Test.

### **STATISTICAL TEST 2: T-TEST**

The t-test can used when the independent variable is categorical but the dependent variable is numeric. A t-test is used when there are one or two possible values for the independent variable, and a generalization of the t-test, called **ANOVA** is used when there are three or more possible values for the independent variable. 

A t-test can be used to determine whether the means of two samples are statistically significantly different from each other. There are three types of t-tests:

**One-sample t-test**: Test the null hypothesis that the sample mean is equal to some mean determined by the researcher. For example, a researcher could measure the heights of 100 UCLA undergraduates and use the one-sample t-test to test whether or not the mean is statistically significantly different than 68 inches.

**Two-sample (independent) t-test**: Test the null hypothesis that the means of two samples are equal to each other. For example, a researcher could measure the heights of 100 UCLA undergraduates and 100 USC undergraduates, compute the means of the two samples, and then use the two-sample t-test to determine if the heights of UCLA and USC undergraduates are different from each other.

**Paired t-test**: Also known as the two-sample dependent t-test. The paired t-test is the same as the two-sample t-test, but is used when the entries in the two samples are *dependent*, or matched with one another. For example, a researcher could measure the height of 100 UCLA undergraduates in January, and then the height of the *same* 100 UCLA undergraduates in March, and test whether those heights are different from each other in those two months using a paired t-test.

There are multiple measures for the **effect size** of a two-sample comparison, but some of them include reporting the difference between the two means, recording the ratio of the two means, and **Cohen's D**, the difference in means divided by the (pooled) standard deviation of the samples, which can be calculated by the computer. 
