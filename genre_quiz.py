class GenreQuiz:
    """ The genre Quiz"""
    def __init__(self, pop: int, jazz: int, electropop: int, classical: int):
        self.genre = {
            'pop': pop,
            'jazz': jazz,
            'electropop': electropop,
            'metal': classical
        }

    def add(self, genre: str) -> None:
        """adds a point to the provided genre"""
        if genre == 'pop':
            self.genre['pop'] = self.genre.get('pop') + 1
        if genre == 'jazz':
            self.genre['jazz'] = self.genre.get('jazz') + 1
        if genre == 'electropop':
            self.genre['electropop'] = self.genre.get('electropop') + 1
        if genre == 'classical':
            self.genre['classical'] = self.genre.get('classical') + 1

    def sort(self) -> str:
        """returns the first genre with the highest score"""
        score = 0
        result = ''
        for genre, points in self.genre.items():
            if points > score:
                result = genre

        return result

    def clear(self) -> None:
        """resets all genre points"""
        self.genre = {
            'pop': 0,
            'jazz': 0,
            'electropop': 0,
            'classical': 0
        }
