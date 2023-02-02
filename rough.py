class Team:
    def __init__(self, name, avat):
        self.name = name
        self.avat = avat


class Fixture:
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
        self.score = []

    def __str__(self):
        return f"{self.t1.avat} v {self.t2.avat}"

    def fixture_stadium(self):
        return f"{self.t1.avat} at home"



man = Team("Manchester", "MUN")
ars = Team("Arsenal", "ARS")
f = Fixture(man, ars)
print(f)
print(f.fixture_stadium())