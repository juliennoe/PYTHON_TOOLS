import os
import json
import logging

chemin_dossier = os.path.dirname(__file__)
chemin_json = os.path.join(chemin_dossier, "data", "movies.json")
print(chemin_json)

def get_movies():
    with open(chemin_json, "r") as f:
        movies_title = json.load(f)
        
    return(movies_title)

class Movie :
    def __init__(self,title):
        self.title = title.title()

    def __str__(self):
        return self.title

    def _load_movies(self):
        with open(chemin_json, "r") as f:
         return json.load(f)

    def _write_movies(self, movies):
        with open (chemin_json, "w") as f:
            json.dump(movies, f)
    
    def _add_movies(self):
        movies = self._load_movies()
     
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f'le film{self.title} est deja enregistrer')
            return False
    
    def _remove_movies(self):
        movies = self._load_movies()
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
        else:
            logging.warning(f'le film {self.title} est pas deja enregistrer')


print('tout est bon')
