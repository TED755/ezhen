import json
from core.ezhen_settings import EZHEN_TOKEN
from core.ezh_except import EzhException
from core.actions.ezh_action import EzhAction
from core.ezh_do_actions import EzhDoActions
from core.user_session import UserSession


class EzhenCore():
    def __init__(self):
        self.token = EZHEN_TOKEN
        self.user_sessions = []
        try:
            with open('core/ezhen_vocabluary.json', 'r') as vocabluary:
                self.vocabluary: dict = json.load(vocabluary)
            with open('core/ezhen_actions.json', 'r') as actions:
                self.actions: dict = json.load(actions)
            with open('core/ezh_config.json', 'r') as config:
                self.config: dict = json.load(config)
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
        print(f"find_action: {find_action}")
        action_id = self.__find_action(find_action)
        print(f"Action id: {action_id}")
        if action_id:
            action = self.__form_action(action_id, messages[1:])
            return action

    def __form_action(self, action_id: str,
                      ext_comm_info: list = []) -> EzhAction:
        action_settings = self.actions.get(action_id)
        if not action_id:
            return EzhAction(act_id=None, answer='Я тебя не понял. Я пока могу'
                             ' не все, поэтому посмотри еще раз, что я могу и '
                             'обратись еще раз')

        if action_settings['need_ext']:
            if ext_comm_info:
                rec_object = ' '.join(ext_comm_info)
                rec_object_id = self.__find_action(rec_object)
                action = self.__form_action(rec_object_id)
            else:
                return EzhAction(
                    act_id=action_id,
                    answer=action_settings['bad_answer'],
                    wait_next=True)
        else:
            return EzhAction(act_id=action_id,
                             answer=action_settings['answer'],
                             wait_next=False)

        # return EzhAction(action_id=action_id,
        #                  wait_next=False,
        #                  ext=rec_object_id,
        #                  answer=action_settings['answer'])
        return action

    def do_action(self, action: EzhAction) -> EzhAction:
        action.answer = EzhDoActions.get_answer(action)
        return action

    def new_user_session(self, user_id, chat_id):
        self.user_sessions.append(
            UserSession(user_id,
                        chat_id,
                        self.config['user_session_lifetime']))

        # if self.user_sessions.get(user_id):
        #     user_sesions = self.user_sessions[user_id]
        #     user_sesions.append(new_session)
        #     self.user_sessions[user_id] = user_sesions
        # else:
        #     user_sesions = []
        #     user_sesions.append(new_session)

    def close_unactive_sessions(self) -> list:
        sessions = self.user_sessions
        close_sessions = []
        for session in sessions:
            if session.is_expired():
                self.user_sessions.remove(session)
                close_sessions.append(session)

        return close_sessions

    def check_user_active_session(self, user_id, session_id) -> UserSession:
        for session in self.user_sessions:
            if session.user_id == user_id and \
               session.chat_id == session_id:
                return session

    def __find_action(self, find_object: str):
        for voc in self.vocabluary.keys():
            if find_object.lower() in self.vocabluary[voc]:
                return voc
