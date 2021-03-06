from algorithms.variability import VariabilityTest, cut_data
# from variability import VariabilityTest, cut_data
from time import time


def create_points(jd, mag):
    points = []
    for i in range(len(jd)):
        points.append(Point(jd[i], mag[i]))
    return points


def calculate_period(jd, period, mo=2450000):
    return (jd - mo) / period


class Point(object):
    def __init__(self, jd, magnitudo):
        self.jd = jd
        self.magnitudo = magnitudo


class Period(object):
    def __init__(self, times, magnitudo, mo, is_phase, period=0.9042):
        self.is_phase = is_phase
        self.points = create_points(times, magnitudo)
        self.secondPartOfPoints = create_points(times, magnitudo)
        self.period = period
        self.mo = mo
        self.tolerance = 0.1

    def calculate(self):
        for point in self.points:
            jd = point.jd
            part1 = calculate_period(float(jd), self.period, self.mo)
            part2 = int(calculate_period(float(jd), self.period, self.mo))
            point.jd = part1 - part2
        self.add_second_part_of_points()
        if not self.is_phase:
            for point in self.points:
                point.jd = self.mo + self.period*point.jd
        return self.points

    def add_second_part_of_points(self):
        for point in self.secondPartOfPoints:
            jd = point.jd
            part1 = calculate_period(float(jd), self.period, self.mo)
            part2 = int(calculate_period(float(jd), self.period, self.mo))
            point.jd = part1 - part2 + 1
        self.points.extend(self.secondPartOfPoints)


class ExperimentalPeriod(object):
    def __init__(self, times, magnitudo):
        self.times = times
        self.magnitudo = magnitudo
        self.min = 0
        self.max = 1
        self.step = 0.0001
        self.calculate()

    def calculate_ten_times(self):
        for i in range(1, 10):
            points = Period(self.times, self.magnitudo, i / 10000).calculate()
            t = []
            m = []
            for p in points:
                t.append(float(p.jd))
                m.append(float(p.magnitudo))
            new_result = VariabilityTest(m, t, 2).calculate()

    def calculate(self):
        per = 0
        result = 0
        t1 = time()
        self.calculate_ten_times()
        avg_time = time() - t1
        print("It will take %s sec in avg" % (avg_time * 1000))
        for i in range(1, 10000):
            points = Period(self.times, self.magnitudo, i / 10000).calculate()
            t = []
            m = []
            for p in points:
                t.append(float(p.jd))
                m.append(float(p.magnitudo))
            new_result = VariabilityTest(m, t, 2).calculate()
            if new_result > result:
                per = i / 10000
                result = new_result
                print("Current per: %s\nCurrent result: %s" % (per, result))
                # print("%s - %s" % (result, i))
        print("Per: %s\nResult: %s" % (per, result))


if __name__ == '__main__':
    file = open("/home/laszlo/workspace/astroConverter/mats/AC-Cru.txt", "r")
    data = file.read()
    data = cut_data(data)
    t1 = time()
    exp = ExperimentalPeriod(data[0], data[1])
    print("It took %s seconds" % (time() - t1))
