import random


def print_intro():
    print '''   Congrats, you are the newest ruler of ancient Samaria, elected for a ten year term
    of office. Your duties are to distribute food, direct farming, and buy and sell land
    as needed to support your people. Watch out for rat infestations and the resultant
    plague! Grain is the general currency, measured in bushels. The following will help
    you in your decisions:
        * Each person needs at least 20 bushels of grain per year to survive.
        * Each person can farm at most 10 acres of land.
        * It takes 2 bushels of grain to farm an acre of land.
        * The market price for land fluctuates yearly.
    Rule wisely and you will be showered with appreciation at the end of your term. Rule
    poorly and you will be kicked out of office!\n'''


def ask_to_buy_land(bushels, cost):
    acres = input("How many acres will you buy?")
    while acres * cost > bushels:
        print "O great Hammurabi, we have but", bushels, "bushels of grain!"
        acres = input("How many acres will you buy? ")
    return acres


def ask_to_sell_land(acres):
    acres_to_sell = input("How many acres will you sell? ")
    while acres_to_sell > acres:
        print "O great Hammurabi, we have but", acres, "of acres!"
        acres_to_sell = input("How many acres will you sell? ")
    return acres_to_sell


def ask_to_feed(bushels):
    bushels_to_feed = input(
        "How many bushels will you want to use for feeding? ")
    while bushels_to_feed > bushels:
        print "O great Hammurabi, we have but", bushels, "of bushels!"
        bushels_to_feed = input(
            "How many bushels will you want to use for feeding? ")
    return bushels_to_feed


def ask_to_cultivate(acres, population, bushels):
    land_to_plant = input("how much land they want to plant seed in?\n")
    while land_to_plant > acres or land_to_plant / 10.0 > population or land_to_plant * 2 > bushels:
        print "O great Hammurabi, we have but", bushels, "of bushels,", acres, "of lands and", population, "of people!"
        land_to_plant = input("how much land they want to plant seed in?\n")
    return land_to_plant


def isPlague():
    rand = random.randint(0, 100)
    if rand <= 15:
        return True
    else:
        return False


def numStarving(population, bushels):
    num_starved = population-bushels / 20

    if num_starved < 0:
        num_starved = 0
    return num_starved


def numImmigrants(land, grainInStorage, population, numStarving):
    if numStarving > 0:
        return 0
    else:
        num_of_immigrants = (
            20 * land + grainInStorage) / ((100 * population) + 1)

        return num_of_immigrants


def getHarvest():
    return random.randint(1, 8)


def doRatsInfest():
    if random.randint(1, 100) > 40:
        return 0
    else:
        return random.randint(10, 30) / 100.0


def priceOFLand():
    return random.randint(16, 22)


def Hammutabi():
    starved = 0
    immigrants = 5
    population = 100
    harvest = 3000      # totol bushels harvested
    bushels_per_acre = 3  # amount harvested for each acre planted
    rats_ate = 200
    bushels_in_storage = 2800
    acres_owned = 1000
    cost_per_acre = 19      # each acre costs this many bushels
    plague_deaths = 0

    print_intro()

    for year in range(1, 11):
        print '''       O great Hammurabi!
        You are in year''', year, '''of your ten year rule.
        In the previous year''', starved, '''people starved to death.
        In the previous year''', immigrants, '''people entered the kingdom.
        The population is now''', population, '''.
        We harvested''', harvest, '''bushels at''', bushels_per_acre, '''bushels per acre.
        Rats destroyed''', rats_ate, '''bushels, leaving''', bushels_in_storage, '''bushels in storage. 
        The city owns''', acres_owned, '''acres of land.
        Land is currently worth''', cost_per_acre, '''bushels_per_acre.
        There were''', plague_deaths, '''from the plague\n'''

        landbought = ask_to_buy_land(bushels_in_storage, cost_per_acre)

        if landbought > 0:
            acres_owned += landbought
            bushels_in_storage -= cost_per_acre * landbought
        else:
            landsell = ask_to_sell_land(acres_owned)
            acres_owned -= landsell
            bushels_in_storage += cost_per_acre * landsell

        num_feed = ask_to_feed(bushels_in_storage)

        bushels_in_storage -= num_feed

        num_cultivate = ask_to_cultivate(acres_owned,population,bushels_in_storage)

        bushels_in_storage -= num_cultivate*2

        if isPlague()==True:
            plague_deaths = population = population / 2


        starved = numStarving(population, num_feed)
        if starved*100 / population > 45:
            print "GAME OVER!! You are a terrible ruler!!",starved ,"people get starved because of you!!!"
            break

        population-=starved

        immigrants = numImmigrants(acres_owned, bushels_in_storage, population, starved)

        population += immigrants

        bushels_per_acre=getHarvest()
        rats_ate = int(num_cultivate * bushels_per_acre *  doRatsInfest())
        harvest = num_cultivate * bushels_per_acre - rats_ate

        bushels_in_storage += harvest

        cost_per_acre=priceOFLand();

    print "Congratulations, you have finished the game!" 
    print '''   In the previous year''', starved, '''people starved to death.
        In the previous year''', immigrants, '''people entered the kingdom.
        The population is now''', population, '''.
        We harvested''', harvest, '''bushels at''', bushels_per_acre, '''bushels per acre.
        Rats destroyed''', rats_ate, '''bushels, leaving''', bushels_in_storage, '''bushels in storage. 
        The city owns''', acres_owned, '''acres of land.
        Land is currently worth''', cost_per_acre, '''bushels_per_acre.
        There were''', plague_deaths, '''from the plague\n'''

    rate=acres_owned-starved*10
    if rate>5000:
        print "You are a great ruler!"
    elif rate>2000:
        print "You are a good ruler!"
    else:
        print "You are an bad ruler!"

if __name__=="__main__":
    Hammutabi()






