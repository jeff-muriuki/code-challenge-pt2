class Band:
    all = []

    def __init__(self, name, hometown):
        self.name = name
        if isinstance(hometown, str) and len(hometown) > 0:
            self._hometown = hometown
        else:
            raise ValueError('hometown must be a non-empty string')
        Band.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError('Name must be a non-empty string')

    @property
    def hometown(self):
        return self._hometown

    
    def concerts(self):
        return [concert for concert in Concert.all if concert.band == self]

    
    def venues(self):
        return list(set(concert.venue for concert in self.concerts()))

    def play_in_venue(self, venue, date):
        if not isinstance(venue, Venue):
            raise ValueError('venue must be an instance of Venue')
        concert = Concert(date, self, venue)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()]


class Venue:
    all = []

    def __init__(self, name, city):
        self.name = name
        self.city = city
        Venue.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError('Name must be a non-empty string')

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError('City must be a non-empty string')

    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):
        return list(set(concert.band for concert in self.concerts()))

    def concert_on(self, date):
        for concert in self.concerts():
            if concert.date == date:
                return concert
        return None


class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError('Date must be a non-empty string')

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise ValueError('Band must be an instance of Band')

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise ValueError('Venue must be an instance of Venue')

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f'Hello {self.venue.city}!!!!! We are {self.band.name} and we\'re from {self.band.hometown}'


