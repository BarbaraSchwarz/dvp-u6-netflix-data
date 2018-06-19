
# coding: utf-8

# # Introduction
# 
# In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the "Netflix Stock Profile" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. 
# 
# For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:
# + The distribution of the stock prices for the past year
# + Netflix's earnings and revenue in the last four quarters
# + The actual vs. estimated earnings per share for the four quarters in 2017
# + A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 
# 
# Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).
# 
# During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.
# 
# After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:
# 
# - A title slide
# - A list of your visualizations and your role in their creation for the "Stock Profile" team
# - A visualization of the distribution of the stock prices for Netflix in 2017
# - A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary
# - A visualization and a brief summary of their earned versus actual earnings per share
# - A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017
# 
# Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)
# 

# ## Step 1
# 
# Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# In[4]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# ## Step 2

# Let's load the datasets and inspect them.

# Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.
# 
# Hint: Use the `pd.read_csv()`function).
# 
# Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day.

# In[5]:


netflix_stocks = pd.read_csv("NFLX.csv")
print(netflix_stocks)


# Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.
# 
# Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). 
# 

# In[6]:


dowjones_stocks = pd.read_csv("DJI.csv")
print(dowjones_stocks)


# Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.
# 

# In[7]:


netflix_stocks_quarterly = pd.read_csv("NFLX_daily_by_quarter.csv")
print(netflix_stocks_quarterly)


# ## Step 3

# Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.
#  - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly
#  - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.
#  - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). 
#  
# Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer.

# What year is represented in the data? Look out for the latest and earliest date.

# In[8]:


#Earliest date is in NFLX.csv == 2017-01-01 ;
# Latest date is in NFLX_daily_by_quarter.csv == 2017-12-29 ;
# The year represented is 2017.


# + Is the data represented by days, weeks, or months? 
# + In which ways are the files different? 
# + What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?

# In[9]:


# As perhaps to be expected, NFLX.csv and DJI.csv have same structure for comparing 'start-of month like-with-like';
# These two (NFLX.csv and DJI.csv) register prices on first day of each month for the whole of 2017.
# By contrast, NFLX_daily_by_quarter.csv gives daily prices of trading days in each quarter of 2017 ;
# Each row in NFLX_daily_by_quarter.csv is assigned to a particular quarter (rather than simply months per se)


# ## Step 4
# 
# Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. 

# In[10]:


print(netflix_stocks.head())


# What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! 
# 
# The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.
# 
# This means this is the column with the true closing price, so these data are very important.
# 
# Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.
# 
# Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.
# Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).
# 

# In[11]:


netflix_stocks.rename(columns={'Adj Close':'Price'}, inplace=True)
dowjones_stocks.rename(columns={'Adj Close':'Price'}, inplace=True)
netflix_stocks_quarterly.rename(columns={'Adj Close':'Price'}, inplace=True)


# Run `netflix_stocks.head()` again to check your column name has changed.

# In[12]:


print(netflix_stocks.head())


# Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`.

# In[13]:


print(dowjones_stocks.head())
print(netflix_stocks_quarterly.head())


# ## Step 5
# 
# In this step, we will be visualizing the Netflix quarterly data! 
# 
# We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!
# 
# 
# 1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.
# 2. Use `sns.violinplot()` and pass in the following arguments:
# + The `Quarter` column as the `x` values
# + The `Price` column as your `y` values
# + The `netflix_stocks_quarterly` dataframe as your `data`
# 3. Improve the readability of the chart by adding a title of the plot. Add `"Distribution of 2017 Netflix Stock Prices by Quarter"` by using `ax.set_title()`
# 4. Change your `ylabel` to "Closing Stock Price"
# 5. Change your `xlabel` to "Business Quarters in 2017"
# 6. Be sure to show your plot!
# 

# In[73]:


plt.figure(figsize=(10, 10))
ax = sns.violinplot(x="Quarter", y="Price", data=netflix_stocks_quarterly)
ax.set_title("Distribution of 2017 Netflix Stock Prices by Quarter", fontsize=18)
ax.set_ylabel("Closing Stock Price", fontsize=16)
ax.set_xlabel("Business Quarters in 2017", fontsize=16)
plt.savefig('Distribution_Netflix_Stock_Prices_2017_Quarters.png')
plt.show()


# ## Graph Literacy
# - What are your first impressions looking at the visualized data?
# 
# - In what range(s) did most of the prices fall throughout the year?
# 
# - What were the highest and lowest prices? 

# #First impressions are: the median rose steadily for each quarter : Netflix Stock accrued successive value over time. #Stock prices fluctuated considerably within the 3rd quarter 
# #(elongated 95% confidence level, elongated interquartile range), 
# #but mostly settled towards the higher end of the price range for that specific period, i.e. Q3; 
# #(median situated towards upper part of confidence level and interquartile range). 
# #The first quarter shows the least fluctuation in price (the density plot is very wide around the median); 
# #the last quarter (fourth) and the second quarter have less pronounced binomial distribution shapes than Q1. 
# #Most prices were above 140 and below 200 (median seen across all four quarters). 
# #The highest price was well above 200 (see top tip of Q4 violin plot);
# #the lowest price was almost touching 120 (see bottom tip of Q1 violin plot).

