import datetime
date_input = input("Enter the date (mm/dd/yyyy): ")
date_input = date_input.split("/")
a = int(date_input[0])
b = int(date_input[1])
c = int(date_input[2])
d = datetime.datetime(c, a, b)
print('{:%B %d, %Y}'.format(d))