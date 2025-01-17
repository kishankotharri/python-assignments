class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other_time):
        total_minutes = self.minutes + other_time.minutes
        total_hours = self.hours + other_time.hours + (total_minutes // 60)
        remaining_minutes = total_minutes % 60
        return Time(total_hours, remaining_minutes)
    
    def displayMinute(self):
        total_minutes = self.minutes + (self.hours * 60)
        return total_minutes

    def __str__(self):
        return f"{self.hours} hours and {self.minutes} minutes"

# Example usage
time1 = Time(2, 50)
time2 = Time(1, 20)
result = time1.addTime(time2)
print("Resultant time:", result)

time3 = Time(1, 2)
print("Resultant time:", time3.displayMinute())