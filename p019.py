
class Date:
    def __init__(self, d=1, m=1, y=1900):
        self.date = d
        self.month = m
        self.year = y

    def __str__(self):
        return str(self.date)+'/'+str(self.month)+'/'+str(self.year)

    def __lt__(self, other):
        if self.year!=other.year:
            return self.year < other.year
        elif self.month!=other.month:
            return self.month < other.month
        else:
            return self.date < other.date

    def ndays_current_month(self):
        if self.month in [4,6,9,11]:
            return 30
        elif self.month==2:
            if self.year%4==0:
                if self.year%100==0:
                    if self.year%400==0:
                        return 29
                    else:
                        return 28
                else:
                    return 29
            else:
                return 28
        else:
            return 31

    def nextweek(self):
        d = Date(self.date, self.month, self.year)
        ndays = self.ndays_current_month()
        if ndays-self.date >= 7:
            d.date += 7
        else:
            d.date = 7-(ndays-self.date)
            if self.month < 12:
                d.month += 1
            else:
                d.month = 1
                d.year += 1
        return d

start = Date(1,1,1901)        
end = Date(31,12,2000)
current = Date(7,1,1900)
n = 0

while current < end:
    if (not(current < start)) and (current.date==1):
        n += 1
    current = current.nextweek()

print(n)

