import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"


def write_to_file(movies):
    with open("movies.text", mode="w", encoding="utf-8") as file:
        file.write(movies)


response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

movies_header = soup.select("#__next main article div div div h3")

movie_list = []
for movie in movies_header:
    movie_list.insert(0, movie.text)

str_movies = '\n'.join(movie_list)
write_to_file(str_movies)

