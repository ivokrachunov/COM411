
'''
def observed() :
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations

def run_task1():
    result = observed()
    print(result)
# Call the function to see the set of observations
run_task1()
'''

'''
def observed_items():
    observations = []
    for _ in range(7):
        value = input("Enter an observation: ")
        observations.append(value)
    return observations


def run_task2():
    print("Counting observations...")
    observations_list = observed_items()

    observations_set = set()
    for value in observations_list:
        count = observations_list.count(value)
        observation_tuple = (value, count)
        observations_set.add(observation_tuple)

    print("Observations set:", observations_set)


# Run the second function
run_task2()
'''


'''
def observed_items():
    observations = []
    for _ in range(5):
        value = input("Enter an observation: ")
        observations.append(value)
    return observations

def remove_observations(observations):
    remove_flag = input("Do you wish to remove observations? (yes/no): ").lower()
    while remove_flag == "yes":
        to_remove = input("Enter the observation to be removed: ")
        if to_remove in observations:
            observations.remove(to_remove)
            print(f"{to_remove} removed from the list.")
        else:
            print(f"{to_remove} not found in the list.")
        remove_flag = input("Do you wish to remove more observations? (yes/no): ").lower()

def run_task3():
    observations_list = observed_items()
    remove_observations(observations_list)
    sorted_observations = sorted(observations_list)
    unique_observations = set(sorted_observations)
    for unique_observation in unique_observations:
        count = sorted_observations.count(unique_observation)
        print(f"{unique_observation}: {count} times")

# Call the main function
run_task3()
'''


