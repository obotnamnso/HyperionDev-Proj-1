def celsius_to_kelvin(temp):
    return temp + 273.15

def kelvin_to_celsius(temp):
    return temp - 273.15

temp = float(input('Enter the temperature: '))
unit_of_measurement = input(''' What are the unit of measurement?
                                Select the appropriate below:
                                1. Degree Celsius.
                                2. Kelvin
                            ''')

if unit_of_measurement == '1':
    result = celsius_to_kelvin(temp)
elif unit_of_measurement == '2':
    result = kelvin_to_celsius(temp) 
else:
    print('Wrong input select either 1 or 2')

print(f'Your temperature converted is: {result}')
