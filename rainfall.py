"""Rainfall
6 kyu

URL:https://www.codewars.com/kata/56a32dd6e4f4748cc3000006/train/python

data and data1 are two strings with rainfall records of a few cities for 
months from January to December. The records of towns are separated by
\n. The name of each town is followed by :.
data and towns can be seen in "Your Test Cases:".

Task:
function: mean(town, strng) should return the average of rainfall for 
the city town and the strng data or data1 (In R and Julia this function
is called avg).
function: variance(town, strng) should return the variance of rainfall 
for the city town and the strng data or data1.

Examples:
mean("London", data), 51.19(9999999999996) 
variance("London", data), 57.42(833333333374)

Notes:
if functions mean or variance have as parameter town a city which has 
no records return -1 or -1.0 (depending on the language)
Don't truncate or round: the tests will pass if abs
(your_result - test_result) <= 1e-2 or abs((your_result - test_result) 
/ test_result) <= 1e-6 depending on the language.
Shell tests only variance
A ref: http://www.mathsisfun.com/data/standard-deviation.html
data and data1 (can be named d0 and d1 depending on the language; 
see "Sample Tests:") are adapted from: http://www.worldclimate.com
"""

import re


# def _get_towns(data):
#     towns = re.findall('(\S+):', data)
#     return towns


# def _m_start(months):
#     m_start = []
#     m = 12
#     lengths = len(_get_towns(months))
#     for i in range(1, lengths + 1):
#         m_start.append(i * 12)
#     return m_start


# def _rainfall(data):
#     rainfall = re.findall('([0-9]+.[0-9]+)', data)
#     return rainfall


# def _rainfall_means(means):
#     m_start = _m_start(means)
#     rainfall = _rainfall(means)
#     lengths = len(_get_towns(means))
#     avg_lst = []
#     month = 12
#     count = 0
#     while count < lengths:
#         for i in m_start:
#             sum_i = 0
#             for ii in range(month*count, i):
#                 sum_i += float(rainfall[ii])
#             avg = sum_i / month
#             avg_lst.append(avg)
#             count += 1
#     return avg_lst


# def _rainfall_var(variance):
#     m_start = _m_start(variance)
#     rainfall = _rainfall(variance)
#     lengths = len(_get_towns(variance))
#     avg_lst = _rainfall_means(variance)
#     var_lst = []
#     month = 12
#     count = 0
#     while count < lengths:
#         for i in m_start:
#             sum_i = 0
#             for ii in range(month*count, i):
#                 sum_i += (float(rainfall[ii]) - (avg_lst[count])) **2
#             var = sum_i / month
#             var_lst.append(var)
#             count += 1
#     return var_lst


# def mean(town, strng):
#     towns = _get_towns(strng)
#     avg_lst = _rainfall_means(strng)
#     for t, a in zip(towns, avg_lst):
#         if t == town:
#             return a
#     else:
#         return -1


# def variance(town, strng):
#     towns = _get_towns(strng)
#     var_lst = _rainfall_var(strng)
#     for t, v in zip(towns, var_lst):
#         if t == town:
#             return v
#     else:
#         return -1
  
#-----------------------------------------------------------------

def _get_towns_stats(strng):
    town_stats_d = {}

    towns_strng = strng.split('\n')
    for ts in towns_strng:
        town_split = ts.split(':')
        town, month_rainfalls = town_split[0], town_split[1].split(',')
        rainfalls = [float(mr.split(' ')[1]) for mr in month_rainfalls]
        # print(rainfalls)

        n = len(rainfalls)
        _mean = sum(rainfalls) / n
        # print(_mean)
        _var = sum([(r - _mean) ** 2 for r in rainfalls]) / n
        # print(_variance)
        town_stats_d[town] = {'mean': _mean, 'var': _var}
    return town_stats_d


def mean_split(town, strng):
    town_stats_d = _get_towns_stats(strng)
    if town in town_stats_d:
        return town_stats_d[town]['mean']
    else:
        return -1


def variance_split(town, strng):
    town_stats_d = _get_towns_stats(strng)
    if town in town_stats_d:
        return town_stats_d[town]['var']
    else:
        return -1


