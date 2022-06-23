from datetime import datetime

n = input("# 23/06/2022 14:57:10 : \n")
n = n[2:]
datetime_object = datetime.strptime(n, "%d/%m/%Y %H:%M:%S")
print("# " + str(datetime.now() - datetime_object))
print("# " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
