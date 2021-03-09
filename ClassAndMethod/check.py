class Student:
    def __init__(self, name):
        self.name = name

    def calculateAvg(self, data):
        sum = 0
        for num in data:
            sum += num

        avg = sum/len(data)
        return avg

    def jadge(self, avg):

        if(avg >= 60):
            result = "passed"
        else:
            result = "failed"
        return result


a001 = Student("sato")

data = [70, 65, 30, 90, 30]
avg = a001.calculateAvg(data)

result = a001.jadge(avg)

print(avg)
print(a001.name + " " + result)
