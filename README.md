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

   #### 2.	The even distributed type of movie will lead to the maximum of the profit.
   We assume that the movie type can affect the profit of movies and then we illustrate that the different movie type will infect the profit of a movie. And generated the data frame and get the plot as follows: 

   We can see that the curve fluctuations in the graph of Hypothesis 2 are much smaller than that of Hypothesis 1, so we can draw the conclusion that Hypothesis 2 (the type of movie) will have more impact on the final profit of the movie than Hypothesis 1 (the celebrity of the movie) influence.

   #### 3.	The length of the film is between 110 minutes and 120 minutes will maximize the profit.
   We assume that the length of movies in minutes can affect the profit of movies. and then we illustrate that the different length of movie will infect the profit of a movie. And generated the data frame and get the plot as follows: 


   #### 4.	The film production (editing time of the movie) costs no longer than 90 days will maximize the profit.
   We assume that the spend time of the movie in days can affect the profit of movies. And plot as follows:

   #### 5.  Original voice dubbing of movie actors will also lead to the maximum of the movie.
   We assume that whether the movie is dubbing can affect the profit of movies. And plot as follows:

### Phase 3 Analysis:
Because the Monte Carlo method can truly simulate the actual physical process, the problem solving is very consistent with the reality, and very satisfactory results can be obtained. According to the results of the discrete graph obtained from the five hypotheses, we can support Hypothesis 5 and Hypothesis 2, that is, the type of movie and whether the movie is dubbing will affect the profit of the movie. And refuse to accept assumptions 1, 3, 4 that the length of the movie, the time spent on the movie, and the Celebrity of the movie will not affect the profit of the movie.