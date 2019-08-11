from helpers.difficulty import Difficulty

class Trail:
    def __init__(self, trail_data: dict = None):
        self.id = None
        self.name = None
        if trail_data is None:
            trail_data = {}
        for key, value in trail_data.items():
            setattr(self, key, value) 

        # Use the difficulty helper to make difficulty data make sense. 
        self.difficulty = Difficulty(trail_data.get('difficulty'))

    def __repr__(self):
        return f'<Trail - id: {self.id}, name: {self.name}>'

    def __str__(self):
        return f'Trail {self.id}'
