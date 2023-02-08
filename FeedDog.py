# Name: Peter Orndoff
# Class: CS 325 - Analysis of Algorithms.
# Description: Given a list of hungry dogs & biscuits, returns the maximum number of dogs that can be fed.

def feedDog(dog_hunger_list, biscuit_list):
    """
    Greedy Algorithm Implementation. Both lists are iterated through which results in a (O)n^2 worst case runtime.

    :param dog_hunger_list: Passed hunger level of dogs
    :param biscuit_list: Passed biscuit size
    :return: Returns the number of Dogs that can be fed
    """

    # Start by sorting passed lists from large to small values.

    number_of_biscuits = len(biscuit_list)  # Grabs number of biscuits
    number_of_dogs = len(dog_hunger_list)  # Grabs number of dogs.
    potential_fed_dogs = 0  # Starts increment counter

    sorted(dog_hunger_list)
    sorted(biscuit_list)

    if number_of_biscuits > number_of_dogs:
        innerloop = number_of_biscuits - 1
        outerloop = number_of_dogs - 1
    else:
        innerloop = number_of_dogs - 1
        outerloop = number_of_biscuits - 1

    for i in range(1):

        if number_of_biscuits == number_of_dogs:
            if biscuit_list[number_of_biscuits-1] >= dog_hunger_list[number_of_dogs-1]:
                potential_fed_dogs +=1

        for j in range(innerloop):

            if j > number_of_dogs-1:
                return potential_fed_dogs

            if i > number_of_biscuits-1:
                return potential_fed_dogs


            if biscuit_list[i] >= dog_hunger_list[j]:
                potential_fed_dogs += 1
                i += 1

    return potential_fed_dogs