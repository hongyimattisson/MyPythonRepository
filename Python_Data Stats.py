import pandas as pd
from scipy import stats
# Test the codeing
# --- Load your CSV instead ---
df = pd.read_csv("Book1-A.csv")

df.columns = [f"col_{i}" for i in range(len(df.columns))]
df = df.rename(columns={"col_0": "A", "col_1": "B", "col_2": "RowID", "col_9": "CVR_A"})

def group_stats(x):
    std = x["CVR_A"].std(ddof=1)
    n = x["CVR_A"].count()
    mean = x["CVR_A"].mean()
    t_stat, p_val = stats.ttest_1samp(x["CVR_A"].dropna(), popmean=df["CVR_A"].mean())
    return pd.Series({
        "Count": n,
        "Mean": mean,
        "Std": std,
        "t_stat": t_stat,
        "p_value": p_val
    })

result = df.groupby(["A", "B"]).apply(group_stats).reset_index()
result.to_csv("CVR_A_group_stats.csv", index=False)
print(result.head())
#Add Testing Events
