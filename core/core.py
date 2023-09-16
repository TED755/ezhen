import json
from core.ezhen_settings import EZHEN_TOKEN
from core.ezh_except import EzhException
from core.ezh_action import EzhAction
from core.ezh_do_actions import EzhDoActions


class EzhenCore():
    def __init__(self):
        self.token = EZHEN_TOKEN
        try:
            with open('core/ezhen_vocabluary.json', 'r') as vocabluary:
                self.vocabluary: dict = json.load(vocabluary)
            with open('core/ezhen_actions.json') as actions:
                self.actions: dict = json.load(actions)
        except FileNotFoundError as ex:
            raise EzhException(message=f'Не найден файл "{ex.filename}" '
                               'при оживлении Эженя')

    def is_me(self, first_word: str) -> bool:
        for my_name in self.vocabluary['me']:
            if my_name in first_word.lower():
                return True
        return False

    def def_action(self, messages: list) -> EzhAction:
        find_action = messages[0]
        action_id = ''
        # TODO: Убрать дублирующий код в отдельный метод
        for voc in self.vocabluary.keys():
            if find_action.lower() in self.vocabluary[voc]:
                action_id = voc
                break

        action = self.__form_action(action_id, messages[1:])
        return action

    def __form_action(self, action_id: str,
                      ext_comm_info: list = []) -> EzhAction:
        action_settings = self.actions.get(action_id)
        if not action_id:
            return EzhAction(action=None, answer='Я тебя не понял. Я пока могу'
                             ' не все, поэтому посмотри еще раз, что я могу и '
                             'обратись еще раз')

        if action_settings['need_ext']:
            if ext_comm_info:
                rec_object = ext_comm_info[0]
                # TODO: Убрать дублирующий код в отдельный метод
                for voc in self.vocabluary.keys():
                    if rec_object.lower() in self.vocabluary[voc]:
                        rec_object_id = voc
                        break
            else:
                return EzhAction(
                    action=action_id,
                    answer='Что тебе порекомендовать?'
                    )
        else:
            return EzhAction(action=action_id,
                             answer=action_settings['answer'])

        return EzhAction(action_id=action_id,
                         wait_next=False,
                         ext=rec_object_id,
                         answer=action_settings['answer'])

    def do_action(self, action: EzhAction):
        action.answer = EzhDoActions.get_answer(action)
        return action
