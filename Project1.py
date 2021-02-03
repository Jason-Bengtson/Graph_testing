# -----------------------------
# CSCI 347 Data Mining
# Project 1: Exploratory Data Analysis
# For Dr. Strnadova-Neeley
#
# Jason Bengtson
# Blake Stanger
# Due 2/1/2021
# code saved in csci-347-spring2021-private
# ----------------------------

import numpy as np
import pandas as pd
import csv
import string
import matplotlib.pyplot as plt

"""
PART ONE

The data selected comes frome the Institute of Mathematics and Computer Science John Paul II Catholic University Lublin,
Poland. Information collected came from experimental fields of grain, collected with the purpose of proving new
developments in Agrophysics. This data has seven attributes, six numerical and one categorical. One-hot coding was used,
as students believed using label encoding may create an artificial relationship that does not otherwise exist in the data.
Students also recognise that using One-hot coding can lead to multicollinearity and a Variance Inflation Factor
test was performed in the code with a VIF (INSERT SCORE HERE)

One of the common ways to check for multicollinearity is the Variance Inflation Factor (VIF):

VIF=1, Very Less Multicollinearity
VIF<5, Moderate Multicollinearity
VIF>5, Extreme Multicollinearity (This is what we have to avoid)

The data does not appear to have missing values. The students selected this data for two reasons: it fell within a
goldilocks zone of not too difficult to work with, but challenging enough to learn from; Secondly the data came from an
agricultural university from almost the same latitude north as Bozeman. The to our own area and school was intriguing.

Before data analysis the AREA attribute seems to logically be the most descriptive. If the study was to provide data on
experimental wheat fields to increase yields the area seems a good descriptor as total wheat increase.

"""
"""
PART TWO
"""

