class Record:

    def __init__(self,name,number,type,amount):
        self.name=name
        self.number=number
        self.type=type
        self.amount=amount



record_1= Record('shipra',1234567890,'c',1500)
record_2= Record('ruhi',1234567891,'c',1200)

record=[record_1,record_2]