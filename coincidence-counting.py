# Justin Smethers with slight modifications by Christopher Jacobs 
# Purdue Fort Wayne Physics
# Advised by Dr. Mark Masters


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as plticker
import numpy as np
import serial
#Send information to PSOC to set channels for single counts and coincidence counts
def set_channels(name_list):
    name_list = name_list.split(',')
    individual_channel_list = []
    coincident_channel_list = []
    chn_cmnd_list = []
    for name in name_list:
        if name.upper() == 'A':
            individual_channel_list.append('Channel A')
            chn_cmnd_list.append("CHN1000\r\n")
        elif name.upper() == 'B':
            individual_channel_list.append('Channel B')
            chn_cmnd_list.append("CHN0100\r\n")
        elif name.upper() == 'C':
            individual_channel_list.append('Channel C')
            chn_cmnd_list.append("CHN0010\r\n")
        elif name.upper() == 'D':
            individual_channel_list.append('Channel D')
            chn_cmnd_list.append("CHN0001\r\n")
        elif name.upper() == 'AB':
            coincident_channel_list.append('Channel AB')
            chn_cmnd_list.append("CHN1100\r\n")
        elif name.upper() == 'AC':
            coincident_channel_list.append('Channel AC')
            chn_cmnd_list.append("CHN1010\r\n")
        elif name.upper() == 'AD':
            coincident_channel_list.append('Channel AD')
            chn_cmnd_list.append("CHN1001\r\n")
        elif name.upper() == 'BC':
            coincident_channel_list.append('Channel BC')
            chn_cmnd_list.append("CHN0110\r\n")
        elif name.upper() == 'BD':
            coincident_channel_list.append('Channel BD')
            chn_cmnd_list.append("CHN0101\r\n")
        elif name.upper() == 'CD':
            coincident_channel_list.append('Channel CD')
            chn_cmnd_list.append("CHN0011\r\n")

        elif name.upper() == 'ABC':
            coincident_channel_list.append('Channel ABC')
            chn_cmnd_list.append("CHN1110\r\n")
        elif name.upper() == 'ABD':
            coincident_channel_list.append('Channel ABD')
            chn_cmnd_list.append("CHN1101\r\n")
        elif name.upper() == 'BCD':
            coincident_channel_list.append('Channel BCD')
            chn_cmnd_list.append("CHN0111\r\n")

        elif name.upper() == 'ABCD':
            coincident_channel_list.append('Channel ABCD')
            chn_cmnd_list.append("CHN1111\r\n")

    print('Individual channel list:', individual_channel_list)
    print('Coincident channel list:', coincident_channel_list)
    for i in range(len(chn_cmnd_list)):
        ser.write(str("CTR" + str(i) + "\r\n").encode())
        ser.write(chn_cmnd_list[i].encode())

    output = ser.readline().decode()
    while output != "":
        output = ser.readline().decode()

    return individual_channel_list, coincident_channel_list
#plot the data with an animation graph that is dynamic to the channels asked for
def plot_data(individual_channel_list, coincident_channel_list):
    # Print start message to the console
    print('starting plot data')

    # Send commands to the PSoC to turn of echo and execute the start function
    ser.write("ECO 0\r\n".encode())
    output = ser.readline().decode()
    while output != "":
        output = ser.readline().decode()
        print(output)
        # Write the start command to the data collection device
    ser.write("STA\r\n".encode())
    # Get the output from the data collection device
    output = ser.readline().decode()

    # Create figure for plotting
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.legend(loc="upper left")
    #produce list for each counter in numpy array
    xs = []
    ys = [[],[],[],[],[],[],[],[]]

    # This function is called periodically from FuncAnimation
    def animate(i, xs, ys):

        # Read output from PSOC

        output = ser.readline().decode().strip()
        list_of_outputs = output.split(",")
        print(list_of_outputs)
        print(individual_channel_list[0], list_of_outputs[0])
        print(individual_channel_list[1], list_of_outputs[1])
        #Add x length to self
        xs.append(len(xs))
        # Draw x and y lists
        ax.clear()
        for channel  in range(0,len(individual_channel_list)):
            #add outputs to y list
            ys[channel].append(list_of_outputs[channel])
            # Limit x and y lists to 20 items
            xs = xs[-20:]
            ys[channel] = ys[channel][-20:]

            print(ys[channel])
            ax.plot(xs, ys[channel], label = str(individual_channel_list[channel]))
            channel++1

        # Format plot
        loc1 = plticker.MultipleLocator(base=1.0)  # this locator puts ticks at regular intervals
        ax.xaxis.set_major_locator(loc1)
        ax.yaxis.set_major_locator(loc1)
        plt.subplots_adjust(bottom=0.30)
        plt.legend(loc="upper left")
        plt.title('Single Photon Counts')
        plt.ylabel('Counts')
        plt.xlabel('Seconds')
        plt.xticks(rotation=90)




    #animate and show plot
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
    plt.show()






