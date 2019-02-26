###########################################################################################################################
#Function definitions
###########################################################################################################################

def calculate_trace_params(d_file_name):    
    data_file_name = d_file_name

    out_data_file_name = data_file_name.replace("_data", "_params")

    output_data_file_name = out_data_file_name[:-3] + "dat"

    sampling_frequency = 50000000

    data_file = open(data_file_name)
    output_data_file = open(output_data_file_name, 'a')


    for line in data_file: #loops through each line in the data file
        line_data = [] # temporarily stores a single line from the text file 
        points = line.split(",") # splits the entire line of numbers/words separated by certain characters into individual elements.
        
        for singlePoint in points:
            line_data.append(float(singlePoint))
        												  # Now I go through individual elements in the line and convert them to float type and store them in line_data list. 
        
        difference = max(line_data) - min(line_data)

        peak = max(line_data)

        peak_position = line_data.index(peak)

        first_elements = line_data[:999]    

        first_elements_sum = 0.0
        for element in first_elements:
        	first_elements_sum += float(element)

        baseline = float(first_elements_sum) / 1000.0
        normalised_peak = max(line_data) - baseline


        line_parameters = {}
        line_parameters['min'] = min(line_data)
        line_parameters['max'] = peak
        line_parameters['diff'] = difference
        line_parameters['baseline'] = baseline
        line_parameters['norm_peak'] = normalised_peak
        line_parameters['noise'] = line_data[999]
        line_parameters['peak_position'] = peak_position 
        
        #Now adding code to find the pre-peak-50% value and post-peak-50% value
        half_peak = normalised_peak / 2.0

        pre_delta = 1000000.0

        for idx, sample in enumerate(line_data):
        	previous_pre_delta = pre_delta
        	pre_delta = abs(half_peak - sample)
        	if pre_delta < previous_pre_delta and idx < line_parameters['peak_position']:
        		pre_50_position = idx

        line_parameters['pre_50_position'] = pre_50_position


        #This part of the algorithm needs examining. 
        post_delta = 1000000.0
        post_delta_arr = []

        for sample in line_data:
            previous_post_delta = post_delta
            post_delta = abs(half_peak - sample)
            post_delta_arr.append(float(post_delta))


        cut_post_delta_arr = post_delta_arr[line_parameters['peak_position']:]

        post_50 = min(cut_post_delta_arr)

        post_50_position = line_parameters['peak_position'] + cut_post_delta_arr.index(post_50)

        line_parameters['post_50_position'] = post_50_position

        #Now determining FWHM from pre and post 50 positions

        width_in_sample_units = int(line_parameters['post_50_position'] - line_parameters['pre_50_position'])

        line_parameters['fwhm'] = float(width_in_sample_units) * ( 1 / sampling_frequency )

        #Now want to find area under pulse...
        #Need to establish locations of pulse_start and pulse_end || sum any bin with a value greater than the largest noise spike (~= -0.064) so set threshold at 0.07
        #todo: try to determine the accuracy of this...
        pulse_area = 0.0

        for sample in line_data:
        	if sample >= 0.07:
        		pulse_area += sample


        line_parameters['pulse_area'] = pulse_area


        print(line_parameters)
        

        output_data_file.write(str(line_parameters['noise']))
        output_data_file.write('    ')
        output_data_file.write(str(line_parameters['norm_peak']))
        output_data_file.write('    ')
        output_data_file.write(str(line_parameters['fwhm']))
        output_data_file.write('    ')
        output_data_file.write(str(line_parameters['pulse_area']))
        output_data_file.write('\n')
    
    data_file.close()
    output_data_file.close()

###########################################################################################################################

def generate_run_list(start_no, end_no):

    run_list = list(range(int(start_no), int(end_no)+1))

    return run_list


###########################################################################################################################
#Start of Program
###########################################################################################################################
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
        calculate_trace_params("../data/run" + str(run_number) + "/" + name)












      