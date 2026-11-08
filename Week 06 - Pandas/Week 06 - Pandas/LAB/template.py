"""
RECORD CHECK  -  my version
===========================

Name  : Amy
Lane  : IT      (delete two)
Date  : 28/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

df = pd.read_csv("read.csv")  

df["percent"] = (df["used_gb"] / df["total_gb"]) * 100
df["status"] = df["percent"].apply(lambda x: "OVER LIMIT" if x >= 100 else "WARNING" if x >= 90 else "OK")


print(df[df["status"] != "OK"])
grouped = df.groupby("status")
print(grouped.count())
df.to_csv("output.csv", index=False)

import matplotlib.pyplot as plt
df["status"].value_counts().plot(kind="bar")
plt.show()

