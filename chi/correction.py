import pandas as pd
from scipy.stats import chi2_contingency

# Define the data
data = pd.DataFrame({
    'Recovered': [13, 5],
    'Not Recovered': [7, 15]
}, index=['Test Group', 'Control Group'])

# Print the data
print("Contingency Table:")
print(data)

# Perform the chi-square test of independence without Yates' correction for continuity
chi2_stat, p_value, dof, expected = chi2_contingency(data, correction=False)

# Print the results
print(f"\nChi-Square Test Results (without Yates' correction): {chi2_stat}")
print(f"P-Value: {p_value}")
print(f"Degrees of Freedom: {dof}")

# Perform the chi-square test of independence with Yates' correction for continuity
chi2_stat, p_value, dof, expected = chi2_contingency(data, correction=True)

# Print the results
print(f"\nChi-Square Test Results (with Yates' correction): {chi2_stat}")
print(f"P-Value: {p_value}")
print(f"Degrees of Freedom: {dof}")


# Interpret the results
alpha = 0.05
if p_value < alpha:
    print(f"\nSince p_value ({p_value}) < alpha ({alpha}), we reject the null hypothesis.")
    print("This suggests that there is a statistically significant association between the treatment and recovery.")
else:
    print(f"\nSince p_value ({p_value}) >= alpha ({alpha}), we fail to reject the null hypothesis.")
    print("This suggests that there is no statistically significant association between the treatment and recovery.")