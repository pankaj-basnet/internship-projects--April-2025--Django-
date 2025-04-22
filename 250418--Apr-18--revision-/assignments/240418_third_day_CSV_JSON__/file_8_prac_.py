import csv

filename_of_csv = 'ass8.csv'
def calculate_average_coding_time():

    try:
        with open(filename_of_csv, 'r', newline='') as file:
            reader = csv.DictReader(file)
            days_of_coding = list(reader)


            print(days_of_coding)

            print("--------")
            sum_of_dur = 0

            list_dur = [(float((ii.get("coding_duration"))[:2]) )for ii in days_of_coding] 
            print(list_dur)
            print(list_dur[1], type(list_dur[1]))
            print("-----")

            sum_of_dur = sum(list_dur)
            print(sum_of_dur)
            print("-----")

            avg = (sum(list_dur)/len(list_dur))
            print(avg, "avg")

            ### con= error when iterating over list of dictionary and get value from each dictionary, convert each value to float and find average prac= sn= beginners problem=
            # for ii in days_of_coding:
            #     # print(ii)
            #     print("--------")
            #     dur = ii.get("coding_duration")
            #     print(dur , type(dur))
            #     print("--------")
            #     sum += float(dur[:2])
            #     print(sum)

            #     print("--------")
            #     # print(ii["duration"])
    except:
        print("error in reading")


calculate_average_coding_time()