from fuzzywuzzy import fuzz


def spelling_check(names_list, name):
    matches_names_list = []

    for name_from_list in names_list:
        score_test_result = fuzz.ratio(name_from_list.lower(), name.lower())
        if score_test_result == 100:
            return [name_from_list]
        elif score_test_result > 81:
            matches_names_list.append(name_from_list)

    return matches_names_list
