#########################################################################
# TITLE:            Date Dimensions                                     #
# AUTHOR:           BASASKS                                             #
# PYTHON VERSION:   Python 3.5.9                                        #
# USAGE:            python3 py02_sc_datedimension.py                    #
# NOTES:            Toggle variable curr_ts for different dates         #
#########################################################################


#####   MODULES

from datetime import datetime, date, time, timedelta
import calendar
import math


#####   MAIN CODE

# INITIALIZE BASE VARIABLES

#curr_ts = datetime.now()
curr_ts = datetime(2021, 7, 31)
curr_tsstr = curr_ts.strftime("%Y-%m-%d %H:%M:%S.%f")
base_dt = datetime(year=1900,month=1,day=1)
base_dtstr = base_dt.strftime("%Y-%m-%d")

# DATE DIMENSION VARIABLES

dim_dateserial = abs(curr_ts-base_dt).days + 2 # Serial based on MS Excel
str_dim_dateserial = str(dim_dateserial)

dim_date = curr_ts.strftime("%Y-%m-%d")
str_dim_date = str(dim_date)

dim_year = int(curr_ts.strftime("%Y")) # Stored as integer
str_dim_year = str(dim_year)

dim_month = int(curr_ts.strftime("%m")) # Stored as integer
str_dim_month = str(dim_month)

dim_monthname1 = curr_ts.strftime("%B")
str_dim_monthname1 = str(dim_monthname1)

dim_monthname2 = curr_ts.strftime("%b")
str_dim_monthname2 = str(dim_monthname2)

str_dim_monthname = str_dim_monthname1 if str_dim_monthname1 == str_dim_monthname2 else str_dim_monthname1 + " or " + str_dim_monthname2

dim_day = int(curr_ts.strftime("%d")) # Stored as integer
str_dim_day = str(dim_day)

dim_dayofweek1 = curr_ts.strftime("%A") 
str_dim_dayofweek1 = str(dim_dayofweek1)

dim_dayofweek2 = curr_ts.strftime("%a") 
str_dim_dayofweek2 = str(dim_dayofweek2)

dim_dayofweeknum = int(curr_ts.strftime("%w")) # Stored as integer
str_dim_dayofweeknum = str(dim_dayofweeknum)

dim_quarter = int(math.ceil(float(dim_month)/3)) # Stored as integer
str_dim_quarter = str(dim_quarter)

dim_dayofyear = int(curr_ts.strftime("%j")) # Stored as integer
str_dim_dayofyear = str(dim_dayofyear)

dim_weekofyear = int(curr_ts.strftime("%U")) # Stored as integer
str_dim_weekofyear = str(dim_weekofyear)

dim_weekofyear = int(curr_ts.strftime("%U")) # Stored as integer
str_dim_weekofyear = str(dim_weekofyear)

dim_yearstart = datetime(dim_year, 1, 1).strftime("%Y-%m-%d")
str_dim_yearstart = str(dim_yearstart)

dim_yearend = datetime(dim_year, 12, 31).strftime("%Y-%m-%d")
str_dim_yearend = str(dim_yearend)

dim_quarterstart = datetime(dim_year, dim_quarter*3-2, 1).strftime("%Y-%m-%d")
str_dim_quarterstart = str(dim_quarterstart)

dim_quarterend = datetime(dim_year, dim_quarter*3, calendar.monthrange(dim_year, dim_quarter*3)[1]).strftime("%Y-%m-%d")
str_dim_quarterend = str(dim_quarterend)

dim_monthstart = datetime(dim_year, dim_month, 1).strftime("%Y-%m-%d")
str_dim_monthstart = str(dim_monthstart)

dim_monthend = datetime(dim_year, dim_month, calendar.monthrange(dim_year, dim_month)[1]).strftime("%Y-%m-%d")
str_dim_monthend = str(dim_monthend)

dim_weekstart = (curr_ts - timedelta(days=dim_dayofweeknum)).strftime("%Y-%m-%d")
str_dim_weekstart = str(dim_weekstart)

dim_weekend = (curr_ts + timedelta(days=6-dim_dayofweeknum)).strftime("%Y-%m-%d")
str_dim_weekend = str(dim_weekend)

dim_72hrsbefore = curr_ts - timedelta(hours=72)
str_dim_72hrsbefore = str(dim_72hrsbefore)

dim_24hrsbefore = curr_ts - timedelta(hours=24)
str_dim_24hrsbefore = str(dim_24hrsbefore)

dim_8hrsbefore = curr_ts - timedelta(hours=8)
str_dim_8hrsbefore = str(dim_8hrsbefore)

dim_8hrsafter = curr_ts + timedelta(hours=8)
str_dim_8hrsafter = str(dim_8hrsafter)

dim_24hrsafter = curr_ts + timedelta(hours=24)
str_dim_24hrsafter = str(dim_24hrsafter)

dim_72hrsafter = curr_ts + timedelta(hours=72)
str_dim_72hrsafter = str(dim_72hrsafter)


# OUTPUT DATE DIMENSION

print("\n")
print("TIMESTAMP: " + curr_tsstr)

print("\n")
print("Date Serial: \t\t" + str_dim_dateserial)
print("Date: \t\t\t" + str_dim_date)
print("Year: \t\t\t" + str_dim_year)
print("Quarter: \t\t" + str_dim_quarter)
print("Month: \t\t\t" + str_dim_month)
print("Month Name: \t\t" + str_dim_monthname)
print("Day: \t\t\t" + str_dim_day)
print("Day of Week: \t\t" + str_dim_dayofweek1 + " or " + str_dim_dayofweek2)
print("Day of Week (0=Sun): \t" + str_dim_dayofweeknum)
print("Week of Year: \t\t" + str_dim_weekofyear)
print("Day of Year: \t\t" + str_dim_dayofyear)

print("\n")
print("Year Startdate: \t" + str_dim_yearstart)
print("Year Enddate: \t\t" + str_dim_yearend)
print("Quarter Startdate: \t" + str_dim_quarterstart)
print("Quarter Enddate: \t" + str_dim_quarterend)
print("Month Startdate: \t" + str_dim_monthstart)
print("Month Enddate: \t\t" + str_dim_monthend)
print("Week Startdate: \t" + str_dim_weekstart)
print("Week Enddate: \t\t" + str_dim_weekend)

print("\n")
print("72 Hours Before is...\t" + str_dim_72hrsbefore)
print("24 Hours Before is...\t" + str_dim_24hrsbefore)
print("8 Hours Before is...\t" + str_dim_8hrsbefore)
print("8 Hours From Now is...\t" + str_dim_8hrsafter)
print("24 Hours From Now is...\t" + str_dim_24hrsafter)
print("72 Hours From Now is...\t" + str_dim_72hrsafter)
print("\n")
