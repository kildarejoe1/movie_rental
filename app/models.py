import app
from sqlalchemy import Column, Integer, Boolean, Float
#Database Models
class Movie(app.db.Model):
    __tablename__ = "movie"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    genre=Column(String)
    watched=Column(Boolean)


    def __init__(self,name, genre, watched=False):
        self.name=name
        self.genre=genre
        self.watched = watched

    def __repr__(self):
        pass


class User(db.Model):
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
        self.movies=[]

    __tablename__ = "user"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)
    password=Column(Boolean)

    def add_movie(self, name,genre): #my user object calling this method
        new_movie=Movie(name,genre,False)
        self.movies.append(new_movie)

    def delete_movie(self,name):
        print(self.movies)
        self.movies.remove(name)
        print(self.movies)


    def __repr__(self):
        return "User %s" % self.movies
