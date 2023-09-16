import json
import random
from core.ezh_action import EzhAction
from core.ezh_except import EzhException


class EzhDoActions():
    def get_answer(action: EzhAction):
        if action.act_id == 'recommend':
            return EzhDoActions.__recommend(action)

    def __recommend(action: EzhAction) -> str:
        try:
            with open(f'files/{action.ext}.json') as rec_objects:
                objects = json.load(rec_objects)
            recommendation = objects[action.ext][
                random.randint(0, len(objects[action.ext]) - 1)
                ]
        except FileNotFoundError:
            raise EzhException("Опа... Что-то пошло не так :(")
        return action.answer.replace("{}", recommendation)
