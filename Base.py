from abc import ABC, abstractmethod

class TeamManagerBase(ABC):
    @abstractmethod
    def create_team(self, team_json: str) -> str:
        pass

    @abstractmethod
    def delete_team(self, team_id: str) -> str:
        pass

    @abstractmethod
    def list_teams(self,board_json: str) ->str:
        pass

    class BoardManagerBase(ABC):
        @abstractmethod
        def create_board(self, board_json: str) -> str:
            pass

        @abstractmethod
        def delete_board(self, board_id: str) -> str:
            pass

        @abstractmethod
        def list_boards(self) -> str:
            pass


        class TaskManagerBase(ABC):
            @abstractmethod
            def create_task(self, task_json: str) -> str:
                pass

            @abstractmethod
            def delete_task(self, task_id: str) -> str:
                pass

            @abstractmethod
            def list_tasks(self) -> str:
                pass
        
      