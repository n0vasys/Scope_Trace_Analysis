###########################################################################################################################
#Function definitions
###########################################################################################################################

def generate_plots(d_file_name):    
    data_file_name = d_file_name
    data_file = open(data_file_name)


    plot_counter = 0
    for line in data_file: #loops through each line in the data file
        line_data = [] # temporarily stores a single line from the text file 
        points = line.split(",") # splits the entire line of numbers/words separated by certain characters into individual elements.
        
        for singlePoint in points:
            line_data.append(float(singlePoint))

        time = np.arange(0.0000, 2e-04, 2e-08)

        plt.plot(time, line_data)

        plt.xlabel("Time [s]")
        plt.ylabel("Voltage [v]")
        plt.title("Trace plot")
        plt.savefig(data_file_name[0:15] + "trace_plot" + data_file_name[-13:-4] + "_measurement_" + str(plot_counter)+ ".png")
        plt.clf()

        plot_counter += 1





###########################################################################################################################

def generate_run_list(start_no, end_no):

    run_list = list(range(int(start_no), int(end_no)+1))

    return run_list




###########################################################################################################################
#Start of program
###########################################################################################################################
import matplotlib.pyplot as plt
import numpy as np
import os

start_run_number = input("Enter the first run number : ")
end_run_number = input("Enter the last run number : ")

full_run_list = generate_run_list(str(start_run_number), str(end_run_number))

for run_number in full_run_list:

    directory_name = "../data/run" + str(run_number)

    directory_files = os.listdir(directory_name)

    file_names = []

    for file in directory_files:
        if file[-3:] == "csv":
            file_names.append(file)

    for name in file_names:
        generate_plots("../data/run" + str(run_number) + "/" + name)






