import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_csv("transactions.csv")
transactions = df["Items"].apply(lambda x: x.split(","))
te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
basket = pd.DataFrame(te_array, columns=te.columns_)
frequent_itemsets = apriori(
    basket,
    min_support=0.3,
    use_colnames=True
)
print("Frequent Itemsets:")
print(frequent_itemsets)

rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.6
)

print("\nAssociation Rules:")
print(
    rules[
        [
            "antecedents",
            "consequents",
            "support",
            "confidence",
            "lift"
        ]
    ]
)
# Association Rules print hone ke baad

import matplotlib.pyplot as plt

frequent_itemsets.sort_values(
    by="support",
    ascending=False
).head(10).plot(
    x="itemsets",
    y="support",
    kind="bar"
)

plt.title("Top Frequent Itemsets")
plt.xlabel("Itemsets")
plt.ylabel("Support")
plt.show()