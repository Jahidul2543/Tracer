def count_odds_and_evens(number_list):
    # number_list = [1, 2, 3, 4, 5]
    ODDS, EVENS = 0, 0
    for num in number_list:
        if num % 2 == 0:
            EVENS += 1

        else:
            ODDS += 1

    # print("Even numbers in the list: ", EVENS)
    # print("Odd numbers in the list: ", ODDS)
    odds_even_dictionary = {
        "EVENS": EVENS,
        "ODDS": ODDS
    }
    for (key, value) in odds_even_dictionary.items():
        print(key, " :: ", value)
    # for value in odds_even_dictionary :
    #     print(value)
    return odds_even_dictionary