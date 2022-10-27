import datetime 

last_stations = ['A', 'D', 'E', 'K', 'H', 'J']
hrs = datetime.datetime.now()
hours = int(hrs.strftime('%H'))
min = datetime.datetime.now()
minutes = int(min.strftime('%M'))
localtime = int((hours * 60) + minutes)
time = datetime.datetime.now()
time = int(time.strftime('%H'))
stations_104 =  {'104_1':'A','104_2':'B','104_3':'C', '104_2':'D'}
stations_124 = {'124_1':'H','124_2': 'G','124_3': 'C', '124_4':'D'}
stations_487 ={ '487_1':'E', '487_2': 'A', '487_3':'B', '487_4': 'F'}

class Route104:
    def __init__(self, interval, route_time1, route_time2, full_route_time) -> None:
        
        self.full_route_time = full_route_time
        self.interval = interval
        self.route_time1 = route_time1
        self.route_time2 = route_time2
        self.station = stations_104
        self.lasts = last_stations
        self.time = time
        self.hours = hours
        self.minutes = minutes
        self.localtime = localtime
        
    def show_time(self):
        # stop_bus = input('Enter your current station: ')
        for key in self.station:
            if stop_bus == self.station[key]:
                if stop_bus in self.lasts:
                    if self.time > 1:  
                        overall= self.full_route_time - (self.localtime - (self.localtime // self.interval) * self.interval)
                        time = self.localtime - ((self.localtime // self.interval) * self.interval)
                        return  f' "104", destination "A": {overall} \n "104", destination "D": {time}'             
                    else:
                        print("Buses are not available now!")
                else:
                    if self.time > 1:  
                        overall = self.route_time1 - (self.localtime - (self.localtime // self.interval) * self.interval)
                        time = self.route_time2 - (self.localtime - ((self.localtime // self.interval) * self.interval))
                        return f' "104", destination "A": {overall} \n "104", destination "D": {time}'
                    else:
                        print("Buses are not available now!")


class Route124:
    def __init__(self, interval, route_time1, route_time2, full_route_time) -> None:
        
        self.full_route_time = full_route_time
        self.interval = interval
        self.route_time1 = route_time1
        self.route_time2 = route_time2
        self.station = stations_124
        self.lasts = last_stations
        self.time = time
        self.hours = hours
        self.minutes = minutes
        self.localtime = localtime
        
    def show_time(self):
        # stop_bus = input('Enter your current station: ')
        for key in self.station:
            if stop_bus == self.station[key]:
                if stop_bus in self.lasts:
                    if self.time > 1:  
                        overall= self.full_route_time - (self.localtime - (self.localtime // self.interval) * self.interval)
                        time = self.localtime - ((self.localtime // self.interval) * self.interval)
                        return  f' "124", destination "H": {overall} \n "124", destination "J": {time}'             
                    else:
                        print("Buses are not available now!")
                else:
                    if self.time > 1:  
                        overall = self.route_time1 - (self.localtime - (self.localtime // self.interval) * self.interval)
                        time = self.route_time2 - (self.localtime - ((self.localtime // self.interval) * self.interval))
                        return f' "124", destination "H": {overall} \n "124", destination "J": {time}'
                    else:
                        print("Buses are not available now!")

class Route487:
    def __init__(self, interval, route_time1, route_time2, full_route_time) -> None:
        
        self.full_route_time = full_route_time
        self.interval = interval
        self.route_time1 = route_time1
        self.route_time2 = route_time2
        self.station = stations_487
        self.lasts = last_stations
        self.time = time
        self.hours = hours
        self.minutes = minutes
        self.localtime = localtime
        
    def show_time(self):
        # stop_bus = input('Enter your current station: ')
        for key in self.station:
            if stop_bus == self.station[key]:
                if stop_bus in self.lasts:
                    if self.time > 1:  
                        overall= self.full_route_time - (self.localtime - (self.localtime // self.interval) * self.interval)
                        time = self.localtime - ((self.localtime // self.interval) * self.interval)
                        return  f' "487", destination "E": {overall} \n "487", destination "F": {time}'             
                    else:
                        print("Buses are not available now!")
                else:
                    if self.time > 1:  
                        overall = self.route_time1 - (self.localtime - (self.localtime // self.interval) * self.interval)
                        time = self.route_time2 - (self.localtime - ((self.localtime // self.interval) * self.interval))
                        return f' "487", destination "E": {overall} \n "487", destination "F": {time}'
                    else:
                        print("Buses are not available now!")

st104 = Route104(10, 9, 8, 12)
st124 = Route124(7, 10, 10, 15)
st487 = Route487(5, 9, 7, 13)
print(f'Time: {hours} : {minutes}')
while True:
    stop_bus = input('Enter your current station: ')
    print(st104.show_time())
    print(st124.show_time())
    print(st487.show_time())
