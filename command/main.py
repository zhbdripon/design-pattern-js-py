from abc import ABC, abstractmethod

class Command(ABC):
	
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass

class SimpleCommand(Command):

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.perform_task()

class Receiver:
	
    def perform_task(self):
        print('Executed in receiver.')

class Invoker:
	
    def command(self, cmd):
        self.cmd = cmd

    def execute_command(self):
        self.cmd.execute()

if __name__ == "__main__":
	
    receiver = Receiver()
    cmd = SimpleCommand(receiver)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute_command()
