#create file for testing
createFile = open("input.txt", 'w')
createFile.write("January 10 2018 236.9\n")
createFile.write("January 11 2018 267.6\n")
createFile.write("January 12 2018 278.1\n")
createFile.write("January 13 2018 246.9\n")
createFile.write("February 2 2018 199.7\n")
createFile.write("February 3 2018 134.6\n")
createFile.write("February 4 2018 200.8\n")
createFile.write("February 5 2018 198.2\n")
createFile.write("March 10 2018 168.3\n")
createFile.write("March 11 2018 179.4\n")
createFile.close()
createFile = open("input2.txt", 'w')
createFile.write("January 10 2018 236.9\n")
createFile.write("March 11 2018 267.6\n")
createFile.write("May 12 2018 278.1\n")
createFile.write("July 13 2018 246.9\n")
createFile.write("July 14 2018 262.3\n")
createFile.write("November 15 2018 288.6\n")
createFile.write("November 2 2018 199.7\n")
createFile.close()

records = [] # Initializes an empty data structure for text data to be stored
def uploadTextData(file_name): # First function for input #1 to upload text data from user inputted file
    with open(file_name, 'r') as file_handle: # Opens file and reads in text data
        for line in file_handle: # Reads each line in file
            data = line.split() # Because of empty split() argument, each space separates the string in each line into a list.
            records.append(data) # List of each item is stored into the previously empty "data" list
    return records # Returns the text data list

def printData(records): # Defines a function to print the data read in from the file
    print("\nData:")
    for line in records: # Iterates the text data from the records list
        print(f"Date: {line[0]} {line[1]}, {line[2]} Output: {line[3]}") # Prints the text data by the index it appears in the records list
    print("") # Hackerrank formatting

def createStatsFile(records): # Defines a function to create a statistics file
    # Initializes variables and dictionary for statistics
    highest_output = 0
    total_by_month = {}
    total_output = 0
    records_num = 0
    all_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] # Initializes a list of all months

    for record in records: # For loop to calculate statistics line by line based on data in a list of records
        if float(record[3]) > highest_output: # Checks if the output value in the current record list is higher than the highest output seen so far
            highest_output = float(record[3]) # Updates the output value in the current record if it is higher than the highest output
            highest_date = record[0] + ' ' + record[1] + ', ' + record[2] # Gives the date that the highest output occurred in 'Month Day, Year' format
        month = record[0] # Assigns month to a variable to search in for loop
        if month in total_by_month: # Conditional to update total by month
            total_by_month[month] += float(record[3]) # If month in dictionary, adds output value in current month (3rd column of the line) to the total for all months
        else:
            total_by_month[month] = float(record[3]) # Otherwise, adds the month to the dictionary and sets the total to the output value from the current record
        total_output += float(record[3]) # Adds the output value from the current record to the overall total_output variable
        records_num += 1 # Increments total number of records processed

    avg_output = total_output / records_num # Calculates average by dividing total output by number of records

    with open("stats.txt", 'w') as file_handle: # Opens the statistics file for writing
        file_handle.write("\nStatistics file contained:")
        file_handle.write(f"\nDay with Highest Output: {highest_date}\n\n")

        for month in all_months:# Iterate through all months
            if month in total_by_month:
                file_handle.write(f"Total output for {month}: {total_by_month[month]:.1f}\n") # If a month is in the list of all months, print its total
            else:
                file_handle.write(f"Total output for {month}: 0\n") # If a month is not in the list, print total of 0

        file_handle.write(f"\nAverage output: {avg_output:.2f}\n")

def printStatsFile(): # Defines a function to print the contents of the stats.txt file
    with open("stats.txt", 'r') as file_handle: # Opens the statistics file for reading
        contents = file_handle.read() # Reads file contents, stores in a variable
        print(contents) # Prints file contents

def main():
    print("Welcome to the Power Plant Analyzer program.", end='') # Main menu welcome screen
    while True: # Program loops back to the main menu until user chooses to exit (Option 5)
        choice = input("Please choose one of the following options:\n1. Upload text data\n2. View data\n3. Download statistics\n4. Print statistics file\n5. Exit the program\n") # Gets user's choice
        if choice == "1": # Uploads text data
            file_name = input("Please enter the name of the file to be uploaded:")
            uploadTextData(file_name)
        elif choice == "2": # Views data
            printData(records)
        elif choice == "3": # Downloads statistics
            createStatsFile(records)
        elif choice == "4": # Prints statistics file
            printStatsFile()
        elif choice == "5": # Exits the program with thank you message
            print("Thank you for using the Power Plant Analyzer Program!")
            break

main()