def main():

    # csv file name for our Data set 
    filename = "seeds_dataset.csv"

    # just some test data
    test_one = [0.2, 0.4, 1.8, -0.5, 0.4, 1.1, 4]
    test_two = [23, 1, 0.5, 34, 19, 11, 8]
  
    # initializing the arrays for the rows and individual columns  
    fields = [] 
    rows = []

    # Each of these arrays represent individual column data for easy selection
    areaA = []
    perimeterP = []
    compactness = []
    lenofkernel = []
    widthofkernel = []
    asymmetrycoefficient = []
    lenofkernelgroove = []
    column8 =[]
  
    # reading csv file 
    with open(filename, 'r') as csvfile:
        # creating a csv reader object 
        csvreader = csv.reader(csvfile)

        # extracting field names through first row 

        fields = next(csvreader) 
  
    # Creating arrays for 'Rows' and each specific Column
        for row in csvreader: 
            rows.append(row)
            areaA.append(row[0])
            perimeterP.append(row[1])
            compactness.append(row[2]) 
            lenofkernel.append(row[3])
            widthofkernel.append(row[4])
            asymmetrycoefficient.append(row[5])
            lenofkernelgroove.append(row[6])
            column8.append(row[7])

        # printing out some general information before the main menu
        print()
        print("*****************************************") 
        print("Total no. of rows: %d"%(csvreader.line_num)) 
  
    # printing the field names 
    print('Field names are:' + ', '.join(field for field in fields)) 
    print("*****************************************")

    # Converting all our arrays into numpy floating point arrays
    xrow = np.array(rows)
    datasetrows = xrow.astype(np.float)

    area = np.array(areaA)
    dataarea = area.astype(np.float)

    perim = np.array(perimeterP)
    dataperim = perim.astype(np.float)

    comp = np.array(compactness)
    datacomp = comp.astype(np.float)

    kern = np.array(lenofkernel)
    datakern = kern.astype(np.float)

    width = np.array(widthofkernel)
    datawidth = width.astype(np.float)

    asym = np.array(asymmetrycoefficient)
    dataasym = asym.astype(np.float)

    groove = np.array(lenofkernelgroove)
    datagroove = groove.astype(np.float)

    col8 = np.array(column8)
    datacol8 = col8.astype(np.float)


    # This function is for dynamically labeling the scatter plot x and y axis
    def axis_labels(x):
        if x == '1' or x == 1:
            return "Area"
        elif x == '2' or x == 2:
            return "Perimeter"
        elif x == '3' or x == 3:
            return "Compactness"
        elif x == '4' or x == 4:
            return "Length of Kernel"
        elif x == '5' or x == 5:
            return "Width of Kernel"
        elif x == '6' or x == 6:
            return "Asymmetery Coefficient"
        elif x == '7' or x == 7:
            return "Length of Kernel Groove"
        elif x == '8' or x == 8:
            return "Type of seed"
        else:
            print("Not a valid number")
    
    # This column is for dynamically selecting which field column we want to analyze
    def col_num(x):
        if x == '1' or x == 1:
            return dataarea
        elif x == '2' or x == 2:
            return dataperim
        elif x == '3' or x == 3:
            return datacomp
        elif x == '4' or x == 4:
            return datakern
        elif x == '5' or x == 5:
            return datawidth
        elif x == '6' or x == 6:
            return dataasym
        elif x == '7' or x == 7:
            return datagroove
        elif x == '8' or x == 8:
            return datacol8
        else:
            print("Not a valid number")


    # Our main iterative selection menu
    loop_condition = True
    while loop_condition == True:
        print("\nWelcome to Python Calculator!\n")
        print("1. Multidata Mean")
        print("2. covariance between two attributes that are input as one-dimensional numpy vectors")
        print("3. compute the correlation between two attributes that are input as two numpy vectors")
        print("4. normalize the attributes in a two-dimensional numpy array using range normalization")
        print("5. normalize the attributes in a two-dimensional numpy array using standard normalization")
        print("6. compute the covariance matrix of a data set")
        print("7. label-encode a two-dimensional categorical data array that is passed in as input")
        print("8. Scatter plot of two columns")
        print("9. Range normalize and covariate")
        print("24. Total variance")
        print("10. Enter 10 to quit.\n")
        print("72. Enter 72 to z_score")

        main_input = int(input("What would you like to do? "))

        # This print out shows what the different column numbers represent in regards to our data.
        print("Column 1 = Area A  Column 2 = Perimeter P  Column 3 = Compactness Cloumn 4 = Length of Kernel")
        print("Column 5 = Width of Kernel  Column 6 = Asymmetery Coeff.  Column 7 = Length of Kernel Groove")
        print("Column 8 = Categorical")

        if main_input == 10:
            print("Every meeting must have a parting")
            loop_condition = False
            break
        else:
            # This if statement calls the mean function to compute each column mean, then appends them to an array
            # and prints out the result as the multivariate mean
            if main_input == 1:
                multivariate_mean = []
                for i in range(8):
                    col = col_num(i+1)
                    mean = multi_data_mean(col)
                    multivariate_mean.append(mean)
                print(multivariate_mean)

            elif main_input == 2:
                # This elif allows the user to dynamically select which two columns they want to compare, then sends
                # the selections to covariance_1D_vectors function, it then prints the result.
                a = input("Please enter the first column number:")
                col1 = col_num(a)
                b = input("Please enter the second column number:")
                col2 = col_num(b)
                cov = covariance_1D_vectors(col1, col2)
                print()
                print("The covariance is:",  cov)

            elif main_input == 3:
                # This elif prompts the user to dynamically choose which two columns they want to analyze, then sends
                # the selections to correlation_two_numpy_vectors to be calculated
                a = input("Please enter the first column number:")
                col1 = col_num(a)
                b = input("Please enter the second column number:")
                col2 = col_num(b)
                correlation_two_numpy_vectors(col1, col2)

            elif main_input == 4:
                # This elif allows the user to dynamically choose which two columns they wish to analyze, then sends
                # the selections to range_normalize_2D_numpy_array along with the length of one of the columns
                a = input("Please enter the first column number:")
                col1 = col_num(a)
                b = input("Please enter the second column number:")
                col2 = col_num(b)
                length = len(col1)
                print(length)
                col = []
                col.append(col1)
                col.append(col2)
                range_normalize_2D_numpy_array(col, length)

            elif main_input == 5:
                # This elif allows the user to dynamically choose which two columns they wish to analyze, then sends
                # the selections to standard_normalize_2D_numpy_array along with the length of one of the columns
                a = input("Please enter the first column number:")
                col1 = col_num(a)
                b = input("Please enter the second column number:")
                col2 = col_num(b)
                length = len(col1)
                print(length)
                col = []
                col.append(col1)
                col.append(col2)
                #print(col)
                standard_normalize_2D_numpy_array(col, length)

            elif main_input == 6:
                # This elif simply sends every column to covariance_1D vectors then appends the results to form and 
                # print the covariance matrix So this is essentially our covariance matrix function. With how the 
                # program was initially set up this was the easiest way to calculate it.
                print("_________________________Covariance Matrix_________________________")
            
                for i in range(8):
                    row = []
                    for j in range(8):
                        row.append(covariance_1D_vectors(col_num(i+1),col_num(j+1)))
                    print(row)    
                    
                print("___________________________________________________________________")
                
            elif main_input == 7:
                # This elif is simply for label encoding our one categorical column, so it is currently hard coded 
                # to send column 8 to the label_encode_2D_cat_array function
                label_encode_2D_cat_array(col_num(8))
            
            elif main_input == 8:
                # This elif is for dynamically making scatter plots of our data. The user can select which two columns
                # they wish to compare and it will label and produce scatter plots. Note that you sometimes have to run
                # the options twice for it to produce the proper plot. It will then print out the plot for the previously 
                # selected two columns (we have no idea why it does this)
                a = input("Please enter the first column number:")
                col1 = col_num(a)
                col1_label = axis_labels(a)
                b = input("Please enter the second column number:")
                col2 = col_num(b)
                col2_label = axis_labels(b)
                scatter_plot(col1, col2, col1_label, col2_label)

                
            elif main_input == 9:
                # This elif is for the range_normal_covariance, the user can dynamically select which columns they want to analyze
                # then sends that information to the range_normal_covariance function along with the length of one of the columns
                a = input("Please enter the first column number:")
                col1 = col_num(a)
                b = input("Please enter the second column number:")
                col2 = col_num(b)
                length = len(col1)
                print(length)
                col = []
                col.append(col1)
                col.append(col2)
                range_normal_covariance(col, length)
                
            elif main_input == 24:
                # This calculates the Total variance of our data. The entire calculation is done below, where we calculate
                # each column individually then sum the answers up. We also appended each answer to an array so we could
                # easily see the variance of each individual column
                total_var = []
                total = 0
                for i in range(8):
                    varsum = 0
                    mean = multi_data_mean(col_num(i+1))
                    length = len(col_num(i+1))
                    for j in col_num(i+1):
                        varsum += (j-mean)**2
                    print("Varsum: " , varsum)
                    print("Length: ", length)
                    col_variance = round(varsum/(length-1),3)
                    print("col_variance: " , col_variance)
                    total_var.append(col_variance)
                    total += col_variance
                print("Total Variance: ", total)

            # This selection calculates the z-score in the function below
            elif main_input == 72:
                z_score(test_one, test_two)

            else:
                print("Wrong-o not a valid input")


