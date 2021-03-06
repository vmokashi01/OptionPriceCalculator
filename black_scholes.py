import math
from scipy.stats import norm

def d1(S, K, r, sigma, T):
    # S - stock price
    # K - exercise price
    # r - risk free return
    # sigma - std deviation of log returns
    # T - time to exercise date
    return (math.log(S/K) + ((r + (sigma * sigma)/2) * T))/(sigma * math.sqrt(T))


def d2(S, K, r, sigma, T):
    # S - stock price
    # K - exercise price
    # r - risk free return
    # sigma - std deviation of log returns
    # T - time to exercise date
    return (math.log(S/K) + ((r - (sigma * sigma)/2) * T))/(sigma * math.sqrt(T))


#---------EUROPEAN CALL----------#

def black_scholes_call(S, K, r, sigma, T):

    d_one = d1(S, K, r, sigma, T)
    d_two = d2(S, K, r, sigma, T)
    return "European Call Option Price: $" + "%.2f" % round((S * norm.cdf(d_one)) - ((K * math.exp(-r * T)) * norm.cdf(d_two)), 2)

#---------EUROPEAN PUT----------#

def black_scholes_put(S, K, r, sigma, T):

    d_one = d1(S, K, r, sigma, T)
    d_two = d2(S, K, r, sigma, T)
    return "European Put Option Price: $" + "%.2f" % round((norm.cdf(-1 * d_two) * (K * math.exp(-r * T))) - (S * norm.cdf(-1 * d_one)), 2)


