# Inflight Entertainment
# O(n) time

# Write a function that takes an integer flight_length (in minutes) and
# a list of integers movie_lengths (in minutes) and returns a boolean
# indicating whether there are two numbers in movie_lengths
# whose sum equals flight_length.

def can_watch_two_movies(flight_length, movie_lengths):
    difference_lengths = set()
    for length in movie_lengths:
        if length in difference_lengths:
            return True

        difference_lengths.add(flight_length - length)
    return False

movies = [1,3,5,6,98]
print can_watch_two_movies(99, movies)
