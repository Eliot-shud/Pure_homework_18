from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO

from service.movie import MovieService
from service.director import DirectorService
from service.genre import GenreService

from setup_db import db

# Экземпляр DAO и схема для вьюшек Genre, Director и Movie
genre_dao = GenreDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)

# Экземпляр DAO, сервиса и схемы для вьюшек
director_service = DirectorService(dao=director_dao)
movie_service = MovieService(dao=movie_dao)
genre_service = GenreService(dao=genre_dao)