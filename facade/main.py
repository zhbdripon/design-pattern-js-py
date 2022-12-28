class ProjectTeam:
    def communicate_with_client(self):
        print("communicating with client")

class DevTeam:

    def get_feature_requirement(self):
        print("getting feature requirements")

    def implement_feature(self):
        print("implementing new feature")

    def bugfix(self):
        print("fixing new reported bug")

    def deploy(self):
        print("deploying")


class QATeam:

    def test_feature(self):
        print("testing features")

    def report_bug(self):
        print("reporting found issues")

# this class act as facade
class EnosisSolution:

    def __init__(self) -> None:
        self.project_team = ProjectTeam()
        self.dev_team = DevTeam()
        self.qa_team = QATeam()

    def sell_service(self):
        self.project_team.communicate_with_client()
        self.dev_team.get_feature_requirement()
        self.dev_team.implement_feature()
        self.qa_team.test_feature()
        self.qa_team.report_bug()
        self.dev_team.bugfix()
        self.qa_team.test_feature()
        self.dev_team.deploy()

if __name__ == "__main__":
    enosis = EnosisSolution()
    enosis.sell_service()

"""
output:

communicating with client
getting feature requirements  
implementing new feature      
testing features
reporting found issues        
fixing new reported bug       
testing features
deploying
"""


