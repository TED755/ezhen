class EzhAction():
    def __init__(self, *args, **kwargs):
        '''
            action: str
            wait_next: bool
            ext: str
            answer: str
            args: передавать только в строго заданном порядке
        '''
        if args:
            self.act_id,
            self.wait_next,
            self.ext_commands,
            self.answer = args

        self.act_id = kwargs.get('action')
        self.wait_next = kwargs.get('wait_next')
        self.ext_commands = kwargs.get('ext')
        self.answer = kwargs.get('answer')
