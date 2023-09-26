from datetime import datetime, timedelta


class UserSession():
    def __init__(self,
                 user_id: int,
                 chat_id: int,
                 lifetime: int,
                 **kwargs):
        self.id = kwargs.get('session_id')
        self.user_id = user_id
        self.chat_id = chat_id
        self.lifetime = lifetime
        self.expired = self.update()

    def is_expired(self) -> bool:
        return datetime.utcnow() > self.expired

    def update(self):
        return datetime.utcnow() + timedelta(seconds=self.lifetime)
