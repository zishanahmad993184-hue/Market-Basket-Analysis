# Market Basket Analysis Project

## Overview

This project performs Market Basket Analysis using Python and the Apriori Algorithm. It identifies products that are frequently purchased together and generates association rules based on transaction data.

## Objective

The main objective of this project is to discover relationships between items in customer transactions and help businesses improve product placement, cross-selling, and marketing strategies.

## Technologies Used

* Python
* Pandas
* MLxtend
* Matplotlib
* VS Code

## Dataset

The dataset contains transaction records with purchased items.

Example:

TransactionID, Items

1, Milk,Bread,Butter

2, Bread,Eggs

3, Milk,Bread

## Features

* Data preprocessing
* One-hot encoding
* Apriori Algorithm
* Frequent Itemset Generation
* Association Rule Mining
* Data Visualization

## Project Structure

Market_Basket_Analysis

├── market_basket.py

├── transactions.csv

└── README.md

## How to Run

1. Install required libraries:

pip install pandas mlxtend matplotlib seaborn

2. Run the project:

python market_basket.py

## Output

The project generates:

* Frequent Itemsets
* Association Rules
* Support, Confidence, and Lift values
* Visualization of top frequent itemsets

## Conclusion

Market Basket Analysis helps businesses understand customer purchasing behavior and identify product combinations that are commonly bought together.
