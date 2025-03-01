# """ This script prints a string. """

# LINE = "yo"
# print(LINE)

# test = "bruh"

# print(test)

# """
# keep track of lowest population + name, make comparison as we iterate, then reassign?

# HANDLE LOWEST INDEX LATER?! -> this is handled in our condition check
# """

# # dict = {} # item of the list

# # dict.get("population", 0) -> 84

# import math

# def most_endangered(species_list):
#     if not species_list:
#         return None
#     minName = ""
#     minPop = 999999999999
#     for item in species_list:
#         if item["population"] < minPop:
#             minPop = item["population"]
#             minName = item["name"]


#     return minName



# species_list = [
#     {"name": "Amur Leopard",
#      "habitat": "Temperate forests",
#      "population": 84
#     },
#     {"name": "Javan Rhino",
#      "habitat": "Tropical forests",
#      "population": 72
#     },
#     {"name": "Vaquita",
#      "habitat": "Marine",
#      "population": 10
#     },
#     {"name": "BROROR",
#      "habitat": "asfas",
#      "population": 10
#     }
# ]

# print(most_endangered(species_list))



# def count_endangered_species(endangered_species, observed_species):
#     if not endangered_species or not observed_species:
#         return 0
#     x = set(endangered_species)
#     counter = 0
#     for s in observed_species:
#         if s in x:
#             counter += 1

#     return counter






# endangered_species1 = "aA"
# observed_species1 = "aAAbbbb"

# endangered_species2 = "z"
# observed_species2 = "ZZ"

# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2))  


def navigate_research_station(station_layout, observations):
    # Create a dictionary to map each letter to its index in the station layout
    station_index = {char: idx for idx, char in enumerate(station_layout)}

    track = 0
    current_position = 0  # Start from the first position in the station layout

    for obs in observations:
        if obs in station_index:  # Only process if the letter exists in the layout
            track += abs(station_index[obs] - current_position)  # Move to the new observation
            current_position = station_index[obs]  # Update current position

    return track


# Test cases
station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  # Expected: 45
print(navigate_research_station(station_layout2, observations2))  # Expected: 4
