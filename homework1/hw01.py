def print_intro():
    print('''Congrats, you are the newest ruler of ancient Samaria, elected for a ten year term
of office. Your duties are to distribute food, direct farming, and buy and sell land
as needed to support your people. Watch out for rat infestations and the resultant
plague! Grain is the general currency, measured in bushels. The following will help
you in your decisions:
	* Each person needs at least 20 bushels of grain per year to survive.
	* Each person can farm at most 10 acres of land.
	* It takes 2 bushels of grain to farm an acre of land.
	* The market price for land fluctuates yearly.
Rule wisely and you will be showered with appreciation at the end of your term. Rule
poorly and you will be kicked out of office!''')


def Hammutabi():
	starved = 0
    immigrants = 5
	population = 100
    harvest = 3000
    bushels_per_acre = 3
    rats_ate = 200
    bushels_in_storage = 2800
    acres_owned = 1000
    cost_per_acre = 19      # each acre costs this many bushels
    plague_deaths = 0
    print_intro()
