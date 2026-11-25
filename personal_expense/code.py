import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Types
name = "Vaishnavi"
age = 21
budget = 10000.0
active = True
categories = ["Food", "Shopping", "Travel"]
details = {"Name": name, "Age": age}

print(type(name), type(age), type(budget))
print(type(active), type(categories), type(details))

# 2. Create Dataset
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri",
            "Sat", "Sun", "Mon", "Tue", "Wed"],
    "Category": ["Food", "Travel", "Shopping", "Food",
                 "Bills", "Travel", "Food", "Shopping",
                 "Bills", "Food"],
    "Amount": [200, 500, 1200, 300, 800,
               600, 250, 1500, 700, 400]
}

df = pd.DataFrame(data)

# 3. Function
def expense_analysis(df):
    print("Total Expense:", np.sum(df["Amount"]))
    print("Average Expense:", np.mean(df["Amount"]))
    print("Highest Expense:", np.max(df["Amount"]))

    df["Status"] = np.where(
        df["Amount"] > 500, "High", "Normal"
    )
    return df

df = expense_analysis(df)

# 4. Pandas Analysis
category = df.groupby("Category")["Amount"].sum()
print("\nCategory Expenses:")
print(category)

# 5. Bar Chart
category.plot(kind="bar")
plt.title("Category Wise Expenses")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()

# 6. Pie Chart
plt.pie(category, labels=category.index,
        autopct="%1.1f%%")
plt.title("Expense Percentage")
plt.show()

# 7. Line Chart
plt.plot(df["Day"], df["Amount"], marker="o")
plt.title("Daily Expense Trend")
plt.xlabel("Day")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 8. Scatter Plot
sns.scatterplot(data=df, x="Amount", y="Day",
                hue="Category")
plt.title("Expense Comparison")
plt.tight_layout()
plt.show()

# 9. Box Plot
sns.boxplot(data=df, x="Category", y="Amount")
plt.title("Category Expense Distribution")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# 10. Heatmap
pivot = df.pivot_table(
    index="Day",
    columns="Category",
    values="Amount",
    aggfunc="sum",
    fill_value=0
)

sns.heatmap(pivot, annot=True, cmap="YlGnBu")
plt.title("Daily Category Expense Heatmap")
plt.tight_layout()
plt.show()

# 11. Save Excel
df.to_excel("Expense_Analysis.xlsx", index=False)

print("\nProject Completed!")