import json
import os
from .base import TaskManagerBase

class TaskManager(TaskManagerBase):
    def __init__(self):
        self.db_path = 'db/tasks.json'
        self._load_data()

        def _load_data(self):
            if not os.path.exists(self.db_path):
                self.tasks = {}
                self._save_data()
            else:
                with open(self.db_path, 'r') as f:
                    self.tasks = json.load(f)

                    def _save_data(self):
                        with open(self.db_path, 'w') as f:
                            json.dump(self.tasks, f, indent=4)

                            def create_task(self, task_json: str) -> str:
                                task = json.loads(task_json)
                                task_id = task.get('id')
                                if task_id in self.tasks:
                                    raise ValueError("Task ID already exists")
                                self.tasks[task_id] = task
                                self._save_data()
                                return json.dumps({"status": "success", "task": task}, indent=4)
                            
                            def delete_task(seld, task_id: str) -> str:
                                if task_id not in self.tasks:
                                    raise ValueError("Task ID does not exist")
                                del self.tasks[task_id]
                                self._save_data()
                                return json.dumps({"status": "success"}, indent=4)
                            
                            def list_tasks(self) -> str:
                                return json.dumps(self.tasks, indent=4)
                            
