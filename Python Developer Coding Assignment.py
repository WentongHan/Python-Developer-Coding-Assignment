import json

#read in json file
with open('data.json', 'r') as data_file:
    data_dict = json.load(data_file)

#Process the read data into a dictionary with star’s name as the key
stars_dict = {}
for i in data_dict:
    star_list = i['stars'].split(', ')
    #Count the number of movies starred in and count the total rating score for subsequent calculations
    rating = float(i['rating'])
    for j in star_list:
        if j in stars_dict:
            stars_dict[j][0] += 1
            stars_dict[j][1] += rating
        else:
            stars_dict[j] = [1, rating]

#Delete stars data who have appeared in less than two movies
for i in list(stars_dict.keys()):
    if stars_dict[i][0] == 1:
        del stars_dict[i]

#Create a class to facilitate data management and subsequent operations
class tuple_list:
    def __init__(self, name, num_movies, avg_rating):
        self.name = name
        self.num_movies = num_movies
        self.avg_rating = avg_rating
    def __repr__(self):
        return repr((self.name, self.num_movies, self.avg_rating))

#Convert dictionary to list for easy sorting
stars_list = []
for i in stars_dict:
    stars_list.append(tuple_list(i, stars_dict[i][0], (stars_dict[i][1]/stars_dict[i][0])))

#sort the list base on number of movies
sort_list = sorted(stars_list, key=lambda x: x.num_movies)

#use the given output format
with open('output.txt',"w") as file:
    for i in sort_list:
        file.write("Star Name: %-20s\t\t| Movies:  %-5s| AVG Rating: %.2f\n"%(i.name, i.num_movies, i.avg_rating))
  