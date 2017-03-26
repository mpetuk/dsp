# Hint:  use Google to find python function

from  datetime import datetime
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

date_format="%m-%d-%Y"
a=datetime.strptime(date_start,date_format)
b=datetime.strptime(date_stop,date_format)
delta=b-a
print (delta,days)
#937

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_format2="%m%d%Y"
a=datetime.strptime(date_start,date_format2)
b=datetime.strptime(date_stop,date_format2)
delta=b-a
print (delta,days)
#513


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

date_format3="%d-%b-%Y"
a=datetime.strptime(date_start,date_format3)
b=datetime.strptime(date_stop,date_format3)
delta=b-a
print (delta,days)
#7850
  
