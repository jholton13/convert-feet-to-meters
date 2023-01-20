#
# Jasmine Holton
# January 19 2023
# Wavelength Classifier
#

# Get the wavelength.
wavelength = float(input('Enter the wavelength (in nm): '))

# Determine the classification of the wavelength
# and display the result.
if wavelength < 10:
    print('Below range')
elif wavelength > 10 or wavelength <= 401:
    print('Infrared')
elif wavelength > 401 or wavelength < 701:
    print('Visible light')
elif wavelength > 701 or wavelength < 1000:
    print('Ultraviolet')
else:
    print('Above range')
print('Above range')
