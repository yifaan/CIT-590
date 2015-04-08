bestActress = {1995: 'Susan Sarandon',
               1996: 'Frances McDormand', 123: 'asdasdgasdhiuqye7qwoy'}

print bestActress[reduce(lambda x, y: x if len(
    bestActress[x]) > len(bestActress[y]) else y, bestActress)]
