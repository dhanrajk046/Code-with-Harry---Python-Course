from random import randint

class Train:

    def __init__(slf, trainno):
        slf.trainno = trainno

    def book(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainno} from {fro} to {to}.")

    def getStatus(self):
        print(f"Train no: {self.trainno} is running on time.")

    def getFare(slf, fro, to):
        print(f"Ticket fare for train no: {slf.trainno} from {fro} to {to} is {randint(222, 5555)} INR.")


t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")
