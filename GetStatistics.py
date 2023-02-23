'''
Write a function that takes in a list of numbers and returns a dictionary containing the following statistics about the numbers: the mean, median, mode, sample variance, sample standard deviation, and 95% confidence interval for the mean.

Note that:

You can assume that the given list contains a large-enough number of samples from a population to use a z-score of 1.96.
If there's more than one mode, your function can return any of them.
You shouldn't use any libraries.
Your output values will automatically be rounded to the fourth decimal.
Sample Input
input_list = [2, 1, 3, 4, 4, 5, 6, 7]
Sample Output
{
  "mean": 4.0,
  "median": 4.0,
  "mode": 4.0,
  "sample_variance": 4.0,
  "sample_standard_deviation": 2.0,
  "mean_confidence_interval": [2.6141, 5.3859],
}
'''

def get_statistics(input_list):
    l = sorted(input_list)
    n = len(input_list)

    mean = sum(l)/n
    
    mid = (n-1)//2
    median = l[mid]
    if(n%2==0):  
        median = (median + l[mid+1])/2  #Average of the two middle elements

    freq = { x : l.count(x) for x in set(l)}
    mode = max(freq.keys(), key = lambda x : freq[x])

    var = sum([(num-mean)**2 / (n-1) for num in l])

    sd = var**0.5


    mse = sd/n**0.5
    z_score = 1.96*mse
    
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": var,
        "sample_standard_deviation": sd,
        "mean_confidence_interval": [mean-z_score, mean+z_score],
    }
