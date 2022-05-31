medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

def createMedalTable(results):
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point

    # Create empty medal table
    medalTable = {}

    # Loop through array of event result dictionaries
    for eventResult in results:
        # For each result, loop through its podium result
        for podiumPos in eventResult["podium"]:
            # extract the country from the string
            country = podiumPos[2:]
            # extract the position from the string
            position = int(podiumPos[0:1])
            # calculate the points
            points = 4 - position

            # if the country doesn't exist in the dictionary, add it with a default value one
            medalTable.setdefault(country, 0)
            # increment the points for the current country
            medalTable[country] += points

    return medalTable


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable
