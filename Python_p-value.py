import pandas as pd
from scipy import stats
import math

# Load your Excel file (adjust sheet name if needed)
df = pd.read_csv("Book4.csv", sheet_name="Summary")

# Calculate Welch’s t-statistic and p-value for each row
def calc_p_value(row):
    mean_a, mean_b = row['Mean A'], row['Mean B']
    std_a, std_b = row['Stdev A'], row['Stdev B']
    n_a, n_b = row['Count A'], row['Count B']
    
    # Handle edge cases
    if n_a <= 1 or n_b <= 1 or std_a == 0 or std_b == 0:
        return None
    
    # Welch’s t-statistic
    t_stat = (mean_a - mean_b) / math.sqrt((std_a**2 / n_a) + (std_b**2 / n_b))
    
    # Degrees of freedom (Welch–Satterthwaite equation)
    df_num = ((std_a**2 / n_a) + (std_b**2 / n_b))**2
    df_denom = ((std_a**2 / n_a)**2 / (n_a - 1)) + ((std_b**2 / n_b)**2 / (n_b - 1))
    degrees_freedom = df_num / df_denom
    
    # Two-tailed p-value
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=degrees_freedom))
    
    return p_value

df['p_value'] = df.apply(calc_p_value, axis=1)

# Save to a new Excel file
df.to_excel("Book4_with_pvalues.xlsx", index=False)
print("✅ Done! p-values saved to 'Book4_with_pvalues.xlsx'")