# A function that will compute the mean of a numerical, multidimensional data set input as a 2-dimensional numpy array

def multi_data_mean(array_to_compute):

    sum = 0
    for l in range(len(array_to_compute)):
        sum += array_to_compute[l]

    a = float(sum / len(array_to_compute))

    mean = round(a, 3)
    return mean


# A function that will compute the sample covariance between two attributes that are input as one-dimensional numpy vectors
def covariance_1D_vectors(vector1, vector2):
    #print(vector1)
    #print(vector2)
    if len(vector1) != len(vector2):
        print("These attributes don't have the same length")
        return
    vector1_total = 0
    for l in vector1:
        vector1_total += l
    vector1_mean = float(vector1_total / len(vector1))
    vector2_total = 0
    for l in vector2:
        vector2_total += l
    vector2_mean = float(vector2_total / len(vector2))

    covariance_col_variance = 0
    v1 = vector1.tolist()
    v2 = vector2.tolist()
    for l, n in zip(v1, v2):
        covariance_col_variance += (l - vector1_mean) * (n - vector2_mean)

    rounded_cov_col_variance = round(covariance_col_variance, 3)
    #print(covariance_col_variance)
    return(rounded_cov_col_variance)

# cite your sources https://stackoverflow.com/questions/15317822/calculating-covariance-with-python-and-numpy


# A function that will compute the correlation between two attributes that are input as two numpy vectors.
def correlation_two_numpy_vectors(vector1, vector2):

    #print("\nMade it into correlation_two_numpy_vectors")

    if len(vector1) != len(vector2):
        print("These attributes don't have the same length")
        return
    vector1_total = 0
    for l in vector1:
        vector1_total += l
    vector1_mean = round(float(vector1_total / len(vector1)),2)
    # print("vector one mean")
    # print(vector1_mean)
    vector2_total = 0
    for l in vector2:
        vector2_total += l
    vector2_mean = float(vector2_total / len(vector2))
    # print("vector 2 mean")
    # print(vector2_mean)
    # print(vector2_mean)
    # print(vector1_mean)
    covariance = 0
    for l in range(len(vector1)):
        covariance += (vector1[l] - vector1_mean) * (vector2[l] - vector2_mean)

    sigma_vector_1 = 0
    for l in range(len(vector1)):
        sigma_vector_1 += (vector1[l]-vector1_mean)**2 # add square


    sigma_vector_2 = 0
    for l in range(len(vector2)):
        sigma_vector_2 += (vector2[l]-vector2_mean)**2 #add square
        #print(sigma_vector_2)

    # print('sigma vector 1')
    # print(sigma_vector_1)
    #
    # print('sigma vector 2')
    # print(sigma_vector_2)

    sigma_vector_1 = sigma_vector_1**.5 * (1 / (len(vector1) - 1))  # take the square root here of sigma _vector1
    sigma_vector_2 = sigma_vector_2**.5 * (1 / (len(vector2) - 1))  # same as above

    covariance = covariance * (1 / (len(vector1)-1))


    print("length")
    print(len(vector1)-1)


    covariance = round(covariance /(sigma_vector_2*sigma_vector_1), 2)

    #print(covariance)
    return covariance

# A function that will normalize the attributes in a two-dimensional numpy array using range normalization
def range_normalize_2D_numpy_array(array, length):
    print("\nMade it into range_normalize_2D_numpy_array")

    large_one_first = array[0][0]
    zmall_one_first = array[0][0]

    large_one_second = array[1][0]
    zmall_one_second = array[1][0]

    for i in range(2):
        for j in range(length):

            # print(i)
            # print(j)
            if array[i][j] >= large_one_first and i == 0:
                large_one_first = array[i][j]

            if array[i][j] >= large_one_second and i == 1:
                large_one_second = array[i][j]

            if array[i][j] <= zmall_one_first and i == 0:
                zmall_one_first = array[i][j]

            if array[i][j] <= zmall_one_second and i == 1:
                zmall_one_second = array[i][j]

    print(array)
    #print(large_one_first)
    #print(large_one_second)
    #print(zmall_one_first)
    #print(zmall_one_second)
    range_one = large_one_first-zmall_one_first
    range_two = large_one_second-zmall_one_second
    range_normalized_array = [[0 for x in range(length)] for y in range(2)]

    for i in range(2):
        for j in range(length):
            if(i==0):
                range_normalized_array[i][j] = round(array[i][j]-range_one, 3)
            if(i==1):
                range_normalized_array[i][j] = round(array[i][j] - range_two, 3)
    print(range_one)
    print(range_two)
    print(range_normalized_array)

