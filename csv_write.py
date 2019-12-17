import csv
# with open('newcsv.csv','w') as file:
#     writer= csv.DictWriter(file,['name','email'])
#     writer.writeheader()
#     writer.writerow({'name':'Aashish','email':'abc@gmail.com'})
#     # for i in range(100):
#     #     writer.writerow({'name':'aasis'})
    

with open('student.csv') as old_file:
    with open ('newcsv.csv','w+') as new_file:
        reader=csv.DictReader(old_file)
        writer=csv.DictWriter(new_file,{'name','email'})
        for row in reader :
            if int(row['sn']) % 2 == 0 :
                 writer.writerow({'name':row['name'],'email':row['email']})
            else:
                pass
            