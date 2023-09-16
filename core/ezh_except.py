class EzhException(BaseException):
    def __init__(self, *args, **kwargs):
        self.message = kwargs.get('message')
        self.code = kwargs.get('code')
