# final_project
# 597 PR final project
# Created by Shihao Jin, Frencis Feng, Yanmeng Xin

import random as random
import pandas as pd
import scipy.stats
import numpy as np


def get_base_cost_for_movie(movie_type: str):
    """
    determine the base revenue and cost for each genre of movies which have different base revenue and cost
    :param movie_type:
    :return:
    """
    if movie_type == 'action':
        cost = 100
        revenue = 100
    elif movie_type == 'comedy':
        cost = 100
        revenue = 100
    elif movie_type == 'drama':
        cost = 100
        revenue = 100
    elif movie_type == 'fantasy':
        cost = 100
        revenue = 100
    elif movie_type == 'horror':
        cost = 100
        revenue = 100
    elif movie_type == 'mystery':
        cost = 100
        revenue = 100
    elif movie_type == 'romance':
        cost = 100
        revenue = 100
    elif movie_type == 'crime':
        cost = 100
        revenue = 100
    elif movie_type == 'animation':
        cost = 100
        revenue = 100
    # movie_type == 'thriller':
    else:
        cost = 100
        revenue = 100
    return [revenue, cost]


def calculate_during_effect(movie_price, length):
    """
    calculate how the movie duration will change the revenue and cost
    :param movie_price:
    :param length:
    :return:
    """
    # for sake of the minimum length of 60 minutes for each movie
    length -= 60


def calculate_the_celebrity_effect(movie_price, number_of_celebrity):
    """
    calculate how the number of celebrity will affect the movie's revenue and cost
    :param movie_price:
    :param number_of_celebrity:
    :return:
    """
    revenue = movie_price[0]
    cost = movie_price[1]
    base_cost_celebrity = 20

    return


def is_over_budget(movie_price):
    """
    determine whether movie will be over budget and how it will change the cost and revenue
    :param movie_price:
    :return:
    """
    # half the chance the budget will be changed by the unexpected event
    if random.random(1, 2) == 1:
        new_weighted_cost = np.random.normal(0.3,0.1)+1
        movie_price[1] *= new_weighted_cost
    return movie_price


def calculate_filming_time(movie_price, number_of_filming_day):
    """
    calculate how filming time will affect revenue and cost of the movie
    :return:
    """


def calculate_dubbing_effect(is_dubbing):
    """
    calculate how the sound effect affect the revenue and cost of the movie
    :param is_dubbing:
    :return:
    """


def main():
    print("This is the Monte Carlo Simulation for the movie profit!!!")


main()
