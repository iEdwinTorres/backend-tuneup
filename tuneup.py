#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Edwin Torres"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    @functools.wraps(func)
    def profile_wrapper(*args, **kwargs):
        performance_object = cProfile.Profile()
        performance_object.enable()
        result = func(*args, **kwargs)
        performance_object.disable()
        get_stats_obj = pstats.Stats(performance_object)
        get_stats_obj.strip_dirs()
        get_stats_obj.sort_stats('cumulative')
        get_stats_obj.print_stats
        return result
    return profile_wrapper


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movie_list = {}
    movies = read_movies(src)
    for movie in movies:
        if movie_list.get(movie):
            movie_list[movie] += 1
        else:
            movie_list[movie] = 1
    return [k for k, v in movie_list.items() if v > 1]


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(stmt="main()", setup="from __main__ import main")
    results = min(t.repeat(repeat=7, number=5)) /5
    print("Best time across 7 repeats of 5 runs per repeat " + str(results + " sec"))

def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()
