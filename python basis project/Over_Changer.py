class Over_Changer:
    def __init__(self, Meter_1_reading, Meter_2_reading, Meter_1_bill, Meter_2_bill):
        self.Meter_1_reading = Meter_1_reading
        self.Meter_2_reading = Meter_2_reading
        self.Meter_1_bill = Meter_1_bill
        self.Meter_2_bill = Meter_2_bill

    @property
    def Meter_1_Total_reading(self):
        return self.Meter_1_reading - self.Meter_1_bill

    @Meter_1_Total_reading.setter
    def Meter_1_Total_reading(self, val):
        self.Meter_1_reading = val
        self.Meter_1_bill = val

    @property
    def Meter_2_Total_reading(self):
        return self.Meter_2_reading - self.Meter_2_bill

    @Meter_2_Total_reading.setter
    def Meter_2_Total_reading(self, val):
        self.Meter_2_reading = val
        self.Meter_2_bill = val

    def Check_reading(self):
        meter_1run = 0
        meter_2run = 0

        if self.Meter_1_Total_reading > self.Meter_2_Total_reading:
            meter_1run = self.Meter_1_Total_reading
        else:
            meter_2run = self.Meter_2_Total_reading

        meter_ON = None

        if meter_1run:
            meter_ON = meter_1run
        else:
            meter_ON = meter_2run

        if meter_ON == meter_1run:
            runing_meter = "Meter_1"
        else:
            runing_meter = "Meter_2"

        print(f"Your {runing_meter} is on with {meter_ON} Unit")

if __name__ == "__main__" :
    Oc = Over_Changer(5540, 440, 5000, 400)
    
    Oc.Meter_1_Total_reading = 56666
    Oc.Meter_2_Total_reading = 89888
    Oc.Check_reading()
