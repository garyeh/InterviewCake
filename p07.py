# Temperature tracker

# Write a class TempTracker with these methods:
# insert()—records a new temperature
# get_max()—returns the highest temp we've seen so far
# get_min()—returns the lowest temp we've seen so far
# get_mean()—returns the mean ↴ of all temps we've seen so far
# get_mode()—returns a mode ↴ of all temps we've seen so far
# Optimize for space and time. Favor speeding up the getter functions get_max(), get_min(), get_mean(), and get_mode() over speeding up the insert() function.
# get_mean() should return a float, but the rest of the getter functions can return integers. Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..110.

class TempTracker:
    def __init__(self):
        self.min_temp = float('inf')
        self.max_temp = float('-inf')
        self.total_temps = 0
        self.num_temps = 0

        self.max_occurrences = 0
        self.mode = None
        self.occurrences = [0] * (111)

    def insert(self, temperature):
        if temperature > self.max_temp:
            self.max_temp = temperature
        if temperature < self.min_temp:
            self.min_temp = temperature
        self.total_temps += temperature
        self.num_temps += 1
        self.occurrences[temperature] += 1
        if self.occurrences[temperature] > self.max_occurrences:
            self.max_occurrences = self.occurrences[temperature]
            self.mode = temperature

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.total_temps / self.num_temps

    def get_mode(self):
        return self.mode
