import numpy as np


class CompassDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)

    def reverse(self, direction):
        if direction == 'N':
            return 0
        else:
            return np.mean(
                list(self.keys())[list(self.values()).index(direction)])


# Instantiate compass object

compass_reversal = CompassDict({range(0, 12): 'N', range(12, 34): 'NNE',
                                range(34, 57): 'NE', range(57, 79): 'ENE',
                                range(79, 102): 'E', range(102, 124): 'ESE',
                                range(124, 147): 'SE', range(147, 169): 'SSE',
                                range(169, 192): 'S', range(192, 214): 'SSW',
                                range(214, 237): 'SW', range(237, 259): 'WSW',
                                range(259, 282): 'W', range(282, 304): 'WNW',
                                range(304, 327): 'NW', range(327, 349): 'NNW',
                                range(349, 360): 'N'})


if __name__ == '__main__':
    print(compass_reversal[120])
    print(compass_reversal.reverse('NE'))