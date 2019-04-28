import datetime

class Temperature:

    @ staticmethod
    def Temp_as_Cels(Celsius_in):
        return (9/5) * (Celsius_in + 32)

    @ staticmethod
    def Temp_as_Fahr(Fahrenheit_in):
        return (5/9) * (Fahrenheit_in - 32)

class TemperatureSensor:

    # static variable
    numberOfSensors = 0
                                                                                        # harcode date as a string for current time
    def __init__(self, Current_Temp_Reading_in, Time_in, Current_Temp_Type_in="celsius", Current_Date_in= datetime.datetime.now().strftime('%Y-%m-%d'), Location_in=1):
        TemperatureSensor.numberOfSensors += 1

        # assume we can't have a a temp reading lower than - 20
        if Current_Temp_Reading_in >= -20:
            self.CurrentTempReading = Current_Temp_Reading_in
        else:
            self.CurrentTempReading = "Current Temp Reading incorrect"

        # Check time is in 24 hour format e.g. 10:00 or 10.00
        if len(Time_in) == 5:
            self.time = Time_in
        else:
            self.time = "Time should be in a 24 hour format"

        # Check type in is either "celsius or Fahrenheit, convert to lower case
        if Current_Temp_Type_in.lower() == "celsius" or Current_Temp_Type_in.lower() == "fahrenheit":
            self.CurrentTempType = Current_Temp_Type_in
        else:
            self.CurrentTempType = "Current Temp should be in Celsius or Fahrenheit"

        # Check if Current_Date_in >= datetime.datetime.now() - compare using strings:
        if Current_Date_in >= datetime.datetime.now().strftime('%Y-%m-%d'):
            self.CurrentDate = Current_Date_in
        else:
            self.CurrentDate = "Date cannot be in the past"

        # Check if Location is 1, 2 or 3
        if Location_in == 1 or Location_in == 2 or Location_in == 3:
            self.Location = Location_in
        else:
            self.Location = ("Location must be Zone 1, 2 or 3")


    def Current_Temp(self):
        return self.CurrentTempReading


    def Temp_as_Cels(self):
            return Temperature.Temp_as_Cels(self.Current_Temp)

    def print_details(self):
        print("\n*** Temperature Reading ***")
        print("***************************")
        # if Temp passed in is Fahrenheit then we will display Celsius Conversion also
        if self.CurrentTempType.lower() == "fahrenheit":
            print("Celsius Temp is {}".format(Temperature.Temp_as_Cels(self.Current_Temp())))
        print("Current Temperature: {}".format(self.Current_Temp()))
        print("Current Temperature Type: {}".format(self.CurrentTempType))
        print("Current Date: {}".format(self.CurrentDate))
        print("Current Time: {}".format(self.time))
        print("Current Location: Zone {}".format(self.Location))

        #added
        print("Sensors: {}".format(TemperatureSensor.numberOfSensors))


# Create list and append 4 object to the list
TempList = []

Temp1 = TempList.append(TemperatureSensor(50, "10:0", "celsius", "2018-02-04", 4))
Temp2 = TempList.append(TemperatureSensor(30, "10:00", "Celsius", "2019-05-04", 2))
Temp3 = TempList.append(TemperatureSensor(80, "12:00", "Fahrenheit", "2019-28-04", 1))
Temp4 = TempList.append(TemperatureSensor(-10, "24:00", "Fahrenheit", "2019-28-10", 3))

# Iterate through the list
for temps in TempList:
    temps: TemperatureSensor
    temps.print_details()

# Print Total Sensors
print("\nTotal number of Sensors: {}".format(TemperatureSensor.numberOfSensors))

