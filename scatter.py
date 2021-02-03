import numpy as np
import pandas as pd
import csv
import string
import matplotlib.pyplot as plt


def main():


    filename = "scatter.csv"

    # initializing the arrays for the rows and individual columns  
    fields = [] 
    rows = []

    # Each of these arrays represent individual column data for easy selection
    dtype = []
    duration = []
    source_bytes = []
    dst_bytes = []


    with open(filename, 'r') as csvfile:
        # creating a csv reader object 
        csvreader = csv.reader(csvfile)

        # extracting field names through first row 

        fields = next(csvreader) 
  
    # Creating arrays for 'Rows' and each specific Column
        for row in csvreader: 
            rows.append(row)
            duration.append(row[0])
            source_bytes.append(row[4])
            dst_bytes.append(row[5])
            dtype.append(row[41])



    dur = np.array(duration)
    datasetdur = dur.astype(np.float)

    src_bytes = np.array(source_bytes)
    datasetsrc_bytes = src_bytes.astype(np.float)

    dest_bytes = np.array(dst_bytes)
    datasetdst_bytes = dest_bytes.astype(np.float)

    length = len(dtype)

    normal_dur = []
    anomalous_dur = []

    normal_src = []
    anomalous_src = []

    normal_dest = []
    anomalous_dest = []

    for i in range(length):
        if dtype[i] == 'normal':
            normal_dur.append(duration[i])
            normal_src.append(source_bytes[i])
            normal_dest.append(dst_bytes[i])
        else:
            anomalous_dur.append(duration[i])
            anomalous_src.append(duration[i])
            anomalous_dest.append(duration[i])




    # Our main iterative selection menu
    loop_condition = True
    while loop_condition == True:
        print("\nScatter Plot\n")
        print("1. Compare duration and source")
        print("2. Compare duration and destination")
        print("3. Compare source and destination")
        print("4. Choose which to compare")
        print("5. Quit")



        main_input = int(input("What would you like to do? "))
        if main_input == 5:
            print("Every meeting must have a parting")
            loop_condition = False
            break

        else:
            # Duration and source
            if main_input == 1:
                scatter_plot(normal_dur, anomalous_dur, normal_src, anomalous_src, "Duration", "Source Bytes")
        
            elif main_input == 2:
                scatter_plot(normal_dur, anomalous_dur, normal_dest, anomalous_dest, "Duration", "Destination Bytes")
        
            elif main_input == 3:
                scatter_plot(normal_src, anomalous_src, normal_dest, anomalous_dest, "Source Bytes", "Destination Bytes")

            elif main_input == 4:
                normal_a = []
                normal_b = []
                anom_a = []
                anom_b = []

                count = 1
                for i in fields:
                    print(count , i)
                    count += 1
                a = input("Please enter the first column number:")
                for i in rows:
                    if i[41] == 'normal':
                        normal_a.append(i[int(a)])
                    else:
                        anom_a.append(i[int(a)])
                print("normal:", normal_a)
                print("Anom: ", anom_a)
                xname = fields[(int(a)+1)]
                b = input("Please enter the second column number:")
                for j in rows:
                    if j[41] == 'normal':
                        normal_b.append(j[int(b)])
                    else:
                        anom_b.append(j[int(b)])
                yname = fields[(int(b)+1)]
                w = np.array(normal_a)
                x = np.array(anom_a)
                y = np.array(normal_b)
                z = np.array(anom_b)

                scatter_plot(w,x,y,z, xname, yname)

    # xrow = np.array(rows)
    # datasetrows = xrow.astype(np.float)
    #print(fields)
    #print()
    #print(dtype)
    

def scatter_plot(w, x, y, z, x_label, y_label):
    print()
    print("Made it into the scatter plot function")

    print(x_label)
    print(y_label)

    fig=plt.figure()
    #ax=fig.add_axes([0,0,1,1])
    # ax.scatter(x, y, color='b')
    # plt.show()
    
    plt.scatter(w,y, color='r')
    plt.scatter(x,z, color='b')
    plt.title(x_label + ' and ' + y_label + ' Scatter Plot')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks([])
    plt.yticks([])
    plt.show()

    #fig=plt.figure()
    #ax=fig.add_axes([0,0,1,1])
    #ax.scatter(w, y, color='r')
    #ax.scatter(x, z, color='b')
    #ax.set_xlabel("x_label")
    #ax.set_ylabel("y_label")
    #ax.set_title('scatter plot')
    #plt.show()







main()





