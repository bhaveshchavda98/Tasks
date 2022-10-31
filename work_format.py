import datetime
today_date = datetime.datetime.now().strftime("%d/%m/%Y")
# print(today_date)
def work_format(topics):
    print("Hello Sir/ ma'am,")
    print(f"Today\'s update {today_date}")
    topics()
    print('''
Best Regards,
Bhavesh Chavda    
    ''')
# print(work_format())

@work_format
def topics():
    print('''
    1) learn about xlswriter 
        - How to write row using write_row() method,
        - How to write column using write_column() method
        - How to write list/tuple type data in xlsx file using write_row() and write_column() methods 
    2) learn about I/O 
        - learn about different file modes 
            "r" - opens file for reading mode only
            "r+" - opens file for both reading and writing mode 
            "rb" - opens file for reading in binary format 
            "rb+" - opens file for both reading and writing in binary format 
            "w" - opens file for writing mode only
            "w+" - opens file for both reading and writing mode 
            "wb" - opens file for writing in binary format
            "wb+" - opens file for both writing and reading in binary format
            "a" - opens file for appending
            "a+" - opens file for appending and reading both  
            "ab" - opens file for appending in binary format
            "ab+" - opens file for both appending and reading in binary format
        - How to open file in different modes
        - How to write data using write() methods ==> single line data
        - How to write data using writelines() methods ==> multi-line data ''')

