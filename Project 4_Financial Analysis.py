#!/usr/bin/env python
# coding: utf-8

# # Financial Analysis of 20Companies

# The data set appears to contain information on the companies by market capitalization, including columns for serial number, company name, market capitalization (in crores), and quarterly sales (in crores). Here's an introduction based on this data:

# In[55]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load the dataset
file_path="C:/Users/Chaitra/Downloads/Financial Analytics data.csv"
data=pd.read_csv(file_path)


# In[19]:


data.head()


# In[25]:


#Drop the irrelevant column
data_cleaned = data.drop(columns=['Unnamed: 4'])


# In[28]:


# Handle missing values by dropping rows with missing market capitalization or sal
data_cleaned = data_cleaned.dropna(subset=['Mar Cap - Crore','Sales Qtr - Crore'])


# In[30]:


#display the clean dataset information
print(data_cleaned.info())


# In[35]:


#Exploratory Data Analysis(EDA)
plt.figure(figsize=(10,6))
sns.histplot(data_cleaned['Mar Cap - Crore'],bins=30,color='yellow',kde=True)
plt.title("Distribution Market Capitalization")
plt.xlabel('Market Capitalization(Cr)')
plt.ylabel('Frequency')
plt.show()


# observations:
# More than 250 companies are 20000Cr Market Capitalization.

# In[41]:


plt.figure(figsize=(10, 6))
sns.histplot(data_cleaned['Sales Qtr - Crore'], bins=30, kde=True,color="blue")
plt.title('Distribution of Quarterly Sales')
plt.xlabel('Quarterly Sales (Crores)')
plt.ylabel('Frequency')
plt.show()


# Observations:
#           More than 250 companies are 4000Cr Quarterly Sales.

# In[42]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Sales Qtr - Crore', y='Mar Cap - Crore', data=data_cleaned,color="Green")
plt.title('Market Capitalization vs Quarterly Sales')
plt.xlabel('Quarterly Sales (Crores)')
plt.ylabel('Market Capitalization (Crores)')
plt.show()


# Observations:Most of the companies lies between 0-100000cr Market Capitalization and 0-20000Cr Quarterly Sales.

# In[44]:


# Calculate and display correlation
correlation = data_cleaned[['Mar Cap - Crore', 'Sales Qtr - Crore']].corr()
print(correlation)


# In[46]:


# Key Metrics Calculation of Market capitalization(Crores)
mean_mar_cap = data_cleaned['Mar Cap - Crore'].mean()
median_mar_cap = data_cleaned['Mar Cap - Crore'].median()
std_mar_cap = data_cleaned['Mar Cap - Crore'].std()


# In[47]:


# Key Metrics Calculation of Sales Quarter(Crores)
mean_sales_qtr = data_cleaned['Sales Qtr - Crore'].mean()
median_sales_qtr = data_cleaned['Sales Qtr - Crore'].median()
std_sales_qtr = data_cleaned['Sales Qtr - Crore'].std()


# In[48]:


print(f'Mean Market Capitalization: {mean_mar_cap}')
print(f'Median Market Capitalization: {median_mar_cap}')
print(f'Standard Deviation of Market Capitalization: {std_mar_cap}')
print(f'Mean Quarterly Sales: {mean_sales_qtr}')
print(f'Median Quarterly Sales: {median_sales_qtr}')
print(f'Standard Deviation of Quarterly Sales: {std_sales_qtr}')


# In[53]:


# Insights and Recommendations
top_companies = data_cleaned.sort_values(by='Mar Cap - Crore', ascending=False).head(20)
print("Top 10 Companies by Market Capitalization:")
print(top_companies[['Name', 'Mar Cap - Crore', 'Sales Qtr - Crore']])


# In[54]:


# Visualization of Top 20 Companies by Market Capitalization
plt.figure(figsize=(14, 7))
sns.barplot(x='Mar Cap - Crore', y='Name', data=top_companies, palette='viridis')
plt.title('Top 20 Companies by Market Capitalization')
plt.xlabel('Market Capitalization (Crores)')
plt.ylabel('Company Name')
plt.show()


# The analysis of the top 20 companies by market capitalization reveals significant insights into their financial health and market position. 
# 
# Key findings include:
# 
# 1.Market Dominance: Companies like Reliance Industries and TCS lead with substantial market capitalizations, indicating their dominant positions in the market.
# 2.Revenue Generation: High quarterly sales figures for these companies demonstrate their robust revenue generation capabilities and strong market demand.
# 3.Industry Leaders: The diversity among the top companies, ranging from technology and banking to consumer goods, underscores the varied sectors contributing to the economy.
# 4.Strategic Positioning: The financial metrics provide a clear picture of each company's strategic positioning, highlighting areas of strength and potential for growth.
# 
# Overall, this financial analysis underscores the pivotal role these corporations play in the market, offering valuable insights for stakeholders aiming to navigate the complexities of the economic landscape.

# In[ ]:




