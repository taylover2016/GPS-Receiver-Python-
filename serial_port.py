# A simple serial port implementation via Python
# Created on Jan 1st,2020 by Tony Zhang
# Happy New Year!


import serial

# Initialize a serial-port communication
serial_com = serial.Serial("COM7", 9600)

# Use $GPRMC message to get the current location
while True:
    reading_buffer = serial_com.read_until(",A,".encode(encoding="utf-8"))
    location_buffer = serial_com.read(24)

    # Decode the location
    location = location_buffer.decode(encoding="utf-8")

    # Output the location
    print(location)
