status = input("Enter the status Active || Non Active ").lower()


if status == 'active':
    tem= int(input("Enter the Temp of your device"))
    if tem > 35 :
        print("High temperature")
    else:
        print("Temperature normal") 
else:
    print("Device Is Offline")               