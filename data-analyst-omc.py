import math

class DataAnalyst:

    data = list()

    def __init__(self):
        pass

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

    def medien(data):

        data.sort()
        index = len(data)

        # this mean values of our data is odd number
        if len(data) % 2 != 0:
            return data[int(((index + 1) / 2 - 1))]
        else:
            num1 = data[int(((index / 2) - 1))]
            num2 = data[int((index / 2))]
            return (num1 + num2) / 2


    def variance(self):
        """AVERAGE SQUARED DIFFERANCE OF EACH OBSERVATION FROM THE MEAN"""
        mean = self.mean()

        l = list()
        for num in self.data:
            l.append( (num - mean)**2 )

        variance = sum(l) / len(l)
        print("Variance is:", variance)
        return variance


    def standard_deviation(self):
        """on average how much each point varies from the mean of the points,
        Standard deviation is the square root of the variance
        """
        standard_deviation = math.sqrt(self.variance())
        print("Standard deviation is", standard_deviation)
        return standard_deviation




a = DataAnalyst()
a.data = [1, 5, 10, 3, 8, 12, 4]
a.standard_deviation()