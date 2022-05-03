import random
from urllib import response
import requests #pip3 install requests
from bs4 import BeautifulSoup #pip3 install bs4 

url  = 'https://www.imdb.com/chart/boxoffice'


def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select('td.titleColumn')
    #scrape all of this element from the whole website
    inner_movietags = soup.select('td.titleColumn a')

    rating_tags = soup.select('td.ratingColumn span[class=secondaryInfo]')
    

    def get_title(movie_tag):
        #moviesplit = innermovietags0.text.split()
        moviesplit = movie_tag.text.split()
        title = moviesplit[-1]
        return title

    title = [get_title(tag) for tag in movietags]
    actors_list = [tag['title'] for tag in inner_movietags]
    
    #ratings = ('span.sim-posted span:last-child')
    #ratings = [tag['secondaryInfo'] for tag in rating_tags]
    
    #print random movie 
    n_movies = len(title)
    print(n_movies)
    while(True):
        idx = random.randrange(0, n_movies)

        print(f'{title[idx]} starring: {actors_list[idx]}')
        user_input = input('do you want a different movie to watch (y/n)?')
        if user_input != 'y':
            break



    


if __name__ == '__main__':
    main()