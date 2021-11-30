# final_project
# 597 PR final project
# Created by Shihao Jin, Frencis Feng, Yanmeng Xin

import random as random
import pandas as pd
import scipy.stats
import numpy as np

def get_base_cost_for_movie(movie_type: str):
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


def calculate_length_effect(movie_price, length):
    # for sake of the minimum length of 60 minutes for each movie
    length -= 60


def calculate_the_celebrity_effect(movie_price, number_of_celebrity):

    return


def is_over_budget(movie_price):
    # half the chance the budget will be changed by the unexpected event
    if random.random(1, 2) == 1:
        new_weighted_cost = np.random.normal(0.3,0.1)+1
        movie_price[1] *= new_weighted_cost
    return movie_price


def main():


main()