# A function that will normalize the attributes in a two-dimensional numpy array using standard normalization.
def standard_normalize_2D_numpy_array(array, length):
    print("\nMade it into standard_normalize_2D_numpy_array")

    large_one_first = array[0][0]
    zmall_one_first = array[0][0]

    large_one_second = array[1][0]
    zmall_one_second = array[1][0]

    for i in range(2):
        for j in range(length):
            # print(i)
            # print(j)
            if array[i][j] >= large_one_first and i == 0:
                large_one_first = array[i][j]
            if array[i][j] >= large_one_second and i == 1:
                large_one_second = array[i][j]
            if array[i][j] <= zmall_one_first and i == 0:
                zmall_one_first = array[i][j]
            if array[i][j] <= zmall_one_second and i == 1:
                zmall_one_second = array[i][j]
    print(array)
    # print(large_one_first)
    # print(large_one_second)
    # print(zmall_one_first)
    # print(zmall_one_second)
    range_one = large_one_first-zmall_one_first
    range_two = large_one_second-zmall_one_second
    standard_normalized_array = [[0 for x in range(length)] for y in range(2)]
    for i in range(2):
        for j in range(length):
            if(i==0):
                standard_normalized_array[i][j] = round((array[i][j]-zmall_one_first)/(large_one_first-zmall_one_first),3)
            if(i==1):
                standard_normalized_array[i][j] = round((array[i][j] - zmall_one_second)/(large_one_second-zmall_one_second),3)
    print(range_one)
    print(range_two)
    print(standard_normalized_array)

# A function that will compute the covariance matrix of a data set.
def compute_covariance_matrix(matrix):

    print(matrix)

# A function that will label-encode a two-dimensional categorical data array that is passed in as input.

def label_encode_2D_cat_array(catigorical_array):

    encoded_array = []
    #print(catigorical_array)
    for i in catigorical_array:
        #print(i)
        if i == 'A':
            encoded_array.append(1.0)
        elif i == 'B':
            encoded_array.append(2.0)
        elif i == 'C':
            encoded_array.append(3.0)
        else:
            encoded_array.append(i)
    print(encoded_array)
    return encoded_array

# function for dynamically printing out scatter plots with labels
def scatter_plot(x, y, x_label, y_label):
    print()
    print("Made it into the scatter plot function")

    print(x_label)
    print(y_label)

    fig=plt.figure()
    ax=fig.add_axes([0,0,1,1])
    ax.scatter(x, y, color='b')
    plt.show()
    
    plt.scatter(x,y)
    plt.title(x_label + ' and ' + y_label + ' Scatter Plot')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show
    
# function for finding our range normalized covariance
def range_normal_covariance(array, length):

   large_one_first = array[0][0]
   zmall_one_first = array[0][0]

   large_one_second = array[1][0]
   zmall_one_second = array[1][0]

   for i in range(2):
       for j in range(length):
           #print(i)
           #print(j)
           if array[i][j] >= large_one_first and i == 0:
               large_one_first = array[i][j]
           if array[i][j] >= large_one_second and i == 1:
               large_one_second = array[i][j]
           if array[i][j] <= zmall_one_first and i == 0:
               zmall_one_first = array[i][j]
           if array[i][j] <= zmall_one_second and i == 1:
               zmall_one_second = array[i][j]
   #print(array)
    #print(large_one_first)
    #print(large_one_second)
    #print(zmall_one_first)
    #print(zmall_one_second)
   range_one = large_one_first-zmall_one_first
   range_two = large_one_second-zmall_one_second
   range_normalized_array = [[0 for x in range(length)] for y in range(2)]
   col1 = []
   col2 = []
   for i in range(2):
       for j in range(length):
           if(i==0):
               range_normalized_array[i][j] = round(array[i][j]-range_one, 3)
               col1.append(round(array[i][j]-range_one, 3))
           if(i==1):
               range_normalized_array[i][j] = round(array[i][j] - range_two, 3)
               col2.append(round(array[i][j] - range_two, 3))
   #print(range_one)
   #print(range_two)
   #print(range_normalized_array)
   #print("Col one: " , col1)
   #print("Col two: " , col2)
   column1 = np.array(col1)
   column_1 = column1.astype(np.float)

   column2 = np.array(col2)
   column_2 = column2.astype(np.float)

   cov = covariance_1D_vectors(column_1, column_2)
   print("The covariance is:",  cov)

