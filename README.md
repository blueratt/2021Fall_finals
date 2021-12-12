# 2021Fall_finals


## Monte Carlo simulation to maximize the total profit of the entire movie market

### Author: Shihao Jin, Francis Feng, Yanmeng Xin
 ![alt text](https://github.com/blueratt/2021Fall_finals/blob/main/movie_poster.jpeg)

### Design our own scenario:
Since the current year's revenue of a certain type of film company = the previous year's revenue * (1 + revenue growth rate), the revenue growth rate we designed is simulated by Monte Carlo: Run 1000 times to get the expected revenue the max, min and average. Through observation of historical data and the intuition of decision makers, revenue growth rates and revenue fluctuations can be seen.

### Phase 1 Dataset:
We use the random seeds in NumPy to simulate and determine the base revenue and cost for each genre of movies which have different base revenue and cost.
We define that any type of movie exceeds 30% of total portfolio will lead to a decrease in the base revenue because of over-competition, and lower than 5% will increase the base revenue because of lack of competition. Use 3 columns "movie_type", "revenue", "cost" to generate the data frame.

### Phase 2 Controls and Experiments:
We have designed 5 hypotheses to illustrate this project:
   #### 1.	There is a certain number of celebrities in the movie will maximize the profit. 
   We calculated how the number of celebrities will affect the movie's revenue and cost firstly and then we illustrate that the celebrity value will infect the profit of a movie. And generated the data frame and get the plot as follows:
   
 ![alt text](https://github.com/blueratt/2021Fall_finals/blob/main/Hypo%20Graph/Hypothesis1.png)
 
   We can see that there is an peak in the graph, so we can conclude that celebrity in about 5 will make the most profit to the movie.

   #### 2.	The even distributed type of movie will lead to the maximum of the profit.
   We assume that the movie type can affect the profit of movies and then we illustrate that the different movie type will infect the profit of a movie. And generated the data frame and get the plot as follows: 
   
 ![alt text](https://github.com/blueratt/2021Fall_finals/blob/main/Hypo%20Graph/Hypothesis2_1.png)
 ![alt text](https://github.com/blueratt/2021Fall_finals/blob/main/Hypo%20Graph/Hypothesis2_2.png)

   We can see that the total profit from not even distributing the movie market will lead to an great increase of the profit

   #### 3.	The length of the film is between 110 minutes and 120 minutes will maximize the profit.
   We assume that the length of movies in minutes can affect the profit of movies. 
   
 ![alt text](https://github.com/blueratt/2021Fall_finals/blob/main/Hypo%20Graph/Hypothesis3.png)

   we can see that the graph is not showing the case we hyposis
   
   #### 4.	The film production (editing time of the movie) costs no longer than 90 days will maximize the profit.
   We assume that the spend time of the movie in days can affect the profit of movies. And plot as follows:

 ![alt text](https://github.com/blueratt/2021Fall_finals/blob/main/Hypo%20Graph/Hypothesis4.png)

   We can see that the picture of Hypothesis 4 has a sudden decline to the filming days at 120, so between 90 and 120 can have the greatest profit
   

   #### 5.  Original voice dubbing of movie actors will also lead to the maximum of the movie.
   We assume that whether the movie is dubbing can affect the profit of movies. And plot as follows:
 ![alt text](https://github.com/blueratt/2021Fall_finals/blob/main/Hypo%20Graph/Hypothesis5.png)
 ![alt text](https://github.com/blueratt/2021Fall_finals/blob/main/Hypo%20Graph/Hypothesis5_1.png)

   By comparing the two graphs, we can see that using dubbing can greatly increase the profit


### Phase 3 Analysis:
 The problem solving is very consistent with the reality, and very satisfactory results can be obtained because the Monte Carlo method can truly simulate the actual physical process. According to the results of the discrete graph obtained from the five hypotheses, we can support Hypothesis 5 and Hypothesis 2, that is, the type of movie and whether the movie is dubbing will affect the profit of the movie. And refuse to accept assumptions 1, 3, 4 that the length of the movie, the time spent on the movie, and the Celebrity of the movie will not affect the profit of the movie.
 
 

Reference:
1. https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
2. https://pandas.pydata.org/docs/reference/index.html
3. https://matplotlib.org/stable/index.html
4. https://kodify.net/python/math/round-integers/
5. https://www.investopedia.com/financial-edge/0611/why-movies-cost-so-much-to-make.aspx
6. https://www.the-numbers.com/movie/budgets
7. https://dev.to/zohebabai/step-by-step-instructions-for-testing-your-github-python-project-using-github-actions-227b
8. https://dev.to/zohebabai/step-by-step-instructions-for-testing-your-github-python-project-using-github-actions-227b
9. https://stackoverflow.com/questions/31571830/pandas-histogram-from-two-columns
10. https://stackoverflow.com/questions/67523882/workflow-is-not-shown-so-i-cannot-run-it-manually-github-actions
11. https://www.geeksforgeeks.org/python-pandas-dataframe-mean/
12. https://www.geeksforgeeks.org/python-pandas-dataframe-mean/
13. https://github.com/ZohebAbai/python_test_repo/blob/master/.github/workflows/ci.yml
