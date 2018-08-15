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

    def variance(self):
        """AVERAGE SQUARED DIFFERANCE OF EACH OBSERVATION FROM THE MEAN"""
        mean = self.mean()

        l = list()
        for num in self.data:
            l.append( (num - mean)**2 )

        variance = sum(l) / len(l)
        print("Variance is:", variance)
        return variance