# function for finding our zscores
def z_score(test_one, test_two):

    #area and perimeter

    area_array = [0.441, 0.405, 0.349, 0.307, 0.524, 0.358, 0.387, 0.332, 0.57, 0.552, 0.441, 0.325, 0.312, 0.301, 0.297, 0.378,
      0.321, 0.482, 0.388, 0.201, 0.337, 0.332, 0.5, 0.141, 0.417, 0.529, 0.229, 0.203, 0.332, 0.27, 0.243, 0.463,
      0.331, 0.316, 0.421, 0.522, 0.53, 0.613, 0.398, 0.348, 0.279, 0.275, 0.243, 0.464, 0.427, 0.303, 0.45, 0.415,
      0.397, 0.403, 0.363, 0.49, 0.368, 0.353, 0.371, 0.419, 0.365, 0.409, 0.452, 0.144, 0.078, 0.06, 0.167, 0.248,
      0.207, 0.216, 0.354, 0.323, 0.357, 0.202, 0.665, 0.59, 0.63, 0.805, 0.588, 0.584, 0.636, 0.956, 0.788, 0.617,
      0.561, 0.768, 0.907, 0.848, 0.842, 0.725, 0.783, 0.792, 1.0, 0.972, 0.898, 0.771, 0.776, 0.755, 0.734, 0.593,
      0.823, 0.792, 0.716, 0.768, 0.55, 0.699, 0.838, 0.811, 0.789, 0.778, 0.78, 0.665, 0.883, 0.752, 0.742, 0.83,
      0.806, 0.807, 0.98, 0.8, 0.79, 0.808, 0.784, 0.891, 0.911, 0.713, 0.527, 0.74, 0.51, 0.771, 0.761, 0.698, 0.904,
      0.657, 0.728, 0.788, 0.452, 0.526, 0.469, 0.452, 0.639, 0.47, 0.473, 0.533, 0.234, 0.258, 0.26, 0.154, 0.116,
      0.059, 0.079, 0.179, 0.199, 0.019, 0.117, 0.134, 0.158, 0.056, 0.073, 0.057, 0.071, 0.145, 0.11, 0.085, 0.184,
      0.135, 0.138, 0.185, 0.052, 0.143, 0.175, 0.147, 0.072, 0.061, 0.041, 0.091, 0.064, 0.076, 0.023, 0.02, 0.063,
      0.014, 0.084, 0.153, 0.077, 0.177, 0.151, 0.1, 0.217, 0.092, 0.115, 0.03, 0.06, 0.0, 0.032, 0.064, 0.121, 0.022,
      0.144, 0.209, 0.208, 0.263, 0.192, 0.205, 0.169, 0.196, 0.056, 0.199, 0.168, 0.151, 0.06, 0.246, 0.118, 0.161]

    area_array = np.array(area_array)

    perimiter_array = [0.502, 0.446, 0.347, 0.316, 0.533, 0.372, 0.43, 0.349, 0.63, 0.587, 0.504, 0.362, 0.333, 0.341, 0.339, 0.386,
      0.293, 0.483, 0.372, 0.24, 0.411, 0.382, 0.514, 0.169, 0.486, 0.568, 0.279, 0.26, 0.366, 0.333, 0.291, 0.523,
      0.413, 0.364, 0.469, 0.535, 0.591, 0.614, 0.436, 0.364, 0.298, 0.298, 0.236, 0.506, 0.44, 0.337, 0.486, 0.444,
      0.436, 0.467, 0.411, 0.517, 0.455, 0.386, 0.452, 0.488, 0.401, 0.417, 0.488, 0.219, 0.093, 0.045, 0.161, 0.295,
      0.24, 0.225, 0.405, 0.388, 0.409, 0.277, 0.738, 0.674, 0.686, 0.795, 0.64, 0.663, 0.723, 0.996, 0.843, 0.649,
      0.605, 0.781, 0.926, 0.895, 0.888, 0.76, 0.795, 0.878, 0.992, 0.959, 0.946, 0.783, 0.802, 0.752, 0.849, 0.669,
      0.864, 0.86, 0.795, 0.812, 0.587, 0.713, 0.845, 0.872, 0.829, 0.802, 0.777, 0.713, 0.932, 0.787, 0.767, 0.89,
      0.806, 0.868, 1.0, 0.835, 0.783, 0.835, 0.789, 0.928, 0.93, 0.767, 0.614, 0.736, 0.512, 0.779, 0.826, 0.711,
      0.955, 0.671, 0.719, 0.808, 0.514, 0.603, 0.512, 0.465, 0.692, 0.566, 0.558, 0.572, 0.312, 0.316, 0.318, 0.188,
      0.205, 0.149, 0.149, 0.217, 0.269, 0.107, 0.169, 0.229, 0.246, 0.13, 0.132, 0.132, 0.095, 0.273, 0.229, 0.167,
      0.26, 0.19, 0.207, 0.24, 0.079, 0.153, 0.244, 0.215, 0.147, 0.122, 0.122, 0.143, 0.116, 0.138, 0.114, 0.033,
      0.124, 0.066, 0.132, 0.219, 0.112, 0.207, 0.196, 0.136, 0.281, 0.186, 0.215, 0.081, 0.085, 0.0, 0.081, 0.093,
      0.126, 0.087, 0.178, 0.219, 0.231, 0.283, 0.26, 0.2, 0.213, 0.188, 0.064, 0.207, 0.219, 0.163, 0.097, 0.258,
      0.165, 0.192]

    perimiter_array = np.array(perimiter_array)

    compactness= [0.571, 0.662, 0.879, 0.793, 0.865, 0.789, 0.652, 0.753, 0.604, 0.725, 0.558, 0.649, 0.725, 0.615, 0.602, 0.828, 1.0, 0.887, 0.973, 0.549, 0.456, 0.582, 0.823, 0.529, 0.523, 0.697, 0.508, 0.438, 0.671, 0.475, 0.527, 0.583, 0.407, 0.587, 0.633, 0.834, 0.593, 0.906, 0.673, 0.783, 0.717, 0.7, 0.842, 0.671, 0.821, 0.647, 0.708, 0.728, 0.67, 0.54, 0.608, 0.764, 0.415, 0.681, 0.432, 0.524, 0.669, 0.839, 0.704, 0.282, 0.546, 0.689, 0.764, 0.544, 0.576, 0.724, 0.585, 0.494, 0.585, 0.342, 0.537, 0.492, 0.619, 0.907, 0.64, 0.505, 0.47, 0.619, 0.607, 0.736, 0.673, 0.813, 0.738, 0.633, 0.634, 0.716, 0.806, 0.462, 0.824, 0.862, 0.603, 0.819, 0.749, 0.894, 0.337, 0.515, 0.666, 0.55, 0.505, 0.662, 0.712, 0.827, 0.82, 0.577, 0.679, 0.759, 0.885, 0.652, 0.609, 0.711, 0.762, 0.576, 0.866, 0.582, 0.706, 0.701, 0.904, 0.734, 0.841, 0.662, 0.74, 0.627, 0.46, 0.904, 0.892, 0.833, 0.56, 0.828, 0.593, 0.826, 0.932, 0.781, 0.567, 0.511, 0.673, 0.825, 0.639, 0.405, 0.453, 0.698, 0.362, 0.483, 0.489, 0.518, 0.175, 0.078, 0.23, 0.524, 0.372, 0.024, 0.377, 0.152, 0.229, 0.168, 0.273, 0.156, 0.467, 0.0, 0.001, 0.165, 0.312, 0.383, 0.304, 0.433, 0.433, 0.646, 0.346, 0.328, 0.191, 0.252, 0.098, 0.339, 0.307, 0.267, 0.016, 0.462, 0.249, 0.225, 0.356, 0.338, 0.435, 0.567, 0.452, 0.448, 0.417, 0.106, 0.106, 0.264, 0.466, 0.515, 0.28, 0.437, 0.648, 0.159, 0.506, 0.707, 0.64, 0.697, 0.363, 0.801, 0.479, 0.813, 0.544, 0.72, 0.441, 0.637, 0.39, 0.728, 0.399, 0.547]

    compactness = np.array(compactness)

    length_of_kernel = [0.486, 0.369, 0.221, 0.239, 0.427, 0.274, 0.374, 0.293, 0.65, 0.555, 0.459, 0.303, 0.304, 0.327, 0.328, 0.255, 0.124, 0.354, 0.172, 0.184, 0.427, 0.35, 0.405, 0.113, 0.501, 0.526, 0.279, 0.279, 0.361, 0.347, 0.312, 0.483, 0.461, 0.386, 0.458, 0.456, 0.522, 0.525, 0.426, 0.28, 0.253, 0.255, 0.135, 0.551, 0.383, 0.269, 0.452, 0.378, 0.364, 0.439, 0.386, 0.436, 0.459, 0.341, 0.474, 0.452, 0.275, 0.273, 0.43, 0.146, 0.061, 0.002, 0.1, 0.279, 0.204, 0.135, 0.412, 0.4, 0.377, 0.289, 0.727, 0.619, 0.608, 0.707, 0.63, 0.579, 0.656, 0.946, 0.87, 0.535, 0.55, 0.623, 0.78, 0.836, 0.826, 0.717, 0.667, 0.929, 0.943, 0.873, 0.947, 0.717, 0.773, 0.641, 0.995, 0.698, 0.812, 0.873, 0.773, 0.743, 0.461, 0.558, 0.684, 0.828, 0.76, 0.641, 0.706, 0.639, 1.0, 0.706, 0.68, 0.791, 0.723, 0.766, 0.937, 0.854, 0.649, 0.758, 0.748, 0.898, 0.797, 0.653, 0.486, 0.609, 0.261, 0.682, 0.78, 0.608, 0.909, 0.502, 0.608, 0.701, 0.555, 0.533, 0.494, 0.325, 0.702, 0.575, 0.525, 0.548, 0.323, 0.361, 0.276, 0.183, 0.234, 0.214, 0.156, 0.207, 0.274, 0.235, 0.205, 0.285, 0.287, 0.181, 0.155, 0.198, 0.087, 0.279, 0.307, 0.228, 0.311, 0.254, 0.207, 0.244, 0.063, 0.116, 0.236, 0.292, 0.156, 0.108, 0.24, 0.151, 0.106, 0.133, 0.213, 0.046, 0.162, 0.139, 0.158, 0.258, 0.108, 0.19, 0.192, 0.118, 0.336, 0.261, 0.289, 0.106, 0.107, 0.0, 0.083, 0.108, 0.131, 0.158, 0.19, 0.147, 0.183, 0.237, 0.288, 0.098, 0.18, 0.048, 0.062, 0.16, 0.172, 0.134, 0.136, 0.19, 0.155, 0.194]

    length_of_kernel = np.array(length_of_kernel)

    width = [0.486, 0.501, 0.504, 0.534, 0.664, 0.486, 0.448, 0.479, 0.595, 0.624, 0.436, 0.407, 0.406, 0.375, 0.345, 0.501, 0.537, 0.63, 0.596, 0.299, 0.356, 0.383, 0.625, 0.218, 0.438, 0.564, 0.282, 0.232, 0.421, 0.31, 0.246, 0.528, 0.396, 0.371, 0.498, 0.609, 0.594, 0.751, 0.469, 0.476, 0.375, 0.376, 0.407, 0.546, 0.593, 0.374, 0.544, 0.532, 0.471, 0.448, 0.458, 0.573, 0.344, 0.406, 0.344, 0.415, 0.532, 0.557, 0.562, 0.287, 0.157, 0.177, 0.294, 0.314, 0.282, 0.349, 0.399, 0.376, 0.373, 0.18, 0.664, 0.609, 0.687, 0.927, 0.61, 0.576, 0.551, 0.844, 0.719, 0.667, 0.597, 0.875, 0.88, 0.814, 0.835, 0.728, 0.808, 0.741, 1.0, 0.999, 0.823, 0.831, 0.758, 0.877, 0.609, 0.594, 0.841, 0.657, 0.629, 0.751, 0.638, 0.758, 0.9, 0.749, 0.802, 0.824, 0.838, 0.672, 0.808, 0.744, 0.812, 0.828, 0.907, 0.789, 0.97, 0.776, 0.903, 0.845, 0.812, 0.875, 0.949, 0.665, 0.54, 0.813, 0.679, 0.883, 0.687, 0.753, 0.815, 0.756, 0.802, 0.852, 0.455, 0.545, 0.555, 0.595, 0.673, 0.428, 0.468, 0.6, 0.259, 0.316, 0.316, 0.24, 0.105, 0.041, 0.063, 0.24, 0.2, 0.013, 0.15, 0.104, 0.145, 0.045, 0.089, 0.032, 0.156, 0.082, 0.034, 0.046, 0.177, 0.128, 0.155, 0.241, 0.117, 0.222, 0.19, 0.148, 0.027, 0.061, 0.051, 0.153, 0.095, 0.095, 0.008, 0.136, 0.057, 0.009, 0.091, 0.187, 0.103, 0.276, 0.199, 0.157, 0.282, 0.038, 0.061, 0.032, 0.136, 0.112, 0.062, 0.124, 0.23, 0.0, 0.246, 0.354, 0.302, 0.355, 0.2, 0.374, 0.256, 0.36, 0.128, 0.329, 0.235, 0.25, 0.118, 0.429, 0.147, 0.245]

    width = np.array(length_of_kernel)

    assemetry = [0.189, 0.033, 0.251, 0.194, 0.077, 0.221, 0.367, 0.252, 0.166, 0.157, 0.491, 0.124, 0.419, 0.308, 0.282, 0.445, 0.581, 0.108, 0.13, 0.434, 0.3, 0.25, 0.0, 0.085, 0.133, 0.018, 0.339, 0.226, 0.259, 0.36, 0.012, 0.344, 0.41, 0.177, 0.177, 0.196, 0.268, 0.285, 0.305, 0.77, 0.237, 0.193, 0.221, 0.513, 0.307, 0.103, 0.078, 0.285, 0.252, 0.177, 0.417, 0.628, 0.436, 0.333, 0.093, 0.152, 0.265, 0.049, 0.16, 0.096, 0.252, 0.196, 0.319, 0.441, 0.053, 0.206, 0.071, 0.189, 0.091, 0.36, 0.43, 0.508, 0.491, 0.282, 0.421, 0.54, 0.398, 0.479, 0.559, 0.272, 0.62, 0.593, 0.573, 0.092, 0.286, 0.218, 0.115, 0.38, 0.652, 0.553, 0.155, 0.306, 0.321, 0.681, 0.542, 0.381, 0.353, 0.179, 0.271, 0.185, 0.449, 0.169, 0.461, 0.337, 0.338, 0.232, 0.27, 0.388, 0.323, 0.127, 0.191, 0.379, 0.175, 0.769, 0.509, 0.193, 0.464, 0.302, 0.374, 0.299, 0.668, 0.371, 0.458, 0.289, 0.334, 0.445, 0.471, 0.194, 0.149, 0.598, 0.269, 0.279, 0.481, 0.455, 0.547, 0.369, 0.359, 0.244, 0.255, 0.391, 0.59, 0.815, 0.68, 0.612, 0.482, 0.703, 0.189, 0.475, 0.324, 0.611, 0.576, 0.81, 0.519, 0.334, 0.427, 0.656, 0.336, 0.528, 0.47, 0.601, 0.301, 0.456, 0.549, 0.475, 0.731, 0.187, 0.541, 0.374, 0.464, 0.358, 0.776, 0.774, 0.461, 0.627, 0.574, 0.521, 0.594, 0.512, 0.665, 0.116, 0.545, 0.549, 0.532, 0.578, 0.705, 0.429, 0.537, 0.444, 0.879, 0.547, 0.602, 0.419, 0.368, 0.532, 0.438, 0.534, 0.613, 0.508, 0.33, 0.268, 0.612, 0.2, 0.427, 1.0, 0.41, 0.373, 0.463, 0.982, 0.368, 0.633]

    assemetry = np.array(assemetry)



    print("test one and two ")
    correlation_two_numpy_vectors(test_one, test_two)


    print("area and perimeter")
    #scatter_plot(area_array,perimiter_array, "area", "perimeter")
    correlation_two_numpy_vectors(area_array, perimiter_array)
    print("")

    print("permeter and compactness")
    #scatter_plot(perimiter_array, compactness, "perimeter", "compactness")
    correlation_two_numpy_vectors(perimiter_array, compactness)
    print("")

    print("compactness and length_of_kernel")
    #scatter_plot(compactness, length_of_kernel, "compactness", "length_of_kernel")
    correlation_two_numpy_vectors(compactness, length_of_kernel)
    print("")

    print("length_of_kernel and width")
    scatter_plot(length_of_kernel, width, "length_of_kernel", "width")
    correlation_two_numpy_vectors(length_of_kernel, width)
    print("")

    print("width and assemetry")
    scatter_plot(width, assemetry, "width", "assemetry")
    correlation_two_numpy_vectors(width, assemetry)
    print("")


