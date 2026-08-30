class Gun:

    def __init__(self, flag: bool = True):
        self.flag = flag

    def shoot(self):
        [print('pif') if self.flag else print('paf')]
        if self.flag:
            self.flag = False
        else:
            self.flag = True
