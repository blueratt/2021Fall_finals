# final_project
# 597 PR final project
# Created by Shihao Jin, Frencis Feng, Yanmeng Xin

import random as random
import pandas as pd
import scipy.stats
import numpy as np
from matplotlib import pyplot as plt


def get_base_cost_for_movie(index, cost_revenue):
    """
        determine the base revenue and cost for each genre of movies which have different base revenue and cost
        :param movie_type:
        :return:
        """
    type_list = ['action', 'comedy', 'drama', 'fantasy', 'horror', 'mystery', 'romance', 'crime', 'animation',
                 'thriller']
    res = []
    for i in range(1000):
        movie_type = type_list[index[i]]
        if movie_type == 'action':
            cost = cost_revenue[0][0]
            revenue = cost_revenue[0][1]
        elif movie_type == 'comedy':
            cost = cost_revenue[1][0]
            revenue = cost_revenue[1][1]
        elif movie_type == 'drama':
            cost = cost_revenue[2][0]
            revenue = cost_revenue[2][1]
        elif movie_type == 'fantasy':
            cost = cost_revenue[3][0]
            revenue = cost_revenue[3][1]
        elif movie_type == 'horror':
            cost = cost_revenue[4][0]
            revenue = cost_revenue[4][1]
        elif movie_type == 'mystery':
            cost = cost_revenue[5][0]
            revenue = cost_revenue[5][1]
        elif movie_type == 'romance':
            cost = cost_revenue[6][0]
            revenue = cost_revenue[6][1]
        elif movie_type == 'crime':
            cost = cost_revenue[7][0]
            revenue = cost_revenue[7][1]
        elif movie_type == 'animation':
            cost = cost_revenue[8][0]
            revenue = cost_revenue[8][1]
        # movie_type == 'thriller':
        else:
            cost = cost_revenue[9][0]
            revenue = cost_revenue[9][1]
        res.append([movie_type, revenue, cost])
    return res


def define_cost_revenue(indexlist):
    """
       Any type of movie exceeds 30% of total portfolio will lead to a decrease in the base
revenue because of over-competition, and lower than 5% will increase the base revenue
because of lack of competition
        :param movie_type:
        :return:
        """
    cost_revenue = [[100, 90], [90, 70], [100, 80],
                    [120, 110], [130, 100], [100, 100],
                    [90, 90], [120, 100], [100, 90], [100, 100]]
    for i in range(10):
        if indexlist.count(i) >= 300:
            cost_revenue[i][0] -= 20
        elif indexlist.count(i) < 50:
            cost_revenue[i][0] += 20
    return cost_revenue


def calculate_during_effect(data):
    """
    calculate how the movie duration will change the revenue and cost
    :param movie_price:
    :param length:
    :return:
    """
    # for sake of the minimum length of 60 minutes for each movie
    length = [60 for i in range(1000)]
    revenue = np.copy(data["revenue"])
    cost = np.copy(data["cost"])
    for i in range(1000):
        length_increase = np.random.randint(0, 241)
        if length_increase < 30:
            cost_increase = np.log(length_increase + 1) * 0.2
            revenue_increase = np.log(length_increase + 1) * 0.4
        elif length_increase < 90 and length_increase >= 30:
            cost_increase = np.log(length_increase + 1) * 0.25
            revenue_increase = np.log(length_increase + 1) * 0.25
        else:
            cost_increase = np.log(length_increase + 1) * 0.1
            revenue_increase = np.log(length_increase + 1) * 0.1
        length[i] += length_increase
        revenue[i] *= (revenue_increase + 1)
        cost[i] *= (cost_increase + 1)
    data["revenue"] = revenue
    data["cost"] = cost
    data["length/mins"] = pd.DataFrame(length)

    # random increase cost and revenue


def calculate_the_celebrity_effect(data):
    """
    calculate how the number of celebrity will affect the movie's revenue and cost
    :param movie_price:
    :param number_of_celebrity:
    :return:
    """
    revenue = np.copy(data["revenue"])
    cost = np.copy(data["cost"])
    celebrity_num = [0 for _ in range(1000)]
    for i in range(1000):
        celebrity_num[i] = np.random.randint(0, 21)  # min_celebrity_num = 0  max_celebrity_num = 20
        revenue_increase = np.log(celebrity_num[i] + 1) * np.random.rand() * 0.1
        revenue[i] *= (revenue_increase + 1)
    data["revenue"] = revenue
    data["celebrity"] = celebrity_num


def is_over_budget(data):
    """
    determine whether movie will be over budget and how it will change the cost and revenue
    :param movie_price:
    :return:
    """
    num_over_budget = data[data["cost"] > data["revenue"]].shape[0]
    if num_over_budget > 50:
        revenue = np.copy(data["revenue"])
        cost = np.copy(data["cost"])
        celebrity = np.copy(data["celebrity"])
        length = np.copy(data["length/mins"])
        spend_time = np.copy(data["spend_time/days"])
        is_dubbing = np.copy(data["is_dubbing"])
        for i in range(1000):
            revenue_increase = 0
            if revenue[i] < cost[i]:
                if length[i] <= 120 and length[i] >= 110:
                    revenue_increase += 0.1
                if celebrity[i] >= 10:
                    revenue_increase += 0.1
                if spend_time[i] <= 90:
                    revenue_increase += 0.1
                if is_dubbing[i]:
                    revenue_increase += 0.1
                revenue[i] += (cost[i] - revenue[i]) * (revenue_increase + 1)

                num_over_budget -= 1
                if num_over_budget == 50:
                    break
        data["revenue"] = revenue
    else:
        revenue = np.copy(data["revenue"])
        cost = np.copy(data["cost"])
        celebrity = np.copy(data["celebrity"])
        length = np.copy(data["length/mins"])
        spend_time = np.copy(data["spend_time/days"])
        is_dubbing = np.copy(data["is_dubbing"])
        revenue_decrease = 0
        for i in range(1000):
            if revenue[i] < cost[i]:
                if length[i] > 120 and length[i] < 110:
                    revenue_decrease += 0.1
                if celebrity[i] < 10:
                    revenue_decrease += 0.1
                if spend_time[i] > 90:
                    revenue_decrease += 0.1
                if not is_dubbing[i]:
                    revenue_decrease += 0.1

                revenue[i] -= (revenue[i] - cost[i]) * (revenue_decrease + 1)
                num_over_budget += 1
                if num_over_budget == 50:
                    break
        data["revenue"] = revenue


