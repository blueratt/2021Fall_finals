import pytest

from final_proj import get_base_cost_for_movie
import numpy as np
from final_proj import define_cost_revenue
from final_proj import get_length_increase
from final_proj import get_time_increase
from final_proj import get_dubbing_effect


def test_get_base_cost_for_movie_1():
    np.random.seed(0)
    movie_index = [(np.random.randint(0, 1000) % 10) for _ in range(1000)]
    cost_revenues = define_cost_revenue(movie_index)
    tmp = get_base_cost_for_movie(movie_index, cost_revenues)
    assert tmp[0] == ['horror', 100, 130]


def test_get_base_cost_for_movie_2():
    np.random.seed(1)
    movie_index = [(np.random.randint(0, 1000) % 10) for _ in range(1000)]
    cost_revenues = define_cost_revenue(movie_index)
    tmp = get_base_cost_for_movie(movie_index, cost_revenues)
    assert tmp[0] == ['crime', 100, 120]


def test_define_cost_revenue_1():
    cost = define_cost_revenue([1 for _ in range(70)])
    assert (cost[1]) == [90, 70]


def test_define_cost_revenue_2():
    cost = define_cost_revenue([1 for _ in range(30)])
    assert cost[1][0] > 90


def test_get_length_increase_1():
    tmp = get_length_increase(30)
    assert tmp == (0.8584968011212866, 0.8584968011212866)


def test_get_length_increase_2():
    tmp = get_length_increase(70)
    assert tmp == (1.0656699692603289, 1.0656699692603289)


def test_get_time_increase_1():
    tmp = get_time_increase(40)
    assert tmp == (0.2511879584971126, 0.1559729458245868)


def test_get_time_increase_2():
    tmp = get_time_increase(100)
    assert tmp == (1.3980195544500345, 0.9414918407912269)


def test_get_dubbing_effect_1():
    revenue_data = [100]
    cost_data = [100]
    dubbing = [True]
    get_dubbing_effect(dubbing, revenue_data, cost_data, 0)
    assert revenue_data == [123.82026172983834]


def test_get_dubbing_effect_2():
    revenue_data = [100]
    cost_data = [100]
    dubbing = [True]
    get_dubbing_effect(dubbing, revenue_data, cost_data, 0)
    assert cost_data == [103.40015720836722]
