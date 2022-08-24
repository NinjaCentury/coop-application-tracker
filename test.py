import csv
import os
from urllib import response
import matplotlib.pyplot as plt

#current errors: stati values do not add on if file exists (side note, all stati values are multiplied by 4 for some reason, therefore I've divided by 4)

#csv format: first item is company string, second item is location string, third item is date string, fourth item is application status
new_entry = []
stati = [0, 0, 0, 0, 0]
cont = "yes"

desktop_path = os.path.expanduser('~')+'\\Desktop\\coop-application-tracker.csv'
file_exists = os.path.exists(desktop_path)

def status(csvreader, stati):
    for row in csvreader:
        if csvreader[3] == 1:
            stati[0] += 1
        elif csvreader[3] == 2:
            stati[1] += 1
        elif csvreader[3] == 3:
            stati[2] += 1
        elif csvreader[3] == 4:
            stati[3] += 1
        elif csvreader[3] == 5:
            stati[4] += 1

new_entry.clear()
if file_exists:
    file = open(desktop_path)
    csvreader = list(csv.reader(file))
    status(csvreader, stati)
    file.close()

file = open(desktop_path, 'a')

while cont == "yes":
    new_entry.clear()
    new_entry.append(input("What company did you apply to? "))
    new_entry.append(input("Where is this position located? "))
    new_entry.append(input("When did you apply here? "))
    new_entry.append(int(input("What is the status of your application: \t (1) Applied (2) Rejected (3) Interview (4) Offer (5) No Response \t")))
    writer = csv.writer(file)
    writer.writerow(new_entry)
    status(new_entry, stati)
    cont = input("Do you want to add another entry? \t (type 'yes' or 'no') ")
file.close()

newl = [a/4 for a in stati]

responsevar = ["Applied", "Rejected", "Interview", "Offer", "No Response"]
fig, ax = plt.subplots()
ax.barh(responsevar, newl, color = ["blue", "Red", "cyan", "green", "black"])
plt.show()