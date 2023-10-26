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
        self.update()

    def is_expired(self) -> bool:
        return datetime.utcnow() > self.expired

    def update(self):
        self.expired = datetime.utcnow() + timedelta(seconds=self.lifetime)

    def get_session_hash(self):
        return hash(str(self.user_id + self.chat_id))

    def __str__(self):
        return f"{self.id}, {self.user_id}, {self.chat_id}"
