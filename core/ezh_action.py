class EzhAction():
    def __init__(self, *args, **kwargs):
        '''
            action_id: str
            wait_next: bool
            ext: str
            answer: str
            args: передавать только в строго заданном порядке
        '''
        if args:
            self.act_id,
            self.wait_next,
            self.ext,
            self.answer = args

        self.act_id: str = kwargs.get('action_id')
        self.wait_next: bool = kwargs.get('wait_next')
        self.ext: str = kwargs.get('ext')
        self.answer: str = kwargs.get('answer')

    def __str__(self):
        return (f"{self.act_id} {self.wait_next} "
                f"{self.ext} {self.answer}")
