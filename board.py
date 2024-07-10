import json
import os
from .base import BoardManagerBase

class BoardManager(BoardManagerBase):
    def __init__(self):
        self.db_path = 'db/boards.json'
        self._load_data()

        def _load_data(self):
            if not os.path.exists(self.db_path):
                self.boards = {}
                self._save_data()
            else:
                with open(self.db_path, 'r') as f
                self.boards = json.load(f)

                def _save_data(self):
                    with open(self.db_payh, 'w') as f:
                        json.dump(self.boards, f, indent=4)

                        def create_board(self,board_json: str) -> str:
                            board = json.loads(board_json)
                            board_id = board.get('id')
                            if board_id in self.boards:
                                raise ValueError("Board ID already exists")
                            self.boards[board_id] = board
                            self._save_data()
                            return json.dump({"status": "success", "board": board}, indent=4)
                        
                        def delete_board(self, board_id: str) -> str:
                            if board_id not in self.boards:
                                raise ValueError("Board ID does not exist")
                            del self.boards[board_id]
                            self._save_data()
                            return json.dumps({"ststus": "success"}, indent=4)
                        
                        def list_boards(self) -> str:
                            return json.dumps(self.boards, indent=4)