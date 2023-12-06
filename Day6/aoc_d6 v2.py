# Advent of Code Day6 challenge - Psrt 2
import sys
import math

def calculate_points(time_: int, distance_:int) -> int:
    """calculates the number of possibilities to surpass the distance record
    It calculates the distance between the soluttions for the cubic equation 
    -ax^2 + bx -c 
    where a=1, b=time and c=distance
    and the solution requires floor(abs(x1-x2) +1

    Args:
        time_ (int): time limit
        distance_ (int): distance record

    Returns:
        int: number of solutions
        
    Special case: the solution requires a srict inequality, therefore, for just equality for an integer number, we have to distract two points from the total
    """
    x1 = math.ceil((time_ - math.sqrt(time_**2 - 4*distance_))/2)
    x2 = math.floor((time_ + math.sqrt(time_**2 - 4*distance_))/2)
    
    if math.isclose(math.sqrt(time_**2 - 4*distance_), math.floor(math.sqrt(time_**2 - 4*distance_))):
        corrector = - 1 # +1-2
    else:
        corrector = + 1
    print(x1, x2)
    return x2-x1 + corrector

# with open('C:\\Users\\Noybeyto\\_Projects\\Schema\\Python courses\\AoC2023\\AoC_2023\\Day6\\input.txt', "rt") as infile:
#     time_ = infile.readline()
#     distance_ = infile.readline()
#     times = list(map(int, time_.split()[1:]))
#     distances = list(map(int, distance_.split()[1:]))
#     product = 1
    
#     for pair in zip(times, distances):
#         points_ = calculate_points(pair[0], pair[1])
#         product *= points_
#         print(pair, "-->", points_)
# run the test first:  product = calculate_points(71530, 940200)
product = calculate_points(51699878, 377117112241505)
        
print(product)