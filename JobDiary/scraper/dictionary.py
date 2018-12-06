def check_grade(html):
    combinations = ["1st", "First class", "1st class", "Upper second class", "2:1", "2:2"]

    for classification in combinations:
        if classification.lower() in html.replace("first class results.", ""):
            return classification



