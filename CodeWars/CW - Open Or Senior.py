"""To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
Input

Input will consist of a list of lists containing two items each. Each list contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

Note for F#: The input will be of (int list list) which is a List<List>"""


def open_or_senior(data):
    results = []

    for x in data:
        if x[0] >= 55 and x[1] > 7:
            results.append("Senior")
        else:
            results.append("Open")
    return (results)

