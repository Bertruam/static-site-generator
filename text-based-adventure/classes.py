direction = ('North', 'South', 'East', 'West', 'North East', 'North West', 'South East', 'South West')

class room():
    def __init__(self):
        self.name = ''
        self.description = ''
        self.exit_list = []
        self.items_here = []
        self.locks_here = []

class item():
    def __init__(self):
        self.name = ''
        self.description = ''

class lock():
    def __init__(self):
        self.name = ''
        self.description = ''
        self.my_key = item

class exit():
    def __init__(self) -> None:
        self.name = ''
        self.description = ''
        self.my_dir = direction
        self.lock = []


