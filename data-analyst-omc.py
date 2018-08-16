import math

class DataAnalyst:

    data = list()

    # def __init__(self,userdata):
    #     self.data = userdata

    def mean(self):
        """We calculate the mean by adding all of our values together, and dividing by the number of values in our dataset"""
        # string = ""
        # for num in self.data:
        #     string = string + str(num) + "+"
        # string = string[:-1]
        # print("1:-adding all of our values together:\n{0}".format(string))

        total = sum(self.data)
        # print("total", total)
        # print("2.and dividing by the number of values ({0}) in our dataset ".format(len(self.data)))
        # print(total, "/", len(self.data), "is", total / len(self.data))

        return total / len(self.data)

    def medien(self,data):

        self.data.sort()
        index = len(self.data)

        # this mean values of our data is odd number
        if len(self.data) % 2 != 0:
            return self.data[int(((index + 1) / 2 - 1))]
        else:
            num1 = self.data[int(((index / 2) - 1))]
            num2 = self.data[int((index / 2))]
            return (num1 + num2) / 2


    def five_number_summary(self):

        self.data.sort()

        minimum = min(self.data)
        maximum = max(self.data)
        Q2 = self.medien(self.data)

        index = len(self.data)

        if index % 2 != 0:
            Q1 = self.medien(self.data[:(int(((index + 1) / 2 - 1)))])
            Q3 = self.medien(self.data[int(((index + 1) / 2)):])
        else:
            Q1 = self.medien(self.data[:(int(((index + 1) / 2)))])
            Q3 = self.medien(self.data[int(((index + 1) / 2)):])
        return minimum, Q1, Q2, Q3, maximum

    def range_(self):
        minimum,maximum = self.five_number_summary()[0::4]
        return maximum - minimum

    def interquartile(self):
        Q1,Q3 = self.five_number_summary()[1:-1:2]
        return Q3 - Q1


    def variance(self):
        """AVERAGE SQUARED DIFFERANCE OF EACH OBSERVATION FROM THE MEAN"""
        mean = self.mean()

        l = list()
        for num in self.data:
            l.append( (num - mean)**2 )

        variance = sum(l) / len(l)
        # print("Variance is:", variance)
        return variance



    def standard_deviation(self):
        """on average how much each point varies from the mean of the points,
        Standard deviation is the square root of the variance
        """
        standard_deviation = math.sqrt(self.variance())
        # print("Standard deviation is", standard_deviation)
        return standard_deviation




a = DataAnalyst()
a.data = [1, 5, 10, 3, 8, 12, 4]
print(a.data)
print(a.range_())
