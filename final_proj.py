# final_project
# 597 PR final project
# Created by Shihao Jin, Francis Feng, Yanmeng Xin

import math
import pandas as pd
from numba import jit
import numpy as np
from matplotlib import pyplot as plt


def get_base_cost_for_movie(index, cost_revenue):
    """
    determine the base revenue and cost for each genre of movies which have different base revenue and cost
    :param index: the index list for the cost and revenue
    :param cost_revenue: the cost and revenue list for the movie
    :return: the cost and revenue for the movie
    >>> np.random.seed(0)
    >>> movie_index = [(np.random.randint(0, 1000) % 10) for _ in range(1000)]
    >>> cost_revenues = define_cost_revenue(movie_index)
    >>> tmp = get_base_cost_for_movie(movie_index, cost_revenues)
    >>> tmp[0] == ['horror', 100, 130]
    True
    >>> np.random.seed(1)
    >>> movie_index = [(np.random.randint(0, 1000) % 10) for _ in range(1000)]
    >>> cost_revenues = define_cost_revenue(movie_index)
    >>> tmp = get_base_cost_for_movie(movie_index, cost_revenues)
    >>> tmp[0] == ['crime', 100, 120]
    True
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


def define_cost_revenue(index_list):
    """
    Any type of movie exceeds 30% of total portfolio will lead to a decrease in the base
    revenue because of over-competition, and lower than 5% will increase the base revenue
    because of lack of competition
    :param index_list: the index list of the generated movie portfolio
    :return: the revenue and cost of the list
    >>> cost = define_cost_revenue([1 for _ in range(70)])
    >>> (cost[1])
    [90, 70]
    >>> cost = define_cost_revenue([1 for _ in range(30)])
    >>> cost[1][0] > 90
    True
    """
    np.random.seed(0)
    mu, sigma = 0.3, 0.1
    cost_revenue = [[100, 90], [90, 70], [100, 80],
                    [120, 110], [130, 100], [100, 100],
                    [90, 90], [120, 100], [100, 90], [100, 100]]
    for i in range(10):
        if index_list.count(i) >= 300:
            cost_revenue[i][0] *= 1 - np.random.normal(mu, sigma)
        elif index_list.count(i) < 50:
            cost_revenue[i][0] *= 1 + np.random.normal(mu, sigma)
    return cost_revenue


def calculate_duration_effect(data):
    """
    calculate how the movie duration will change the revenue and cost
    :param data: the data of revenue and cost the duration
    :return: the adjusted data of the data revenue and cost
    """
    np.random.seed(0)
    # for sake of the minimum length of 60 minutes for each movie
    length = [60 for _ in range(1000)]
    revenue = np.copy(data["revenue"])
    cost = np.copy(data["cost"])
    for i in range(1000):
        # normal distribution of the increased length with the mean 60 and sd 20
        length_increase = math.ceil(np.random.normal(90, 18))
        increase = get_length_increase(length_increase)
        revenue_increase = increase[1]
        cost_increase = increase[0]
        length[i] += length_increase
        revenue[i] *= (revenue_increase + 1)
        cost[i] *= cost_increase + 1
    data["revenue"] = revenue
    data["cost"] = cost
    data["length_per_min"] = pd.DataFrame(length)
    # random increase cost and revenue


@jit
def get_length_increase(length_increase):
    """
    get the length increase of the effect
    :param length_increase: the length increase time
    :return:
    >>> tmp = get_length_increase(30)
    >>> tmp
    (0.8584968011212866, 0.8584968011212866)
    >>> tmp = get_length_increase(70)
    >>> tmp
    (1.0656699692603289, 1.0656699692603289)
    """
    if length_increase < 0:
        length_increase = 0
    if length_increase < 30:
        cost_increase = np.log(length_increase + 1) * 0.2
        revenue_increase = np.log(length_increase + 1) * 0.4
    elif 90 > length_increase >= 30:
        cost_increase = np.log(length_increase + 1) * 0.25
        revenue_increase = np.log(length_increase + 1) * 0.25
    else:
        cost_increase = np.log(length_increase + 1) * 0.1
        revenue_increase = np.log(length_increase + 1) * 0.1
    return cost_increase, revenue_increase


def calculate_the_celebrity_effect(data):
    """
    calculate how the number of celebrity will affect the movie's revenue and cost
    :param data: the data of revenue and cost the duration
    :return: the adjusted data of the data revenue and cost
    """
    np.random.seed(0)
    revenue = np.copy(data["revenue"])
    #    cost = np.copy(data["cost"])
    celebrity_num = [0 for _ in range(1000)]
    for i in range(1000):
        celebrity_num[i] = math.ceil(np.random.normal(5, 1.2))  # min_celebrity_num = 0  max_celebrity_num = 20
        revenue_increase = np.log(celebrity_num[i] + 1) * np.random.rand() * 0.1
        revenue[i] *= (revenue_increase + 1)
    data["revenue"] = revenue
    data["celebrity"] = celebrity_num


def is_over_budget(data):
    """
    determine whether movie will be over budget and how it will change the cost and revenue
    :param data: the data of the original value before adjustment
    :return: the data of revenue and cost adjusted the effect of over budget
    """
    np.random.seed(0)
    revenue = np.copy(data["revenue"])
    for i in range(1000):
        if np.random.randint(1, 100) > 6:
            continue
        revenue[i] *= 1 + np.random.normal(0.3, 0.1)
    data["revenue"] = revenue
    # num_over_budget = data[data["cost"] > data["revenue"]].shape[0]
    # if num_over_budget > 50:
    #     revenue = np.copy(data["revenue"])
    #     cost = np.copy(data["cost"])
    #     celebrity = np.copy(data["celebrity"])
    #     length = np.copy(data["length_per_min"])
    #     spend_time = np.copy(data["spend_time/days"])
    #     is_dubbing = np.copy(data["is_dubbing"])
    #     for i in range(1000):
    #         revenue_increase = 0
    #         if revenue[i] < cost[i]:
    #             if 120 >= length[i] >= 110:
    #                 revenue_increase += 0.1
    #             if celebrity[i] >= 10:
    #                 revenue_increase += 0.1
    #             if spend_time[i] <= 90:
    #                 revenue_increase += 0.1
    #             if is_dubbing[i]:
    #                 revenue_increase += 0.1
    #             revenue[i] += (cost[i] - revenue[i]) * (revenue_increase + 1)
    #
    #             num_over_budget -= 1
    #             if num_over_budget == 50:
    #                 break
    #     data["revenue"] = revenue
    # else:
    #     revenue = np.copy(data["revenue"])
    #     cost = np.copy(data["cost"])
    #     celebrity = np.copy(data["celebrity"])
    #     length = np.copy(data["length_per_min"])
    #     spend_time = np.copy(data["spend_time/days"])
    #     is_dubbing = np.copy(data["is_dubbing"])
    #     revenue_decrease = 0
    #     for i in range(1000):
    #         if revenue[i] < cost[i]:
    #             if 120 < length[i] < 110:
    #                 revenue_decrease += 0.1
    #             if celebrity[i] < 10:
    #                 revenue_decrease += 0.1
    #             if spend_time[i] > 90:
    #                 revenue_decrease += 0.1
    #             if not is_dubbing[i]:
    #                 revenue_decrease += 0.1
    #
    #             revenue[i] -= (revenue[i] - cost[i]) * (revenue_decrease + 1)
    #             num_over_budget += 1
    #             if num_over_budget == 50:
    #                 break
    #     data["revenue"] = revenue


def calculate_filming_time(data):
    """
    calculate how filming time will affect revenue and cost of the movie
    :param data: the data of the original value before adjustment
    :return: the data of revenue and cost adjusted the effect of filming time
    """
    # min spend days define as 30 days
    spend_time = [30 for _ in range(1000)]
    revenue = np.copy(data["revenue"])
    cost = np.copy(data["cost"])
    for i in range(1000):
        spend_time_increase = np.random.normal(90, 12)
        increase = get_time_increase(spend_time_increase)
        cost_increase = increase[0]
        revenue_increase = increase[1]
        spend_time[i] += spend_time_increase
        revenue[i] *= revenue_increase + 1
        cost[i] *= (cost_increase + 1)
    data["revenue"] = revenue
    data["cost"] = cost
    data["spend_time/days"] = pd.DataFrame(spend_time)


@jit
def get_time_increase(spend_time_increase):
    """
    calculate the effect of the time increase
    :param spend_time_increase: the increased amount of time
    :return: the effect number of the effect
    >>> tmp = get_time_increase(40)
    >>> tmp
    (0.2511879584971126, 0.1559729458245868)
    >>> tmp = get_time_increase(100)
    >>> tmp
    (1.3980195544500345, 0.9414918407912269)
    """
    np.random.seed(0)
    if spend_time_increase < 60:  # log(spend_time_increase)*[0,0.1)
        cost_increase = np.log(spend_time_increase + 1) * np.random.normal(0.05, 0.01)
        revenue_increase = np.log(spend_time_increase + 1) * np.random.normal(0.04, 0.005)
    elif 90 > spend_time_increase >= 60:  # log(spend_time_increase)*[0,0.2)
        cost_increase = np.log(spend_time_increase + 1) * np.random.normal(0.20, 0.01)
        revenue_increase = np.log(spend_time_increase + 1) * np.random.normal(0.25, 0.03)
    elif 200 > spend_time_increase >= 90:
        cost_increase = np.log(spend_time_increase + 1) * np.random.normal(0.25, 0.03)
        revenue_increase = np.log(spend_time_increase + 1) * np.random.normal(0.20, 0.01)
    else:
        cost_increase = np.log(spend_time_increase + 1) * np.random.normal(1, 0.2)
        revenue_increase = np.log(spend_time_increase + 1) * np.random.normal(0.8, 0.15)
    return cost_increase, revenue_increase


def calculate_dubbing_effect(data):
    """
    calculate how the sound effect affect the revenue and cost of the movie
    :param data: the data of the original value before adjustment
    :return: the data of the cost and revenue after adjustment by the dubbing effect
    """
    np.random.seed(0)
    is_dubbing = [False for _ in range(1000)]
    revenue = np.copy(data["revenue"])
    cost = np.copy(data["cost"])
    for i in range(1000):
        get_dubbing_effect(is_dubbing, revenue, cost, i)
    data["revenue"] = revenue
    data["cost"] = cost
    data["is_dubbing"] = is_dubbing


def get_dubbing_effect(is_dubbing, revenue, cost, i):
    """
    applied the effect of dubbing to each
    :param is_dubbing: the row of whether it is dubbing
    :param revenue: the revenue row of the data
    :param cost: the cost row of the data
    :param i: the number of the row of the data
    :return: not return anything
    >>> revenue_data = [100]
    >>> cost_data = [100]
    >>> dubbing = [True]
    >>> get_dubbing_effect(dubbing, revenue_data, cost_data, 0)
    >>> revenue_data
    [123.82026172983834]
    >>> revenue_data = [100]
    >>> cost_data = [100]
    >>> dubbing = [True]
    >>> get_dubbing_effect(dubbing, revenue_data, cost_data, 0)
    >>> cost_data
    [103.40015720836722]
    """
    np.random.seed(0)
    is_dubbing[i] = True
    random_num = np.random.normal(0.15, 0.05)
    if random_num < 0:
        random_num = 0
    revenue[i] *= (1 + random_num)
    random_num = np.random.normal(0.03, 0.01)
    if random_num < 0:
        random_num = 0
    cost[i] *= random_num + 1


def init_data():
    """
    initialize all the data
    :return: the initialized data containing all the information
    """
    np.random.seed(0)
    movie_index = [(np.random.randint(0, 1000) % 10) for _ in range(1000)]
    cost_revenues = define_cost_revenue(movie_index)
    data = get_base_cost_for_movie(movie_index, cost_revenues)
    index = ["movie_type", "revenue", "cost"]
    data = pd.DataFrame(data)
    data.columns = index
    calculate_duration_effect(data)
    calculate_the_celebrity_effect(data)
    calculate_filming_time(data)
    calculate_dubbing_effect(data)
    is_over_budget(data)
    return data


def main():
    print("This is the Monte Carlo Simulation for the movie profit!!!")
    monte_carlo_iterator = eval(input("How many times do you want to run the simulation? (at least 50 times) "))
    if monte_carlo_iterator < 50:
        monte_carlo_iterator = 50
    # self_input = input("Do you want to customize the movie portfolio (y/n)? ")
    # if self_input.lower().startswith("y"):
    #     action_type = eval(input("How many action type do you want to have? (0-1000) "))
    #     comedy_type = eval(input("How many comedy type do you want to have? (0-1000) "))
    #     drama_type = eval(input("How many drama type do you want to have? (0-1000) "))
    #     fantasy_type = eval(input("How many fantasy type do you want to have? (0-1000) "))
    #     horror_type = eval(input("How many horror type do you want to have? (0-1000) "))
    #     mystery_type = eval(input("How many mystery type do you want to have? (0-1000) "))
    #     romance_type = eval(input("How many romance type do you want to have? (0-1000) "))
    #     crime_type = eval(input("How many crime type do you want to have? (0-1000) "))
    #     animation_type = eval(input("How many animation type do you want to have? (0-1000) "))
    #     if action_type + comedy_type + drama_type + fantasy_type + horror_type + mystery_type + romance_type + \
    #             crime_type + animation_type > 1000:
    #         print("Please make sure you have no more than 1000 movies in total")
    #     print("the number of thriller type will be determined by the previous entered number")
    #     thriller_type = 1000 - action_type - comedy_type - drama_type - fantasy_type - horror_type - mystery_type - \
    #                     romance_type - crime_type - animation_type
    #     for i in range(action_type):
    #         movie_index.append(0)
    #     for i in range(comedy_type):
    #         movie_index.append(1)
    #     for i in range(drama_type):
    #         movie_index.append(2)
    #     for i in range(fantasy_type):
    #         movie_index.append(3)
    #     for i in range(horror_type):
    #         movie_index.append(4)
    #     for i in range(mystery_type):
    #         movie_index.append(5)
    #     for i in range(romance_type):
    #         movie_index.append(6)
    #     for i in range(crime_type):
    #         movie_index.append(7)
    #     for i in range(animation_type):
    #         movie_index.append(8)
    #     for i in range(thriller_type):
    #         movie_index.append(9)

    verify_hypothesis_1 = []
    verify_hypothesis_2 = []
    verify_hypothesis_3 = []
    verify_hypothesis_4 = []
    verify_hypothesis_5 = []

    for i in range(monte_carlo_iterator):
        data = init_data()
        data["revenue-cost"] = data["revenue"] - data["cost"]
        # verify Hypothesis 1
        verify_hypothesis_1.append(data[data["revenue-cost"] == data["revenue-cost"].max()]["celebrity"].values[0])

        # verify Hypothesis 2
        hypo2 = data[data["revenue-cost"] == data["revenue-cost"].max()]["movie_type"].values
        count = data[data["movie_type"] == hypo2[0]].shape[0]
        verify_hypothesis_2.append(count / 1000)

        # verify Hypothesis 3
        length = data[data["revenue-cost"] == data["revenue-cost"].max()]["length_per_min"].values[0]
        verify_hypothesis_3.append(length)

        # verify Hypothesis 4
        spend = data[data["revenue-cost"] == data["revenue-cost"].max()]["spend_time/days"].values[0]
        verify_hypothesis_4.append(spend)

        # verify Hypothesis  5
        is_dubbing = data[data["revenue-cost"] == data["revenue-cost"].max()]["is_dubbing"].values[0]
        verify_hypothesis_5.append(is_dubbing)

    x = range(monte_carlo_iterator)
    plt.title("Hypothesis 1")
    plt.plot(x, verify_hypothesis_1)
    plt.show()

    plt.title("Hypothesis 2")
    plt.plot(x, verify_hypothesis_2)
    plt.show()

    plt.title("Hypothesis 3")
    plt.plot(x, verify_hypothesis_3)
    plt.show()

    plt.title("Hypothesis 4")
    plt.plot(x, verify_hypothesis_4)
    plt.show()

    plt.title("Hypothesis 5")
    plt.plot(x, verify_hypothesis_5)
    plt.show()


if __name__ == '__main__':
    main()
