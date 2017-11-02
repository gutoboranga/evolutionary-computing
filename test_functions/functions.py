from math import cos, sqrt, pow

def drop_wave(x1, x2):
    result = 1 + cos(12 * sqrt(pow(x1, 2) + pow(x2, 2)))
    result = result / ((1 / 2) * (pow(x1, 2) + pow(x2, 2)) + 2)
    result = result * (-1)
    
    return result

def shubert(x1, x2):
    x1_sum = 0
    x2_sum = 0
    
    for i in range(1,6):
        x1_sum += i * cos(((i + 1) * x1) + 1)
        x2_sum += i * cos(((i + 1) * x2) + 1)
    
    result = (x1_sum * x2_sum) * (-1)
    
    return result

def six_hump_camel_back(x1, x2):
    result = (4 - (2.1 * pow(x1, 2)) + (pow(x1, 4) / 3)) * pow(x1, 2)
    result = result + (x1 * x2) + ((-4 + (4 * pow(x2, 2))) * pow(x2, 2))
    
    return result
