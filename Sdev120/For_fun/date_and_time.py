from datetime import datetime as dt

print(dt.now())

'''
%Y - Four digit year
%m - Two digit month
%d - Two digit dat
%h -24 hour clock hour
%M - Two digit minute
%S -Two digit second

'''
now = dt.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

def ts():
   return dt.now().strftime("%Y-%m-%d %H:%M:S")


ts()
     