communication_port = 'COM7'

# Open serial port for reading/writing
ser = serial.Serial(communication_port, 115200)
ser.timeout = 1
#Automatically begin communication with PSOC
ser.write("ECO 1\r\n".encode())
output = ser.readline().decode()
while output != "":
    output = ser.readline().decode()
    print(output)


# Wait for user input - for use in outputting multiple commands to the control device
print("\nType 'sta' to start plotting")
print("Type 'hlp' for list of commands")
entry = input("\nEnter command, or q to quit: ")
while entry != "q":
    # Code to run if user inputs "sta" to start
    if entry.upper().startswith("STA"):
        print('\n------------------------------------------------------------------------------------------')
        print('WARNING: file "last_saved_run.csv" will be overwritten unless it has been moved or renamed')
        print('------------------------------------------------------------------------------------------\n')


        # Allow user to enter channels to collect data from
        chosen_channels = input('Enter channels to be used: (eg \'A,B,C,ABC\')\n')
        # quick start ups for grangiers exp type SPD/spd
        if (chosen_channels == "SPD" or chosen_channels =="spd"):
            chosen_channels = "D,A,B,C,AD,AB"
            individual_channel_list, coincident_channel_list = set_channels(chosen_channels)
            plot_data(individual_channel_list,coincident_channel_list)



    elif entry.upper().startswith("HLP"):
        ser.write((entry + '\r\n').encode())
        output = ser.readline().decode()
        while output != "":
            print(output)
            output = ser.readline().decode()
    elif entry.upper().startswith("SCN"):
        ser.write((entry + '\r\n').encode())
        output = ser.readline().decode()
        while output != "":
            print(output)
            output = ser.readline().decode()
    elif entry.upper().startswith("CHN"):
        ser.write((entry + '\r\n').encode())
        output = ser.readline().decode()
        while output != "":
            print(output)
            output = ser.readline().decode()
    elif entry.upper().startswith("CTR"):
        ser.write((entry + '\r\n').encode())
        output = ser.readline().decode()
        while output != "":
            print(output)
            output = ser.readline().decode()
    elif entry.upper().startswith("LSC"):
        ser.write((entry + '\r\n').encode())
        output = ser.readline().decode()
        while output != "":
            print(output)
            output = ser.readline().decode()
    elif entry.upper().startswith("LVL"):
        ser.write((entry + '\r\n').encode())
        output = ser.readline().decode()
        while output != "":
            print(output)
            output = ser.readline().decode()
    elif entry.upper().startswith("DAC"):
        ser.write((entry + '\r\n').encode())
        output = ser.readline().decode()
        while output != "":
            print(output)
            output = ser.readline().decode()
    elif entry.upper().startswith("COL"):
        ser.write((entry + '\r\n').encode())
        output = ser.readline().decode()
        while output != "":
            print(output)
            output = ser.readline().decode()
    elif entry.upper().startswith("WIN"):
        ser.write((entry + '\r\n').encode())
        output = ser.readline().decode()
        while output != "":
            print(output)
            output = ser.readline().decode()
    elif entry.upper().startswith("ECO"):
        ser.write((entry + '\r\n').encode())
        output = ser.readline().decode()
        while output != "":
            print(output)
            output = ser.readline().decode()
    elif entry.upper().startswith("MAXDV"):
        ser.write((entry + '\r\n').encode())
        output = ser.readline().decode()
        while output != "":
            print(output)
            output = ser.readline().decode()
    elif entry.upper().startswith("MINDV"):
        ser.write((entry + '\r\n').encode())
        output = ser.readline().decode()
        while output != "":
            print(output)
            output = ser.readline().decode()

    else:
        print("Invalid command in this context")

    entry = input("\nEnter command, or q to quit: ")
print("Quitting...")


