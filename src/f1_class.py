import requests
import json
from f1_class_lib import *


def main():
    while True:
        try:
            year_amount = int(input("Please input a year: "))
            if 1952 <= year_amount and year_amount <= 2023:
                break
            else:
                raise ValueError

        except ValueError:
            print("This is not valid")
            continue

    http_str = f"http://ergast.com/api/f1/{year_amount}.json"

    race_dict = get_url(http_str)

    season = Season()

    for race_info in race_dict["MRData"]["RaceTable"]["Races"]:
        race = Race(race_info)
        season.add_race(race)

    for race in season.races:
        print(race.round, end=" ")
        print(race.race_name, end=" ")
        print(race.locality)

    max_rounds = season.get_max_rounds()
    while True:
        round_request = input(f"Please enter the round number that you would like to see the results from Rounds 1 to Rounds {max_rounds}: ")
        if 1 <= int(round_request) <= max_rounds:
            break
        print("This round is invalid! Please try again!")
        
    http_str = f" http://ergast.com/api/f1/{year_amount}/{round_request}/results/.json"
    race_dict_results = get_url(http_str)

    results = Results()

    for positions in race_dict_results["MRData"]["RaceTable"]["Races"][0]["Results"]:
        driver = Position(positions)
        results.add_position(driver)

    for driver in results.positions:
        print(driver.position, end=" ")
        print(driver.given_name, end=" ")
        print(driver.family_name, end=" ")
        print(driver.nationality, end=" ")
        print(driver.constructor)


def get_url(http_str):
    try:
        new_response = requests.get(http_str)
        new_response.raise_for_status()
        result_dict = new_response.json()
    except requests.RequestException:
        print("This is invalid")
    return result_dict


if __name__ == "__main__":
    main()
