# 2021Fall_finals


## Monte Carlo simulation to maximize the total profit of the entire movie market

### Author: Shihao Jin, Francis Feng, Yanmeng Xin


### Design our own scenario:
Since the current year's revenue of a certain type of film company = the previous year's revenue * (1 + revenue growth rate), the revenue growth rate we designed is simulated by Monte Carlo: Run 1000 times to get the expected revenue the max, min and avg. Through observation of historical data and the intuition of decision makers, revenue growth rates and revenue fluctuations can be seen.

### Phase 1 Dataset:
We use the random seeds in NumPy to simulate and determine the base revenue and cost for each genre of movies which have different base revenue and cost.
We define that any type of movie exceeds 30% of total portfolio will lead to a decrease in the base revenue because of over-competition, and lower than 5% will increase the base revenue because of lack of competition. Use 3 columns "movie_type", "revenue", "cost" to generate the data frame.

### Phase 2 Controls and Experiments:
We have designed 5 hypotheses to illustrate this project:
   #### 1.	There is a certain number of celebrities in the movie will maximize the profit. 
   We calculated how the number of celebrities will affect the movie's revenue and cost firstly and then we illustrate that the celebrity value will infect the profit of a movie. And generated the data frame and get the plot as follows: 

   We can see that the lines in the graph are very volatile, so we cannot conclude that celebrity will affect the profit of the movie.


###