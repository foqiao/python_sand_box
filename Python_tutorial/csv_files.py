import csv

#Goal: manipulate the content
#open a file use open()
with open('email_directory.csv', 'r') as email:
    # the content inside will be separated by '-' or hyphens
    csv_reader = csv.reader(email, delimiter='-')
    #next(title) can omit the title and going to the next index's matching value
    #next(csv_reader)

    #csv.DictReader reads the content in dictionary form
    csv_dict_reader = csv.DictReader(email)

    #create a new file called editted_email_directory.txt
    with open('editted_email_directory.csv', 'w') as edit_email:
        #'\t' represents tab, the csv_write will separate the content with tabs
        csv_write = csv.writer(edit_email, delimiter='\t')

        #same as the line 12
        csv_dict_writer = csv.DictWriter(edit_email, delimiter='\t')

        #write the header of the file including the title
        csv_dict_writer.writeheader()

        #for each line of the original file
        #copy the same content, format to csv_write variable which represents the writer of the new file
        for line in csv_reader:
            csv_write.writerow(line)