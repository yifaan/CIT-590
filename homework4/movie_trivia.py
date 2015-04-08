import csv


def create_actors_DB(actor_file):
    '''Create a dictionary keyed on actors from a text file'''
    f = open(actor_file)
    movieInfo = {}
    for line in f:
        line = line.rstrip().lstrip()
        actorAndMovies = line.split(',')
        actor = actorAndMovies[0]
        movies = [x.lstrip().rstrip() for x in actorAndMovies[1:]]
        movieInfo[actor] = set(movies)
    f.close()
    return movieInfo


def create_ratings_DB(ratings_file):
    '''make a dictionary from the rotten tomatoes csv file'''
    scores_dict = {}
    with open(ratings_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            scores_dict[row[0]] = [row[1], row[2]]
    return scores_dict


def insert_actor_info(actor, movies, movie_Db):
    '''Update movie database'''
    lst = movie_Db.get(actor, 'none')
    if lst == 'none':
        movie_Db[actor] = set(movies)
    else:
        movie_Db[actor] = movie_Db[actor].union(movies)


def insert_rating(movie, ratings, ratings_Db):
    '''Update rating database'''
    ratings_Db[movie] = set(ratings)


def delete_movie(movie, movie_Db, ratings_Db):
    '''delete all information from the database that corresponds\
     to this movie.'''
    del ratings_Db[movie]

    for x in movie_Db:
        movie_Db[x] = movie_Db[x].difference([movie])


def select_where_actor_is(actorName, movie_Db):
    '''given an actor, return the list of all movies. '''
    if actorName in movie_Db.keys():
        return list(movie_Db[actorName])
    else:
        return []


def select_where_movie_is(movieName, movie_Db):
    '''given a movie, return the list of all actors'''
    lst = []

    for x in movie_Db:
        if movieName in movie_Db[x]:
            lst.append(x)
    return lst


def select_where_rating_is(targeted_rating, comparison, is_critic, ratings_Db):
    '''Find movie satisfied the rating requirement'''
    lst = []
    if is_critic:
        index = 0
    else:
        index = 1

    if comparison == '=':
        for movie in ratings_Db:
            if int(list(ratings_Db[movie])[index]) == int(str(
                    targeted_rating)):
                lst.append(movie)
    elif comparison == '>':
        for movie in ratings_Db:
            if int(list(ratings_Db[movie])[index]) > int(str(targeted_rating)):
                lst.append(movie)
    elif comparison == '<':
        for movie in ratings_Db:
            if int(list(ratings_Db[movie])[index]) < int(str(targeted_rating)):
                lst.append(movie)
    return lst


def get_co_actors(actorName, movie_Db):
    '''returns list of\
    all actors that the actor has ever worked with in any movie.'''
    lst = select_where_actor_is(actorName, movie_Db)
    actor = set([])
    for movie in lst:
        actor = actor.union(select_where_movie_is(movie, movie_Db))

    actor.remove(actorName)
    return list(actor)


def get_common_movie(actor1, actor2, moviedb):
    '''goes through the database and returns the movies where both actors \
    were cast.'''
    lst1 = set(select_where_actor_is(actor1, moviedb))
    lst2 = set(select_where_actor_is(actor2, moviedb))
    movie = lst1.intersection(lst2)
    if movie == set([]):
        return []
    else:
        return list(movie)


def critics_darling(movie_Db, ratings_Db):
    '''given the two dictionaries, we are interested in finding the actor \
    whose movies have the highest average rotten tomatoes rating, \
    as per the critics.'''
    total_score = 0
    best_actor = []
    for actor in movie_Db:
        count = 0
        number_of_movie = 0
        for movie in movie_Db[actor]:
            if movie in ratings_Db.keys():
                count += int(list(ratings_Db[movie])[0])
                number_of_movie += 1.0
        if number_of_movie != 0:
            if count / number_of_movie > total_score:
                best_actor = [actor]
                total_score = count / number_of_movie
            elif count / number_of_movie == total_score:
                best_actor.append(actor)
    return best_actor


def audience_darling(movie_Db, ratings_Db):
    '''given the two dictionaries, we are interested in finding the actor \
    whose movies have the highest average rotten tomatoes rating, as per \
    the audience.'''
    total_score = 0
    best_actor = []
    for actor in movie_Db:
        count = 0
        number_of_movie = 0
        for movie in movie_Db[actor]:
            if movie in ratings_Db.keys():
                count += int(list(ratings_Db[movie])[1])
                number_of_movie += 1.0
        if number_of_movie != 0:
            if count / number_of_movie > total_score:
                best_actor = [actor]
                total_score = count / number_of_movie
            elif count / number_of_movie == total_score:
                best_actor.append(actor)
    return best_actor


def good_movies(ratings_Db):
    '''this function returns the set of movies that both critics and \
    the audience have rated above 85 '''
    lst1 = set(select_where_rating_is(85, '>', True, ratings_Db))
    lst2 = set(select_where_rating_is(85, '>', False, ratings_Db))
    lst3 = set(select_where_rating_is(85, '=', True, ratings_Db))
    lst4 = set(select_where_rating_is(85, '=', False, ratings_Db))
    lst5 = lst1.union(lst3)
    lst6 = lst2.union(lst4)
    return lst5.intersection(lst6)


def get_common_actors(movie1, movie2, movies_Db):
    '''Given a pair of movies, return a list of actors that acted in both.'''
    lst1 = set(select_where_movie_is(movie1, movies_Db))
    lst2 = set(select_where_movie_is(movie2, movies_Db))
    lst = lst1.intersection(lst2)
    return list(lst)


def find_corresponding_actor(actor, movies_Db):
    '''find corresponds actor from user input, if can not find, return the\
     input one'''
    for person in movies_Db:
        if person.lower() == actor.lower().lstrip().rstrip():
            return person
    return actor.lstrip().rstrip()


def find_corresponding_movie(movie, ratings_Db):
    '''find corresponds movie from user input, if can not find, return the\
     input one'''
    for movieName in ratings_Db:
        if movieName.lower() == movie.lower().lstrip().rstrip():
            return movieName
    return movie.lstrip().rstrip()


def main():
    actor_DB = create_actors_DB('movies.txt')
    ratings_DB = create_ratings_DB('moviescores.csv')
    # PLEASE TAKE THE NEXT FEW PRINTING LINES OUT
    # ONCE YOU HAVE CONFIRMED THIS WORKS
    print 'Welcome to the Movie Database!!\
You can do lots of magical things here!!\n'
    print 'input 1 to see all movies an actor ever filmed\n\
input 2 to see all the actor of a movie\n\
input 3 to search movies based on rating\n\
input 4 to find all co-actors of an actor ever have\n\
input 5 to search movies where two actors were cast\n\
input 6 to see actors critics love most\n\
input 7 to see actors audience love most\n\
input 8 to find movies have average rating larger than 85\n\
input 9 to find common actors in two movies\n\
input 0 to exit'

    choice = []

    while choice != '0':
        choice = raw_input(
            'made your choice, integer only\t').rstrip().lstrip()
        while (choice != '0' and choice != '1' and choice != '2' and
                choice != '3' and choice != '4'and choice != '5' and
                choice != '6' and choice != '7' and choice != '8' and
                choice != '9'):
            choice = raw_input(
                'made your choice, integer only\t').rstrip().lstrip()

        if choice == '1':
            people = find_corresponding_actor(raw_input('which actor?\t'),
                                              actor_DB)
            movie_acted = select_where_actor_is(people, actor_DB)
            if movie_acted == []:
                print 'not present\t'
            else:
                print 'The movie', people, 'acted are', movie_acted

        elif choice == '2':
            movie = find_corresponding_movie(raw_input('which movie?\t'),
                                             ratings_DB)
            people_acted = select_where_movie_is(movie, actor_DB)
            if people_acted == []:
                print 'not present\t'
            else:
                print 'The actors acted in', movie, 'are', people_acted

        elif choice == '3':
            critics = []
            rating = []
            compare_input = []
            while critics != 'y' and critics != 'n':
                critics = raw_input(
                    'input y search critics rating,n search audience rating\t')
            if critics == 'n':
                critics = False
            else:
                critics = True
            rating = input(
                'choose the rating you want to compare with\t')
            while (compare_input != '>' and compare_input != '=' and
                   compare_input != '<'):
                compare_input = raw_input('input > find movies larger than the rating,\
< find movies smaller than the rating\
= find movies equal to the rating\t')
            movies = select_where_rating_is(
                rating, compare_input, critics, ratings_DB)
            print 'movies with rating', compare_input, rating, 'are', movies

        elif choice == '4':
            people = find_corresponding_actor(raw_input('which actor?\t'),
                                              actor_DB)
            co_actors = get_co_actors(people, actor_DB)
            print 'co_actors of', people, 'are', co_actors

        elif choice == '5':
            movies = []
            people1 = find_corresponding_actor(raw_input('first actor?\t'),
                                               actor_DB)
            if select_where_actor_is(people1, actor_DB) == []:
                print people1, 'not presented'
            else:
                people2 = find_corresponding_actor(raw_input('second actor?'),
                                                   actor_DB)
                if select_where_actor_is(people2, actor_DB) == []:
                    print people2, 'not presented'
                else:
                    movies = get_common_movie(people1, people2, actor_DB)
                    if movies == []:
                        print 'They never act together!'
                    else:
                        print 'The movies', people1, 'and',\
                               people2, 'cooperated are', movies

        elif choice == '6':
            actors = critics_darling(actor_DB, ratings_DB)
            print 'The actors critics love most is', actors

        elif choice == '7':
            actors = audience_darling(actor_DB, ratings_DB)
            print 'The actors audience love most is', actors

        elif choice == '8':
            movies = list(good_movies(ratings_DB))
            print 'Good movies that audience and critics love are', movies

        elif choice == '9':
            actors = []
            movie1 = find_corresponding_movie(raw_input('first movie?\t'),
                                              ratings_DB)
            if select_where_movie_is(movie1, actor_DB) == []:
                print 'movie1 not present'
            else:
                movie2 = find_corresponding_movie(raw_input('second movie?\t'),
                                                  ratings_DB)
                if select_where_movie_is(movie2, actor_DB) == []:
                    print 'movie2 not present'
                else:
                    actors = get_common_actors(movie1, movie2, actor_DB)
                    if actors == []:
                        print 'no common actors'
                    else:
                        print 'common actors are', actors


if __name__ == '__main__':
    main()