def calculate_filming_time(data):
    """
    calculate how filming time will affect revenue and cost of the movie
    :return:
    """
    # min spend days define as 30 days
    spend_time = [30 for i in range(1000)]
    revenue = np.copy(data["revenue"])
    cost = np.copy(data["cost"])
    for i in range(1000):
        spend_time_increase = np.random.randint(0, 471)
        if spend_time_increase < 60:  # log(spend_time_increase)*[0,0.1)
            cost_increase = np.log(spend_time_increase + 1) * 0.05
            revenue_increase = np.log(spend_time_increase + 1) * 0.4
        elif spend_time_increase < 90 and spend_time_increase >= 60:  # log(spend_time_increase)*[0,0.2)
            cost_increase = np.log(spend_time_increase + 1) * 0.25
            revenue_increase = np.log(spend_time_increase + 1) * 0.25
        elif spend_time_increase < 200 and spend_time_increase >= 90:
            cost_increase = np.log(spend_time_increase + 1) * 0.2
            revenue_increase = np.log(spend_time_increase + 1) * 0.2
        else:
            cost_increase = np.log(spend_time_increase + 1) * 0.1
            revenue_increase = np.log(spend_time_increase + 1) * 0.1
        spend_time[i] += spend_time_increase
        revenue[i] *= (revenue_increase + 1)
        cost[i] *= (cost_increase + 1)
    data["revenue"] = revenue
    data["cost"] = cost
    data["spend_time/days"] = pd.DataFrame(spend_time)


def calculate_dubbing_effect(data):
    """
    calculate how the sound effect affect the revenue and cost of the movie
    :param is_dubbing:
    :return:
    """
    is_dubbing = [False for _ in range(1000)]
    revenue = np.copy(data["revenue"])
    cost = np.copy(data["cost"])
    for i in range(1000):
        if (np.random.randint(0, 2)):
            is_dubbing[i] = True
            revenue[i] *= (1 + 0.2)
            cost[i] *= (np.random.randint(1, 3) * 0.1 + 1)

    data["revenue"] = revenue
    data["cost"] = cost
    data["is_dubbing"] = is_dubbing


def init_data():
    movie_index = [(np.random.randint(0, 1000) % 10) for _ in range(1000)]

    cost_revenut = define_cost_revenue(movie_index)
    data = get_base_cost_for_movie(movie_index, cost_revenut)
    index = ["movie_type", "revenue", "cost"]
    data = pd.DataFrame(data)
    data.columns = index
    calculate_during_effect(data)
    calculate_the_celebrity_effect(data)
    calculate_filming_time(data)
    calculate_dubbing_effect(data)
    is_over_budget(data)
    return data


def main():
    print("This is the Monte Carlo Simulation for the movie profit!!!")

    # Monte Carlo simulation
    Monte_Carlo_iterater = 100

    verifyHypothesis_1 = []
    verifyHypothesis_2 = []
    verifyHypothesis_3 = []
    verifyHypothesis_4 = []
    verifyHypothesis_5 = []
    for i in range(Monte_Carlo_iterater):
        data = init_data()
        data["revenue-cost"] = data["revenue"] - data["cost"];
        # verify Hypothesis 1
        verifyHypothesis_1.append(data[data["revenue-cost"] == data["revenue-cost"].max()]["celebrity"].values[0])

        # verify Hypothesis 2
        type = data[data["revenue-cost"] == data["revenue-cost"].max()]["movie_type"].values
        count = data[data["movie_type"] == type[0]].shape[0]
        verifyHypothesis_2.append(count / 1000)

        # verify Hypothesis 3
        length = data[data["revenue-cost"] == data["revenue-cost"].max()]["length/mins"].values[0]
        verifyHypothesis_3.append(length)

        # verify Hypothesis 4
        spend = data[data["revenue-cost"] == data["revenue-cost"].max()]["spend_time/days"].values[0]
        verifyHypothesis_4.append(spend)

        # verify Hypothesis 5
        is_dubbing = data[data["revenue-cost"] == data["revenue-cost"].max()]["is_dubbing"].values[0]
        verifyHypothesis_5.append(is_dubbing)

    x = range(Monte_Carlo_iterater)
    plt.title("Hypothesis 1")
    plt.plot(x, verifyHypothesis_1)
    plt.show()

    plt.title("Hypothesis 2")
    plt.plot(x, verifyHypothesis_2)
    plt.show()

    plt.title("Hypothesis 3")
    plt.plot(x, verifyHypothesis_3)
    plt.show()

    plt.title("Hypothesis 4")
    plt.plot(x, verifyHypothesis_4)
    plt.show()

    plt.title("Hypothesis 5")
    plt.plot(x, verifyHypothesis_5)
    plt.show()


if __name__ == '__main__':
    main()
