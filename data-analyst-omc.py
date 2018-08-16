import math

class DataAnalyst:

    data = [1]

    # def __init__(self,data):
    #      self.data = data

    def mean(self,data):
        """We calculate the mean by adding all of our values together, and dividing by the number of values in our dataset"""
        # string = ""
        # for num in self.data:
        #     string = string + str(num) + "+"
        # string = string[:-1]
        # print("1:-adding all of our values together:\n{0}".format(string))

        total = sum(data)
        # print("total", total)
        # print("2.and dividing by the number of values ({0}) in our dataset ".format(len(self.data)))
        # print(total, "/", len(self.data), "is", total / len(self.data))

        return total / len(data)

    def medien(self,data ):
        data.sort()
        index = len(data)

        # this mean values of our data is odd number
        if len(data) % 2 != 0:
            return data[int(((index + 1) / 2 - 1))]
        else:
            num1 = data[int(((index / 2) - 1))]
            num2 = data[int((index / 2))]
            return (num1 + num2) / 2


    def five_number_summary(self,data):

        data.sort()

        minimum = min(data)
        maximum = max(data)
        Q2 = self.medien(data)

        index = len(data)

        if index % 2 != 0:
            Q1 = self.medien(data[:(int(((index + 1) / 2 - 1)))])
            Q3 = self.medien(data[int(((index + 1) / 2)):])
        else:
            Q1 = self.medien(data[:(int(((index + 1) / 2)))])
            Q3 = self.medien(data[int(((index + 1) / 2)):])
        return minimum, Q1, Q2, Q3, maximum

    def range_(self,data):
        minimum,maximum = self.five_number_summary(data)[0::4]
        return maximum - minimum

    def interquartile(self,data):
        Q1,Q3 = self.five_number_summary(data)[1:-1:2]
        return Q3 - Q1


    def variance(self,data):
        """AVERAGE SQUARED DIFFERANCE OF EACH OBSERVATION FROM THE MEAN"""
        mean = self.mean(data)

        l = list()
        for num in data:
            l.append( (num - mean)**2 )

        variance = sum(l) / len(l)
        # print("Variance is:", variance)
        return variance



    def standard_deviation(self,data):
        """on average how much each point varies from the mean of the points,
        Standard deviation is the square root of the variance
        """
        standard_deviation = math.sqrt(self.variance(data))
        # print("Standard deviation is", standard_deviation)
        return standard_deviation




a = DataAnalyst()
l = [15, 4, 3, 8, 15, 22, 7, 9, 2, 3, 3, 12, 6]
print("meadian",a.interquartile(l))
print("mean",a.range_(l))
print("v",a.variance(l))
print("standard",a.standard_deviation(l))
