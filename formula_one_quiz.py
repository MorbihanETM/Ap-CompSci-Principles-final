class FormulaOne:
    def __init__(self, max_verstappen: int, charles_leclerc: int, lando_norris: int, fernando_alonso: int, sergio_perez: int, carlos_sainz: int, oscar_piastri: int, lance_stroll: int, george_russell: int, lewis_hamilton: int, daniel_ricciardo: int, yuki_tsunoda: int, logan_sargeant: int, alexander_albon: int, nico_hulkenberg: int, kevin_magnussen: int, pierre_gasly: int, esteban_ocon: int, valterri_bottas: int, zhou_guanyu: int):
        self.driver = {
            'Max Verstappen': max_verstappen,
            'Charles Leclerc': charles_leclerc,
            'Lando Norris': lando_norris,
            'Fernando Alonso': fernando_alonso,
            'Sergio Perez': sergio_perez,
            'Carlos Sainz': carlos_sainz,
            'Oscar Piastri': oscar_piastri,
            'Lance Stroll': lance_stroll,
            'George Russell': george_russell,
            'Lewis Hamilton': lewis_hamilton,
            'Daniel Ricciardo': daniel_ricciardo,
            'Yuki Tsunoda': yuki_tsunoda,
            'Logan Sargeant': logan_sargeant,
            'Alexander Albon': alexander_albon,
            'Nico Hulkenberg': nico_hulkenberg,
            'Kevin Magnussen': kevin_magnussen,
            'Pierre Gasly': pierre_gasly,
            'Esteban Ocon': esteban_ocon,
            'Valterri Bottas': valterri_bottas,
            'Zhou Guanyu': zhou_guanyu

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
        if driver == 'Sergio Perez':
            self.driver['Sergio Perez'] = self.driver.get('Sergio Perez') + 1
        if driver == 'Carlos Sainz':
            self.driver['Carlos Sainz'] = self.driver.get('Carlos Sainz') + 1
        if driver == 'Oscar Piastri':
            self.driver['Oscar Piastri'] = self.driver.get('Oscar Piastri') + 1
        if driver == 'Lance Stroll':
            self.driver['Lance Stroll'] = self.driver.get('Lance Stroll') + 1
        if driver == 'George Russell':
            self.driver['George Russell'] = self.driver.get('George Russell') + 1
        if driver == 'Lewis Hamilton':
            self.driver['Lewis Hamilton'] = self.driver.get('Lewis Hamilton') + 1
        if driver == 'Daniel Ricciardo':
            self.driver['Daniel Ricciardo'] = self.driver.get('Daniel Ricciardo') + 1
        if driver == 'Yuki Tsunoda':
            self.driver['Yuki Tsunoda'] = self.driver.get('Yuki Tsunoda') + 1
        if driver == 'Logan Sargeant':
            self.driver['Logan Sargeant'] = self.driver.get('Logan Sargeant') + 1
        if driver == 'Alexander Albon':
            self.driver['Alexander Albon'] = self.driver.get('Alexander Albon') + 1
        if driver == 'Nico Hulkenberg':
            self.driver['Nico Hulkenberg'] = self.driver.get('Nico Hulkenberg') + 1
        if driver == 'Kevin Magnussen':
            self.driver['Kevin Magnussen'] = self.driver.get('Kevin Magnussen') + 1
        if driver == 'Pierre Gasly':
            self.driver['Pierre Gasly'] = self.driver.get('Pierre Gasly') + 1
        if driver == 'Esteban Ocon':
            self.driver['Esteban Ocon'] = self.driver.get('Esteban Ocon') + 1
        if driver == 'Valterri Bottas':
            self.driver['Valterri Bottas'] = self.driver.get('Valterri Bottas') + 1
        if driver == 'Zhou Guanyu':
            self.driver['Zhou Guanyu'] = self.driver.get('Zhou Guanyu') + 1
            
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
            'Fernando Alonso': 0,
            'Sergio Perez': 0,
            'Carlos Sainz': 0,
            'Oscar Piastri': 0,
            'Lance Stroll': 0,
            'George Russell': 0,
            'Lewis Hamilton': 0,
            'Daniel Ricciardo': 0,
            'Yuki Tsunoda': 0,
            'Logan Sargeant': 0,
            'Alexander Albon': 0,
            'Nico Hulkenberg': 0,
            'Kevin Magnussen': 0,
            'Pierre Gasly': 0,
            'Esteban Ocon': 0,
            'Valterri Bottas': 0,
            'Zhou Guanyu': 0
        }