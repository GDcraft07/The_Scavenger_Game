class Count:
    def __init__(self):
        self.count = 0

    def accrual_of_points(self, count):
        self.count += count

    def deduction_of_points(self, time):
        self.count -= time

    def clearing_points(self):
        self.count = 0

    def return_points(self):
        return self.count
