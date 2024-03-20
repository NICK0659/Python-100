import pywhatkit 

for i in range(1,50):
    pywhatkit.sendwhatmsg(phone_no= "+91 8432734366" , message= "hey!" , time_hour=10 , time_min= 41, wait_time= 7 , tab_close=True , close_time= 7)
    i=i+1
    