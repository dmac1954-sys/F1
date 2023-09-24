import pytest

from src.f1_class_lib import Season, Race, Results, Position

def test_add_race():
    season = Season()
    race = Race({"raceName": "Race 1", "round": 1, "Circuit": {"Location": {"locality": "City 1"}}})
    season.add_race(race)
    assert len(season.get_races()) == 1
    assert season.get_races()[0].get_race_name() == "Race 1"

def test_sort_races():
    season = Season()
    race1 = Race({"raceName": "Race 1", "round": 1, "Circuit": {"Location": {"locality": "City 1"}}})
    race2 = Race({"raceName": "Race 2", "round": 2, "Circuit": {"Location": {"locality": "City 2"}}})
    race3 = Race({"raceName": "Race 3", "round": 3, "Circuit": {"Location": {"locality": "City 3"}}})
    season.add_race(race3)
    season.add_race(race1)
    season.add_race(race2)
    season.sort_races()
    assert [race.get_race_name() for race in season.get_races()] == ["Race 1", "Race 2", "Race 3"]

def test_add_position():
    results = Results()
    position = Position({"position": 1, "Driver": {"givenName": "John", "familyName": "Doe", "nationality": "USA"}, "Constructor": {"name": "Team A"}})
    results.add_position(position)
    assert len(results.get_positions()) == 1
    assert results.get_positions()[0].get_given_name() == "John"

def test_sort_positions():
    results = Results()
    position1 = Position({"position": 3, "Driver": {"givenName": "John", "familyName": "Doe", "nationality": "USA"}, "Constructor": {"name": "Team A"}})
    position2 = Position({"position": 1, "Driver": {"givenName": "Alice", "familyName": "Smith", "nationality": "UK"}, "Constructor": {"name": "Team B"}})
    position3 = Position({"position": 2, "Driver": {"givenName": "Bob", "familyName": "Johnson", "nationality": "Canada"}, "Constructor": {"name": "Team C"}})
    results.add_position(position3)
    results.add_position(position1)
    results.add_position(position2)
    results.sort_positions()
    assert [pos.get_given_name() for pos in results.get_positions()] == ["Alice", "Bob", "John"]