import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from itertools import combinations

def duncan_test(data, response, factor):
    # Perform ANOVA
    #eq = response + " ~ C(" + factor + ")"
    model = ols(f'{response} ~ C({factor})', data=data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    
    # Extract means and sample sizes
    means = data.groupby(factor)[response].mean()
    n = data.groupby(factor)[response].count()
    
    # Calculate Mean Square Error (MSE)
    mse = anova_table['sum_sq']['Residual'] / anova_table['df']['Residual']
    
    # Number of groups
    k = len(means)
    
    # Initialize a result DataFrame
    results = pd.DataFrame(index=means.index, columns=means.index, data=False)
    
    # Use alpha = 0.01 or 0.001 to check level of significance
    alpha = 0.05

    # Duncan critical values (studentized range distribution)
    q = stats.t.ppf(1 - alpha / 2, anova_table['df']['Residual'])
    
    # Perform pairwise comparisons
    for (i, j) in combinations(means.index, 2):
        mean_diff = np.abs(means[i] - means[j])
        se_diff = np.sqrt(mse * (1/n[i] + 1/n[j]))
        
        # Calculate the range statistic
        r = mean_diff / se_diff
        
        # Compare to critical value
        results.loc[i, j] = r > q

    return results, anova_table