def main():
    # # Output:
    data = """Rome:Jan 81.2,Feb 63.2,Mar 70.3,Apr 55.7,May 53.0,Jun 36.4,Jul 17.5,Aug 27.5,Sep 60.9,Oct 117.7,Nov 111.0,Dec 97.9
London:Jan 48.0,Feb 38.9,Mar 39.9,Apr 42.2,May 47.3,Jun 52.1,Jul 59.5,Aug 57.2,Sep 55.4,Oct 62.0,Nov 59.0,Dec 52.9
Paris:Jan 182.3,Feb 120.6,Mar 158.1,Apr 204.9,May 323.1,Jun 300.5,Jul 236.8,Aug 192.9,Sep 66.3,Oct 63.3,Nov 83.2,Dec 154.7
NY:Jan 108.7,Feb 101.8,Mar 131.9,Apr 93.5,May 98.8,Jun 93.6,Jul 102.2,Aug 131.8,Sep 92.0,Oct 82.3,Nov 107.8,Dec 94.2
Vancouver:Jan 145.7,Feb 121.4,Mar 102.3,Apr 69.2,May 55.8,Jun 47.1,Jul 31.3,Aug 37.0,Sep 59.6,Oct 116.3,Nov 154.6,Dec 171.5
Sydney:Jan 103.4,Feb 111.0,Mar 131.3,Apr 129.7,May 123.0,Jun 129.2,Jul 102.8,Aug 80.3,Sep 69.3,Oct 82.6,Nov 81.4,Dec 78.2
Bangkok:Jan 10.6,Feb 28.2,Mar 30.7,Apr 71.8,May 189.4,Jun 151.7,Jul 158.2,Aug 187.0,Sep 319.9,Oct 230.8,Nov 57.3,Dec 9.4
Tokyo:Jan 49.9,Feb 71.5,Mar 106.4,Apr 129.2,May 144.0,Jun 176.0,Jul 135.6,Aug 148.5,Sep 216.4,Oct 194.1,Nov 95.6,Dec 54.4
Beijing:Jan 3.9,Feb 4.7,Mar 8.2,Apr 18.4,May 33.0,Jun 78.1,Jul 224.3,Aug 170.0,Sep 58.4,Oct 18.0,Nov 9.3,Dec 2.7
Lima:Jan 1.2,Feb 0.9,Mar 0.7,Apr 0.4,May 0.6,Jun 1.8,Jul 4.4,Aug 3.1,Sep 3.3,Oct 1.7,Nov 0.5,Dec 0.7"""
    
    # print(_get_towns(data))
    # print(_m_start(data))
    # print(_rainfall(data))
    # print(_rainfall_means(data))
    # print(_rainfall_var(data))
    print(_get_towns_stats(data))
    
    # print(mean_("London", data))  #mean(town, strng):
    # print(mean("Rome", data))
    # print(mean("Caracas", data))
    # print(mean("Vancouver", data))
    # print(variance("London", data))
    # print(variance("Rome", data))
    # print(variance("Caracas", data))
    # print(variance("Vancouver", data))



    print(mean_split("London", data))  #mean(town, strng):
    print(mean_split("Rome", data))
    print(mean_split("Caracas", data))
    print(variance_split("London", data))
    print(variance_split("Rome", data))
    print(variance_split("Caracas", data))

    # towns = ["Rome", "London", "Paris", "NY", "Vancouver", "Sydney", "Bangkok", "Tokyo",
    #          "Beijing", "Lima", "Montevideo", "Caracas", "Madrid", "Berlin"]

    # def assertFuzzyEquals(actual, expected):
    #     merr = 1e-2   # 1 * 10^-2
    #     inrange = abs(actual - expected) <= merr
    #     msg = ""
    #     if (inrange == False):
    #         msg = "abs(actual - expected) must be <= 1e-2. With 10 decimals: Expected was {:.10f} but got {:.10f}".format(expected, actual)
    #         raise Exception(msg)

    # assertFuzzyEquals(mean("London", data), 51.199999999999996)
    # assertFuzzyEquals(mean("Beijing", data), 52.416666666666664)

    # assertFuzzyEquals(variance("London", data), 57.42833333333374)
    # assertFuzzyEquals(variance("Beijing", data), 4808.37138888889)


if __name__ == '__main__':
    main()