#  

# ## Step 6
# 
# Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. 
# 
# 1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.
# 2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color
# 
# 3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.
# 4. Add a legend by using `plt.legend()` and passing in a list with two strings `["Actual", "Estimate"]`
# 
# 5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`
# 6. Assing "`"Earnings Per Share in Cents"` as the title of your plot.
# 

# In[68]:


import numpy as np
plt.figure(figsize=(10, 10))
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]
plt.scatter(x_positions, earnings_actual, color="red", alpha=0.5)
plt.scatter(x_positions, earnings_estimate, color="blue", alpha=0.5)
plt.legend(["Actual", "Estimate"], loc='upper center', frameon=True, fontsize=16)
plt.xticks(x_positions, chart_labels)
plt.title("Earnings Per Share in Cents", fontsize=18)
plt.savefig('Earnings_Per_Share_in_Cents.png')
plt.show()


# ## Graph Literacy
# 
# + What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.
# 

# # The purple dots mean estimates accurately matched actual earnings for the 2nd and 4th quarter, whereas earnings were underestimated in the 1st and over-estimated for the 3rd.

#  

# ## Step 7

# Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).
# 
# As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. 
# 
# 1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars
# 2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data
# 3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars
# 4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data
# 5. Create a legend for your bar chart with the `labels` provided
# 6. Add a descriptive title for your chart with `plt.title()`
# 7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`
# 8. Be sure to show your plot!
# 

# In[112]:


plt.figure(figsize=(10, 8))

# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["1Q2018", "2Q2017","3Q2017","4Q2017"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(d)]
plt.bar(bars1_x, revenue_by_quarter)


# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(d)]
plt.bar(bars2_x, earnings_by_quarter)


middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]

ax.set_xticks(middle_x)
ax.set_xticklabels(quarter_labels)
plt.xticks(middle_x, quarter_labels, fontsize=12)

plt.legend(labels, frameon=True, loc='upper center', fontsize=14)
plt.title("Netflix Revenue and Earnings Overview", fontsize=18)

plt.savefig('Netflix_Revenue_and_Earnings_Overview.png')
plt.show()


# ## Graph Literacy
# What are your first impressions looking at the visualized data?
# 
# - Does Revenue follow a trend?
# - Do Earnings follow a trend?
# - Roughly, what percentage of the revenue constitutes earnings?

# In[17]:


#Revenue follows a gently upward sloping trend, as do earnings - though earnings' growth/ slope is shallower.
# Earnings constitute about 6-ish percent of revenue.


# ## Step 8
# 
# In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. 
# 
# Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.
# - We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot
#     - `1`-- the number of rows for the subplots
#     - `2` -- the number of columns for the subplots
#     - `1` -- the subplot you are modifying
# 
# - Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)
# - Assign "Netflix" as a title to this subplot. Hint: `ax1.set_title()`
# - For each subplot, `set_xlabel` to `"Date"` and `set_ylabel` to `"Stock Price"`
# - Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)
# - Assign "Dow Jones" as a title to this subplot. Hint: `plt.set_title()`
# - There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`
# - Be sure to `.show()` your plots.
# 

# In[103]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fig = plt.figure(figsize=(15, 5))
sns.set_style("darkgrid")

# Left plot Netflix
# ax1 = plt.subplot(total number rows, total number columns, index of subplot to modify)

ax1 = plt.subplot(1,2,1)
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])
plt.title("Netflix 2017 at month's start", fontsize=18)
ax1.set_xlabel("Date", fontsize=12)
plt.xticks(rotation='vertical',fontsize=12)
ax1.set_ylabel("Stock Price", fontsize=12)

# Right plot Dow Jones
# ax2 = plt.subplot(total number rows, total number columns, index of subplot to modify)
ax2 = plt.subplot(1,2,2)
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])
plt.title("Dow Jones 2017 at month's start", fontsize=18)
ax2.set_xlabel("Date", fontsize=12)
plt.xticks(rotation='vertical', fontsize=12)
ax2.set_ylabel("Stock Price", fontsize=12)

plt.subplots_adjust(wspace=.5, bottom=.3)
plt.savefig('Netflix_and_Dow_Jones_2017_Performance.png')
plt.show()






# - How did Netflix perform relative to Dow Jones Industrial Average in 2017?
# - Which was more volatile?
# - How do the prices of the stocks compare?

#  

# # Step 9
# 
# It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig("filename.png")`.
# 
# As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!
# 
# Remember that your slideshow must include:
# - A title slide
# - A list of your visualizations and your role in their creation for the "Stock Profile" team
# - A visualization of the distribution of the stock prices for Netflix in 2017
# - A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary
# - A visualization and a brief summary of their earned versus actual earnings per share
# - A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017
# 

# In[ ]:


#In respect of last graph (Netflix 2017 performance vis-a-vis Dow Jones Average):
#Netflix showed greater volatility than Dow Jones Average and crashed down in June;
#but also bounced back in July, dipped in August, reached a peak in October and sloped off.

