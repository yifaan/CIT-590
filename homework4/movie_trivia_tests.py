from movie_trivia import *
import unittest


class TestMovies(unittest.TestCase):

    movieDb = {}
    ratingDb = {}

    def setUp(self):
        self.movieDb = create_actors_DB('my_test_movies.txt')
        self.ratingDb = create_ratings_DB('my_moviescores.csv')

    # write unit tests for every function.
    def test_insert_actor_info(self):
        insert_actor_info('yifan', ['what'], self.movieDb)
        self.assertEqual(set(['what']), self.movieDb['yifan'])
        insert_actor_info('yifan', ['when'], self.movieDb)
        self.assertEqual(set(['what', 'when']), self.movieDb['yifan'])

    def test_insert_rating(self):
        insert_rating('what', (100, 99), self.ratingDb)
        self.assertEqual(set([100, 99]), self.ratingDb['what'])
        insert_rating('what', (1, 92), self.ratingDb)
        self.assertEqual(set([92, 1]), self.ratingDb['what'])

    def test_delete_movie(self):
        delete_movie('Movie 1', self.movieDb, self.ratingDb)
        self.assertEqual(self.ratingDb.get('Movie 1', 'none'), 'none')

        self.assertEqual(
            self.movieDb['Yyf'].difference('Movie 1'), self.movieDb['Yyf'])

    def testselect_where_actor_is(self):
        lst = set(select_where_actor_is('Hehe Zhang', self.movieDb))
        self.assertEqual(lst, set(['Movie 4']))
        lst = set(select_where_actor_is('HeHe Zhang', self.movieDb))
        self.assertEqual(lst, set([]))

    def testselect_where_the_movie_is(self):
        lst = select_where_movie_is('Movie 2', self.movieDb)
        self.assertEqual(set(lst), set(['Yang', 'Yyf']))

    def testselect_where_rating_is(self):
        lst = select_where_rating_is(3, '=', True, self.ratingDb)
        self.assertEqual(set(lst), set(['Movie 2']))

        lst = select_where_rating_is(3, '>', False, self.ratingDb)
        self.assertEqual(
            set(lst), set(['Movie 2', 'Movie 3', 'Movie 4', 'What']))

    def testget_co_actors(self):
        lst = get_co_actors('Hehe Zhang', self.movieDb)
        self.assertEqual(lst, ['Yang'])

    def testget_common_movie(self):
        movie = get_common_movie('Yyf', 'Hehe Zhang', self.movieDb)
        self.assertEqual([], movie)
        movie = get_common_movie('Yang', 'Hehe Zhang', self.movieDb)
        self.assertEqual(['Movie 4'], movie)

    def testcritics_darling(self):
        lst = critics_darling(self.movieDb, self.ratingDb)
        self.assertEqual(set(lst), set(['Hehe Zhang']))

    def testaudience_darling(self):
        lst = audience_darling(self.movieDb, self.ratingDb)
        self.assertEqual(set(lst), set(['Hehe Zhang']))

    def testgood_movies(self):
        lst = good_movies(self.ratingDb)
        self.assertEqual(lst, set(['What']))

    def testget_common_actors(self):
        lst = get_common_actors('Movie 2', 'Movie 3', self.movieDb)
        self.assertEqual(set(lst), set(['Yyf', 'Yang']))

    def testfind_corresponding_actor(self):
        lst = find_corresponding_actor('yang', self.movieDb)
        self.assertEqual(lst, 'Yang')
        lst = find_corresponding_actor('WHAT', self.movieDb)
        self.assertEqual(lst, 'WHAT')

    def testfind_corresponding_movie(self):
        lst = find_corresponding_movie('movie 1', self.ratingDb)
        self.assertEqual(lst, 'Movie 1')
        lst = find_corresponding_movie('movie 6', self.ratingDb)
        self.assertEqual(lst, 'movie 6')


unittest.main()
