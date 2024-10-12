# Import necessary libraries
import pandas as pd
from scipy.stats import chi2_contingency

# Create a contingency table (2x2) for recovered and not recovered in both groups
data = {
    'Recovered': [13, 5],
    'Not Recovered': [7, 15]
}
df = pd.DataFrame(data, index=['Test Group', 'Control Group'])

print("Contingency Table:")
print(df)

# Perform the chi-square test of independence
chi2, p, dof, expected = chi2_contingency(df)

print("\nChi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2}")
print(f"P-Value: {p}")
print(f"Degrees of Freedom: {dof}")

# Interpret the results
alpha = 0.05
if p < alpha:
    print(f"\nSince p ({p}) is less than alpha ({alpha}), we reject the null hypothesis that the recovery rate is independent of the treatment group.")
    print("This suggests that the drug A is effective.")
else:
    print(f"\nSince p ({p}) is greater than or equal to alpha ({alpha}), we fail to reject the null hypothesis that the recovery rate is independent of the treatment group.")
    print("This suggests that the drug A is not effective.")