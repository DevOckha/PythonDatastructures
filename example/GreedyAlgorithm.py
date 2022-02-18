#Distance_points: İki nokta arasındaki mutlak mesafeyi hesaplar
#distance_tour: Belirli bir turda satış elemanının kat etmesi gereken toplam mesafeyi hesaplar
#generate_cities:Genişliği 500 ve yüksekliği 300 olan bir dikdörtgende rastgele bir dizi n şehir oluşturur

import random
from itertools import permutations

alltours = permutations

def distance_tour(aTour):
    return sum(distance_points(aTour[i - 1], aTour[i]) for i in range(len(aTour)))

aCity = complex

def distance_points(first, second): return abs(first - second)


def generate_cities(number_of_cities):
    seed=111;width=500;height=300
    random.seed((number_of_cities, seed))
    return frozenset(aCity(random.randint(1, width),random.randint(1, height)) for c in range(number_of_cities))


def brute_force(cities):
    return shortest_tour(alltours(cities))

def shortest_tour(tours): return min(tours, key=distance_tour)


import matplotlib.pyplot as plt

def visualize_tour(tour, style='bo-'):
    if len(tour) > 1000: plt.figure(figsize=(15,10))
    start = tour[0:1]
    visualize_segment(tour + start, style)
    visualize_segment(style, 'rD')
        

def visualize_segment(segment, style='bo-'):
    plt.plot([X(c) for c in segment], [Y(c) for c in segment], style, clip_on=False)
    plt.axis('scaled')
    plt.axis('off')

def X(city): 'X axis'; return city.real
def Y(city): 'Y axis'; return city.imag

    
import time
from collections import Counter

def tsp(algorithm, cities):
    t0 = time.process_time()
    tour = algorithm(cities)
    t1 = time.process_time()
    
    assert Counter(tour) == Counter(cities)
    visualize_tour(tour)
    print(" {}: {} cities => tour lenght {:.0f} (in {:.3f} sec) ".format(name(algorithm), len(tour), distance_tour(tour), t1 - t0))

def name(algorithm): return algorithm.__name__.replace('_tsp', '')


def greedy_algorithm(cities, start=None):
    C = start or first(cities)
    tour = [C]
    unvisited = set(cities - {C})
    while unvisited:
        C = nearest_neighbor(C, unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour

def first(collection): return next(iter(collection))

def nearest_neighbor(A, cities):
    return min(cities, key=lambda C: distance_points(C, A))

tsp(greedy_algorithm, generate_cities(10))
