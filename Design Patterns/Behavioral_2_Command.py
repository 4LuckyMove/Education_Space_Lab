from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def unexecute(self):
        pass


class Squad:
    def move(self, direction):
        print(f'Отряд движеться в направлении {direction}')

    def stop(self):
        print('Отряд остановился')


class ForwardCommand(Command):
    def __init__(self, squad: Squad):
        self.squad = squad

    def execute(self):
        self.squad.move('вперед')

    def unexecute(self):
        self.squad.stop()


class RetreatCommand(Command):
    def __init__(self, squad: Squad):
        self.squad = squad

    def execute(self):
        self.squad.move('назад')

    def unexecute(self):
        self.squad.stop()


class SquadInvoker:
    def __init__(self, forward: ForwardCommand, retreat: RetreatCommand):
        self.forward_command = forward
        self.retreat_command = retreat
        self.current_command = None

    def forward(self):
        self.current_command = self.forward_command
        self.forward_command.execute()

    def retreat(self):
        self.current_command = self.retreat_command
        self.retreat_command.execute()

    def stop(self):
        if self.current_command:
            self.current_command.unexecute()
            self.current_command = None
        else:
            print(f'Отряд не может остановиться, так как выполняет команду {self.current_command}')


if __name__ == '__main__':
    squad = Squad()
    interface = SquadInvoker(ForwardCommand(squad), RetreatCommand(squad))
    interface.forward()
    interface.stop()
    interface.retreat()
    interface.stop()