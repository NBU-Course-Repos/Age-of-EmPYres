import os
import pickle
from datetime import datetime
from pprint import pprint


class SaveSystem:

    _saves_base_path = "{os.getcwd()}/Data/Saves/"
    _save_dir = ""
    _objects_to_save = []

    @staticmethod
    def _time_stamp():
        ts = datetime.now()
        return f"{ts.day}-{ts.month}-{ts.year}-{ts.hour}-{ts.minute}"

    @staticmethod
    def _correct_path():
        cwd = os.getcwd()
        SaveSystem._save_dir = f"{cwd}/{SaveSystem._save_dir}"
        if "\\" in cwd:
            SaveSystem._save_dir = SaveSystem._save_dir.replace("/", "\\")

    @staticmethod
    def create_save_dir():
        next_save = len(os.listdir(SaveSystem._saves_base_path)) + 1
        SaveSystem._save_dir = fr"{SaveSystem._saves_base_path}save{next_save}-{SaveSystem._time_stamp()}"
        SaveSystem._correct_path()
        os.mkdir(SaveSystem._save_dir)

    @staticmethod
    def to_be_saved(obj_name, obj_data):
        if {obj_name: obj_data} not in SaveSystem._objects_to_save:
            print(f"adding {obj_name}")
            SaveSystem._objects_to_save.append({obj_name: obj_data})

    @staticmethod
    def save_game():
        for obj in SaveSystem._objects_to_save:
            key = (list(obj.keys()))[0]
            # print(f"saving: {key}")
            with open(fr"{SaveSystem._save_dir}\\{key}.save", "wb") as file:
                print(type(obj[key].__dict__))
                pprint(obj[key].__dict__)
                pickle.dump(obj[key], file)

    @staticmethod
    def load_game():
        # TODO load_game method
        return
