

class Trail:
    def __init__(self, trail_data: dict = None):
        if trail_data is None:
            trail_data = {}
        self.ascent = trail_data.get('ascent')
        self.conditionDate = trail_data.get('conditionDate')
        self.conditionStatus = trail_data.get('conditionStatus')
        self.difficulty = trail_data.get('difficulty')
        self.high = trail_data.get('high')
        self.id = trail_data.get('id')
        self.imgMedium = trail_data.get('imgMedium')
        self.imgSmall = trail_data.get('imgSmall')
        self.imgSmallMed = trail_data.get('imgSmallMed')
        self.imgSqSmall = trail_data.get('imgSqSmall')
        self.latitude = trail_data.get('latitude')
        self.location = trail_data.get('location')
        self.longitude = trail_data.get('longitude')
        self.low = trail_data.get('low')
        self.name = trail_data.get('name')
        self.starVotes = trail_data.get('starVotes')
        self.stars = trail_data.get('stars')
        self.summary = trail_data.get('summary')
        self.type = trail_data.get('type')
        self.url = trail_data.get('url')

    def __repr__(self):
        return f'<Trail - id: {self.id}, name: {self.name}>'

    def __str__(self):
        return f'Trail {self.id}'
