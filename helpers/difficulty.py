"""Difficulty map to translate the Hiking Project API
difficulty codes to something that makes sense to a human"""

DIFFICULTY_MAP = {
    'missing': {'alt': 'Unknown', 'desc': 'This trail does not have a difficulty yet, be sure to set it after you\'re done!', 'code': 0},
    'green': {'alt': 'Easy', 'desc': 'No obstacles. Flat.', 'code': 1},
    'greenBlue': {'alt': 'Easy/Intermediate', 'desc': 'Some sections of uneven terrain. Mostly flat.', 'code': 2},
    'blue': {'alt': 'Intermediate', 'desc': 'Uneven terrain. Small inclines (max 10% grade).', 'code': 3},
    'blueBlack': {'alt': 'Intermediate/Difficult', 'desc': 'Some obstacles such as rocks or roots present. Moderate inclines.', 'code': 4},
    'black': {'alt': 'Difficult', 'desc': 'Tricky terrain. Steep. Not for beginners (max 15% grade).', 'code': 5},
    'dblack': {'alt': 'Extremely Difficult', 'desc': 'Potentially hazardous terrain. Very steep. Experts only.', 'code': 6}
}

class Difficulty:
    def __init__(self, hp_id):
        self.hp_id = hp_id
        try:
            self.diff_map = DIFFICULTY_MAP.get(hp_id)
        except AttributeError:
            #TODO: Implement logging :( 
            print(f'{self.hp_id} is an unknown difficuly. Assigning as missing, please report this at https://github.com/LEXmono/hiking_project_client')
            self.diff_map = DIFFICULTY_MAP.get('missing')
        self.alt = self.diff_map.get('alt')
        self.desc = self.diff_map.get('desc')
        self.code = self.diff_map.get('code')
        # Assign all of the arrtibutes in diff_map as attributes so we don't have to do a lot of setup here. 
    
    @property
    def __dict__(self):
        return self.diff_map

    def __str__(self):
        return f'{self.alt} - {self.desc}'

    def __repr__(self):
        return self.__str__()
