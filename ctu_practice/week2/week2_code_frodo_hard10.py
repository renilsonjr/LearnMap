# 10. Write a program that reads a city name (input) and looks it up in a hard-coded 
# dictionary of city populations; if found, use a nested `if` to print `"Large city"` 
# (population > 1,000,000) or `"Small city"` otherwise; if not found in the dictionary,
# print `"Unknown city"`.

city_populations = {'New York': 2000000, 'new jersey': 1000000, 'connecticut': 50000}
population = input(('What is the city name?'))
if population in city_populations:
    if city_populations[population] > 1000000:
        print('Large city')
    else:
        print('Small city')
else:
    print('Unknown city')

     

    




#