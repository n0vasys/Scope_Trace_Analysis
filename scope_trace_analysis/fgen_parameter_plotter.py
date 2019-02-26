###########################################################################################################################
#Function definitions
###########################################################################################################################

def generate_plots(d_file_name):    
    data_file_name = d_file_name
    data_file = open(data_file_name)


    noise, peak, fwhm, area = [], [], [], []
    for line in data_file: #loops through each line in the data file
        line_parameters = line.split("    ") # splits the entire line of numbers/words separated by certain characters into individual elements.
        
        counter = 0
        for parameter in line_parameters:
            if counter == 0:
                noise.append(float(parameter))
            elif counter == 1:
                peak.append(float(parameter))
            elif counter == 2:
                fwhm.append(float(parameter))
            elif counter == 3:
                area.append(float(parameter))
            counter +=1




    

    #plt.hist(noise)

    n, bins, patches = plt.hist(noise, 10, histtype='step',normed=1, facecolor='g', alpha=0.75)  #Added in histtype option, but is untested

    plt.title("Noise Histogram")
    plt.xlabel("Voltage [v]")
    plt.ylabel("Count") 
    plt.savefig(data_file_name[0:15] + "noise_plot" + data_file_name[27:-4] + ".png")
    plt.clf()

    n, bins, patches = plt.hist(peak, 10, histtype='step',normed=1, facecolor='g', alpha=0.75)

    plt.title("Peak Histogram")
    plt.xlabel("Voltage [v]")
    plt.ylabel("Count") 
    plt.savefig(data_file_name[0:15] + "peak_plot" + data_file_name[27:-4] + ".png")
    plt.clf()



        





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
        if file[-3:] == "dat":
            file_names.append(file)

    for name in file_names:
        generate_plots("../data/run" + str(run_number) + "/" + name)






