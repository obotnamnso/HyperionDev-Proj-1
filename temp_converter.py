def celsius_to_kelvin(temp):
    return temp + 273.15

temp = float(input('Enter the temperature in degree celsius: '))

temp_kelvin = celsius_to_kelvin(temp) 

print(f'Your temperature in Kelvin is: {temp_kelvin}')
