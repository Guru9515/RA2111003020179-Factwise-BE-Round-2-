import json
import os
from .base import TeamManagerBase

class TeamManager(TeamManagerBase):
    def __init__(self):
        self.db_path = 'db/teams.json'
        self._load_data()

    def _load_data(self): 
          if not os.path.exists(self.db_path):
            self.teams = {}
            self._save_data()
            else:
            with open(self.db_path, 'r') as f:
                 self.teams = json.load(f)
                 def _save_data(self):
                        with open(self.db_path, 'w') as f:
                               json.dump(self.teams, f, indent=4)
                               def create_team(self, team_json: str) -> str:
                                      team_json = json.loads(team_json)
                                      team_id = team.get('id')
                                      if team_id in self.teams:
                                           raise ValueError("Team ID already exists")
                                      self.teams[team_id] = team
                                      self._save_data()
                                      return json.dumps({"status": "success"}, indent=4)
                               
                               def list_teams(self) -> str:
                                    return json.dumps(self.teams, indent=4)