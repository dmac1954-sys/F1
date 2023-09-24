class Season:
    def __init__(self):
        self.races = []

    def add_race(self, race):
        self.races.append(race)

    def get_races(self):
        return self.races

    def sort_races(self):
        self.races.sort(key=lambda x: x.get_round())

    def get_max_rounds(self):
        return len(self.races)


class Race:
    def __init__(self, race_info):
        self.race_name = race_info["raceName"]
        self.round = race_info["round"]
        self.locality = race_info["Circuit"]["Location"]["locality"]

    def get_race_name(self):
        return self.race_name

    def get_round(self):
        return self.round

    def get_locality(self):
        return self.locality


class Results:
    def __init__(self):
        self.positions = []

    def add_position(self, position):
        self.positions.append(position)

    def get_positions(self):
        return self.positions

    def sort_positions(self):
        self.positions.sort(key=lambda pos: pos.get_position())


class Position:
    def __init__(self, positions):
        self.position = positions["position"]
        self.given_name = positions["Driver"]["givenName"]
        self.family_name = positions["Driver"]["familyName"]
        self.nationality = positions["Driver"]["nationality"]
        self.constructor = positions["Constructor"]["name"]

    def get_position(self):
        return self.position

    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    def get_nationality(self):
        return self.nationality

    def get_constructor(self):
        return self.constructor

if __name__ == "__main__":
    main()