main()
"""
PART THREE 
CHANGES
All Categorical attributes one-hot encoded? TRUE
No missing values or missing values replaced? TRUE

Multi-Variate Mean: We used our first function [14.848, 14.559, 0.871, 5.629, 3.259, 3.7, 5.408, 2.0]

What is the multivariate mean of the numerical data matrix (where categorical data have been converted to numerical values)?

Multi-Variate Mean: The first function was used to discover the multivariate mean [14.848, 14.559, 0.871, 5.629, 3.259, 3.7, 5.408, 2.0]
The data was rounded to three decimal places. 

What is the covariance matrix of the numerical data matrix (where categorical data have been converted to numerical values)?
The sixth function was used to create the covariance matrix of the data. See Figure One, Covariance matrix

Figure One, Covariance matrix:
_________________________Covariance Matrix_________________________
[1769.467, 789.695, 8.741, 255.963, 222.984, -209.91, 258.143, -172.24]
[789.695, 356.455, 3.413, 117.597, 97.408, -89.194, 119.496, -73.25]
[8.741, 3.413, 0.117, 0.805, 1.421, -2.461, 0.551, -2.146]
[255.963, 117.597, 0.805, 41.028, 30.094, -23.887, 42.453, -19.498]
[222.984, 97.408, 1.421, 30.094, 29.818, -30.627, 29.065, -27.36]
[-209.91, -89.194, -2.461, -23.887, -30.627, 472.483, -1.711, 148.47]
[258.143, 119.496, 0.551, 42.453, 29.065, -1.711, 50.485, 2.043]
[-172.24, -73.25, -2.146, -19.498, -27.36, 148.47, 2.043, 140.0]
___________________________________________________________________

Choose 5 pairs of attributes that you think could be related. Create scatter plots of all 5 pairs and include these in your 
report, along with a description and analysis that summarizes why these pairs of attributes might be related, 
and how the scatter plots do or do not support this intuition.

Attributes were chosen as follows: pair one area and perimeter; pair two perimeter and compactness; pair three compactness and length of kernel;
pair four length of kernel and width of kernel; pair five width of kernel and asymmetry coeff.

Which range-normalized numerical attributes have the greatest sample covariance? What is their sample covariance? 

# TODO range normalize all attributes
feed those to the covariance functions
hold and check all covariance 
list covariace


Create a scatter plot of these range-normalized attributes.



Which Z-score-normalized numerical attributes have the greatest correlation? 
What is their correlation?
Create a scatter plot of these Z-score-normalized attributes. 
Which Z-score-normalized numerical attributes have the smallest correlation? What is their correlation? 
Create a scatter plot of these Z-score-normalized attributes.
How many pairs of features have correlation greater than or equal to 0.5?
How many pairs of features have negative sample covariance?
What is the total variance of the data?
What is the total variance of the data, restricted to the five features that have the greatest sample variance?

"""

"""
Citations

https://www.analyticsvidhya.com/blog/2020/03/one-hot-encoding-vs-label-encoding-using-scikit-learn/

"""
