class FormulaOne:
    def __init__(self, max_verstappen: int, charles_leclerc: int, lando_norris: int, fernando_alonso: int):
        self.driver = {
            'Max Verstappen': max_verstappen,
            'Charles Leclerc': charles_leclerc,
            'Lando Norris': lando_norris,
            'Fernando Alonso': fernando_alonso
        }

    def add(self, driver: str) -> None:
        if driver == 'Max Verstappen':
            self.driver['Max Verstappen'] = self.driver.get('Max Verstappen') + 1
        if driver == 'Charles Leclerc':
            self.driver['Charles Leclerc'] = self.driver.get('Charles Leclerc') + 1
        if driver == 'Lando Norris':
            self.driver['Lando Norris'] = self.driver.get('Lando Norris') + 1
        if driver == 'Fernando Alonso':
            self.driver['Fernando Alonso'] = self.driver.get('Fernando Alonso') + 1

    def sort(self) -> str:
        score = 0
        result = ''
        for driver, points in self.driver.items():
            if points > score:
                score = points
                result = driver

        return result

    def clear(self) -> None:
        self.driver = {
            'Max Verstappen': 0,
            'Charles Leclerc': 0,
            'Lando Norris': 0,
            'Fernando Alonso': 0
        }
