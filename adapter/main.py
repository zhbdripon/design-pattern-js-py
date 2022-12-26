class Dev:
    def __init__(self, name) -> None:
        self.name = name

    def develop_feature(self):
        return "developing new feature"

class QA:
    def __init__(self, name) -> None:
        self.name = name

    def test_feature(self):
        return "testing developed features"

class Lead:
    def __init__(self, name) -> None:
        self.name = name

    def manage_team(self):
        return "managing the assigned team"

class Adapter:
    def __init__(self, obj, **adapted_methods) -> None:
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

if __name__ == "__main__":

    ziaul = Dev("Ziaul")
    ezaz = QA("Ezaz")
    sajjad = Lead("Sajjad")

    team_members = []

    team_members.append(Adapter(ziaul, responsibility=ziaul.develop_feature))
    team_members.append(Adapter(ezaz, responsibility=ezaz.test_feature))
    team_members.append(Adapter(sajjad, responsibility=sajjad.manage_team))

    for team_member in team_members:
        print(f"{team_member.name}'s responsibility is {team_member.responsibility()}")
    
"""
output:
Ziaul's responsibility is developing new feature
Ezaz's responsibility is testing developed features
Sajjad's responsibility is managing the assigned team
"""