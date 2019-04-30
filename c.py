# DataBdef next_weekday(d, weekday):ase Format: <datetime> + <event>

from collections import OrderedDict
from datetime import datetime, date, time, timedelta
from itertools import imap
import re
import os

class bcolors:
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   WHITE = '\033[97m'
   PERFECTBLUE = '\033[96m'
   ENDC = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'

# Given a date, it finds the next weekday (e.g. next Monday).
# d: datetime      weekday: int         return: datetime
def next_weekday(d, weekday):
   days_ahead = weekday - d.weekday()
   if days_ahead <= 0: # Target day already happened this week
     days_ahead += 7
   return d + timedelta(days_ahead)

# This fuction prints out date and time in a clear formate.
# This function takes a string input, and returns a string.
def dateFormat(dateStr):
   dateList = []        # declare an empty list
   for i in range(4):    # stores year
      dateList.append(dateStr[i])
   dateList.append('-')
   for i in range(4, 6):  # stores month
      dateList.append(dateStr[i])
   dateList.append('-')
   for i in range(6, 8):  # stores day
      dateList.append(dateStr[i])
   dateList.append('  ')
   for i in range(8, 10): # stores hour
      dateList.append(dateStr[i])
   dateList.append(' : ') # stores minute
   for i in range(10, 12):
      dateList.append(dateStr[i])

   returnStr = "".join(dateList)
   return returnStr
# end def

# This function returns the length of the longest value in the dict()
# It takes a dict input and returns an int
def longestName(theDic):
   longest = max(theDic.values(), key=len)
   return len(longest)

# This function lists all events out
def listEvents():
   # save the process first ----------------------
   with open("Calendar/DataBase.db", "w") as f:   # rewrite Calendar/DataBase.db
      for key in assignment:
         f.write(key + " " + bytes(assignment[key]) + "\n")
     # end for
   # end with

   print ""
   if len(assignment) == 0:     # there is nothing in the dict
     print bcolors.WARNING + "Your to-do list is empty, man.\n" + bcolors.ENDC
     return
   else:
     longest = longestName(assignment)   # get the length of the longest key
     count = 0              # a counter used to limit ten print-outs
     # key is the date, and you are enumerating dates in the dict()
     for key in assignment:
       keyLen = len(assignment[key])      # get the length of current event
       diff = longest - keyLen + 2
       count = count + 1
       if count == 17:     # make sure at most 16 shits are printed out
         break
       # end if

       todayYear = list()
       currYear = list()
       todayMon = list()
       currMon = list()
       todayDay = list()
       currDay = list()
       for i in range(8):
         if i<4:
            todayYear.append(str(todayDate)[i])
            currYear.append(key[i])
         elif i<6:
            todayMon.append(str(todayDate)[i])
            currMon.append(key[i])
         else:
            todayDay.append(str(todayDate)[i])
            currDay.append(key[i])
       # end for

       fuckCurrYear = "".join(currYear)
       fuckTodayYear = "".join(todayYear)
       fuckCurrMon = "".join(currMon)
       fuckTodayMon = "".join(todayMon)
       fuckCurrDay = "".join(currDay)
       fuckTodayDay = "".join(todayDay)

       delta = date(int(fuckCurrYear), int(fuckCurrMon), int(fuckCurrDay)) - date(int(fuckTodayYear), int(fuckTodayMon), int(fuckTodayDay))
       difference = int(delta.days)

       # create a set of event names in weekly calendar
       nextWeek = open("Calendar/Weekly.db", "r")
       listWeek = set()
       for ddd in nextWeek:
           listWeek.add(ddd.split()[2])
       nextWeek.close()

       weekdayCode = datetime.strptime(key, "%Y%m%d%H%M").weekday()
       wdaydict = {0:'Mon ',1:'Tues',2:'Wed ',3:'Thur',4:'Fri ',5:'Sat ',6:'Sun '}
       if difference == 1:
         if assignment[key] in listWeek:
            print(assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' + wdaydict[weekdayCode] + " (tomorrow)")
         else:
            print bcolors.WARNING + (assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' + wdaydict[weekdayCode] + " (tomorrow)") + bcolors.ENDC
       elif difference == 0:
         if assignment[key] in listWeek:
            print(assignment[key] + diff * " " + bytes(dateFormat(key)) +' ' + wdaydict[weekdayCode] + " (today)")
         else:
            print bcolors.WARNING+ (assignment[key] + diff * " " + bytes(dateFormat(key)) +' ' + wdaydict[weekdayCode] + " (today)") + bcolors.ENDC
       else:
         if assignment[key] in listWeek:
            print(assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' + wdaydict[weekdayCode] +  " (in " + bytes(difference) + " days)")
         else:
            print bcolors.WARNING+ (assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' + wdaydict[weekdayCode] +  " (in " + bytes(difference) + " days)") + bcolors.ENDC
     # end for
   # end if-else
   print("")
# end of list function

assignment = dict()   # restructured: map from due dates to assignment
if os.stat("Calendar/DataBase.db").st_size != 0:
   inputFile = open("Calendar/DataBase.db", "r")


   for line in inputFile:
      newString = line.split()     # split lines in database by space
      the_name_of_assignment = ' '.join(newString[1:])    # newString[0] is date and time
      assignment[newString[0]] = the_name_of_assignment   # map date and time to name
   # end for
#end if

# get today's date
tDate = datetime.today()
todayDate = int(tDate.strftime('%Y%m%d'))

# push next week's agenda in
if os.stat("Calendar/Weekly.db").st_size != 0:
   nextWeek = open("Calendar/Weekly.db", "r")
   for line in nextWeek:
      newString = line.split()
      # get the the date of the last class in next week
      nextShit = next_weekday(datetime.today(), int(newString[0]))
      # stripe it into %Y%m%d form
      # String nextDay;
      nextDay = nextShit.strftime('%Y%m%d')
      # String parseTime;
      parseTime = datetime.strptime(nextDay, "%Y%m%d")
      catDay = str(nextDay) + newString[1]
      reDay = re.sub("[^0-9]", "", catDay)

      assignment[reDay] = newString[2]
   # end for

   # sort the dictionary by date and time
   assignment = OrderedDict(sorted(assignment.items(), key=lambda x: int(x[0])))

   # delete expired assignments
   # key is the date
   for key in assignment:
      stringDate = key[:8]      # take out YMD only
      copy = assignment[key]
      if int(stringDate) < todayDate:     # if the date is less than today's date
         del assignment[key]            # the assignment has passed due date
         print bcolors.WHITE + (copy + " is automatically deleted because it is in the past now.") + bcolors.ENDC
      # end if
   # end for
# end if

print("")
# Up to this point, all history data have been stored into the dictionary and sorted #
print bcolors.HEADER + "Welcome to Todo App developed by James Li." + bcolors.ENDC
print bcolors.HEADER +("Today is " + datetime.today().strftime('%Y-%m-%d') + ".") + bcolors.ENDC
print bcolors.HEADER +"Thanks for using this app. Have a nice one :)" + bcolors.ENDC
print bcolors.HEADER + "----------------------------------------------" + bcolors.ENDC

while True:
   if os.stat("Calendar/DataBase.db").st_size != 0:
     assignment = OrderedDict(sorted(assignment.items(), key=lambda x: int(x[0])))
   print bcolors.PERFECTBLUE + "Commands: ls, map, rm, i, o, q, t, c, r, d" + bcolors.ENDC
   print bcolors.PERFECTBLUE + "Detailed instructions are in the README file." + bcolors.ENDC
   print bcolors.PERFECTBLUE + "Please enter your operation:" + bcolors.ENDC
   ch = raw_input("")
   charArray = ch.split()   # input array: get usr input

   if len(charArray)==0:
     # sort the dict
     if os.stat("Calendar/DataBase.db").st_size != 0:
       assignment = OrderedDict(sorted(assignment.items(), key=lambda x: int(x[0])))
     continue
   elif charArray[0] == 'q' or charArray[0] == 'Q' or charArray[0] == "exit" or charArray[0] == "quit" or charArray[0] == "ZZ":
     with open("Calendar/DataBase.db", "w") as f:   # rewrite Calendar/DataBase.db
        # key is the date
       for key in assignment:
          f.write(key + " " + bytes(assignment[key]) + "\n")
       # end for
     f.close()
     break
   elif (charArray[0] == 'i' or charArray[0] == 'I') and len(ch)==1:
     name = raw_input("   1. Enter event name\n")
     Date = raw_input("   2. Enter the date (format: year + month + day)\n")
     if Date == "today" or Date=='':
       Date = datetime.today().strftime('%Y%m%d')
     elif Date == "tomorrow":
       Date = str(date.today() + timedelta(days=1))
     Date = re.sub("[^0-9]", "", Date)    # keep only numeric chars
     # validity check
     if len(Date) != 8:
       print "Please enter a valid date.\n"
       continue
     time = raw_input("   3. Enter the time (format: hour + minute, e.g. 15:30\n")
     time = re.sub("[^0-9]", "", time)    # for the convenience of reading from data base, keep only numeric chars
     if len(time) != 4:
       time = "0000"
     assignment[Date + time] = name      # concatenate date and time
   elif charArray[0] == 'd' or charArray[0] == 'D':
     tobeDeleted = raw_input("   1. Enter assignment name\n")
     if tobeDeleted in assignment.values():      # check if the assignment is in the dict
        for key in list(assignment.keys()):
           if assignment[key]==tobeDeleted:
              del assignment[key]
        print bcolors.FAIL + (tobeDeleted + " is deleted") + bcolors.ENDC
     else:                        # if the assignment name does not exist
       print(tobeDeleted + " not found")
     # end if-else
   elif charArray[0]=='rm' or charArray[0]=='delete':
     nextWeek = open("Calendar/Weekly.db", "r")
     listWeek = set()
     for ddd in nextWeek:
        listWeek.add(ddd.split()[2])
     nextWeek.close()
     splitedCH = ch.split()[1:]   # for every item after 'rm'
     itemToDel = ' '.join(splitedCH)
     # end for

     if itemToDel in assignment.values():  # if it is in the event dict
        for key in list(assignment.keys()):
           if assignment[key]==itemToDel:
             del assignment[key]
             print bcolors.FAIL +  (itemToDel + " is deleted") + bcolors.ENDC
     else:
       print(itemToDel + " not found")
     print('')
   elif charArray[0] == "Weekly" or charArray[0] == "weekly":
       print("Please enter your weekly schedule in the format weekday (e.g Monday)  time (e.g. 13:00)  eventName")
       print("End input with a \"q\"")

       with open("Calendar/Weekly.db", "w") as nextWeek:
           while True:
               newInput = raw_input()
               if newInput=="q" or newInput=="Q" or newInput=="exit" or newInput=="quit":
                   break
               splitedInput = newInput.split()
               listOfInput = list()
               if splitedInput[0] == "Mon" or splitedInput[0] == "Monday":
                   listOfInput.append("0")
               elif splitedInput[0] == "Tues" or splitedInput[0] == "Tuesday":
                   listOfInput.append("1")
               elif splitedInput[0] == "Wed" or splitedInput[0] == "Wednesday":
                   listOfInput.append("2")
               elif splitedInput[0] == "Thur" or splitedInput[0] == "Thursday":
                   listOfInput.append("3")
               elif splitedInput[0] == "Fri" or splitedInput[0] == "Friday":
                   listOfInput.append("4")
               elif splitedInput[0] == "Sat" or splitedInput[0] == "Saturday":
                   listOfInput.append("5")
               elif splitedInput[0] == "Sun" or splitedInput[0] == "Sunday":
                   listOfInput.append("6")
               else:
                   print("Please enter a valid weekday")
                   continue

               reModTime = re.sub("[^0-9]", "", splitedInput[1])
               if len(reModTime)<4:
                   if int(reModTime)>=0 and int(reModTime)<1000:
                       ["0"] + reModTime
                   else:
                       print("Please enter a valid time")
                       continue
               else:
                   if int(reModTime)<2400:
                       listOfInput.append(reModTime)
                   else:
                       print("Please enter a valid time")

               for i in range(2,len(splitedInput)):
                   listOfInput.append(splitedInput[i])

               nextWeek.write(listOfInput[0] + " " + listOfInput[1] + " " + listOfInput[2])
   elif charArray[0] == 'c' or charArray[0] == 'C':
     name = raw_input("   1. Enter assignment name\n")
     if name in assignment.values():         # check if the assignment is in the dict
       print dateFormat(assignment.keys()[assignment.values().index(name)])     # print the date and time
     else:                      # not found
       print(name + " not found")
     print(" ")
   elif charArray[0]=='mv':
     if len(charArray)!= 3:       # takes three arguments
       print("mv <old event name> <new name>")
       continue
     if charArray[1] not in assignment.values():
       print(charArray[1] + " not found")
       continue
     date_of_old = assignment.keys()[assignment.values().index(charArray[1])]  # get the date of old
     assignment[date_of_old] = charArray[2]   # map new name to old date
     print("")
   elif charArray[0] == 'r' or charArray[0] == 'R':
     name = raw_input("   1. Enter assignment name\n")
     if name in assignment.values():         # check if the assignment is in the dict
       del assignment[assignment.keys()[assignment.values().index(name)]]
       revisedDate = raw_input("   2. Enter the revised date (formate: Year-Month-Day)\n")   # get new date
       if revisedDate == "today" or revisedDate=="Today":
           revisedDate = str(datetime.today().strftime('%Y%m%d'))
       elif revisedDate == "tomorrow" or revisedDate == "Tomorrow":
           whateverShit = str(date.today() + timedelta(days=1))
           revisedDate = re.sub("[^0-9]", "", whateverShit)
       elif revisedDate == "Sun" or revisedDate == "Sunday":
           revisedDate = next_weekday(datetime.today(), 6).strftime("%Y%m%d")
       elif revisedDate == "Sat" or revisedDate == "Saturday":
           revisedDate = next_weekday(datetime.today(), 5).strftime("%Y%m%d")
       elif revisedDate == "Fri" or revisedDate == "Friday":
           revisedDate = next_weekday(datetime.today(), 4).strftime("%Y%m%d")
       elif revisedDate == "Thur" or revisedDate == "Thursday":
           revisedDate = next_weekday(datetime.today(), 3).strftime("%Y%m%d")
       elif revisedDate == "Wed" or revisedDate == "Wednesday":
           revisedDate = next_weekday(datetime.today(), 2).strftime("%Y%m%d")
       elif revisedDate == "Tues" or revisedDate == "Tuesday":
           revisedDate = next_weekday(datetime.today(), 1).strftime("%Y%m%d")
       elif revisedDate == "Mon" or revisedDate == "Monday":
           revisedDate = next_weekday(datetime.today(), 0).strftime("%Y%m%d")
       else:
           revisedDate = re.sub("[^0-9]", "", revisedDate)        # keep only numeric chars

       revisedTime = raw_input("   3. Enter the revised time\n")   # get new time
       revisedTime = re.sub("[^0-9]", "", revisedTime)        # keep only numeric chars
       if len(revisedTime) + len(revisedDate) != 12:
           print bcolors.WARNING + ("\nPlease enter a valid date and time") + bcolors.ENDC
       else:
           assignment[revisedDate + revisedTime] = name          # concatenate and store
           print bcolors.WARNING + ("Revision succeeded\n") + bcolors.ENDC
     else:                      # not found
       print(name + " not found")
     print(" ")
   elif charArray[0] == 't' or charArray[0] == 'T':
     longest = longestName(assignment)  # get the longest word in the dict
     # key is the date
     for key in assignment:
       keyLen = len(assignment[key])  # get the length of the current event name
       diff = longest - keyLen + 2   # the number of required spaces between name and date
       stringDate = key[:8]         # keep only YMD
       if int(stringDate) - todayDate == 1:    # get all assignments due tomorrow
         print(assignment[key] + diff*" " + bytes(dateFormat(key)))
     print("")
   elif charArray[0] == 'o' or charArray[0] == 'O':    # similar to the last one
     longest = longestName(assignment)      # get the longest event name
     for key in assignment:
       keyLen = len(assignment[key])
       diff = longest - keyLen + 2
       stringDate = key[:8]
       if int(stringDate) - todayDate == 0:
         print(assignment[key] + diff*" " + bytes(dateFormat(key)))
     print("")
   elif charArray[0]=="more":
     if len(assignment)==0:
       print bcolors.WARNING + "Your to-do list is empty, man." + bcolors.ENDC
       continue
     else:
       longest = longestName(assignment)
       for key in assignment:
         keyLen = len(assignment[key])
         diff = longest - keyLen + 2
         todayYear = list()
         todayYear = list()
         currYear = list()
         todayMon = list()
         currMon = list()
         todayDay = list()
         currDay = list()
         for i in range(8):
            if i<4:
              todayYear.append(str(todayDate)[i])
              currYear.append(key[i])
            elif i<6:
              todayMon.append(str(todayDate)[i])
              currMon.append(key[i])
            else:
              todayDay.append(str(todayDate)[i])
              currDay.append(key[i])
          # end for

         fuckCurrYear = "".join(currYear)
         fuckTodayYear = "".join(todayYear)
         fuckCurrMon = "".join(currMon)
         fuckTodayMon = "".join(todayMon)
         fuckCurrDay = "".join(currDay)
         fuckTodayDay = "".join(todayDay)

         delta = date(int(fuckCurrYear), int(fuckCurrMon), int(fuckCurrDay)) - date(int(fuckTodayYear),    int(fuckTodayMon), int(fuckTodayDay))
         difference = int(delta.days)

         # create a set of event names in weekly calendar
         nextWeek = open("Calendar/Weekly.db", "r")
         listWeek = set()
         for ddd in nextWeek:
            listWeek.add(ddd.split()[2])
         nextWeek.close()

         weekdayCode = datetime.strptime(key, "%Y%m%d%H%M").weekday()
         wdaydict = {0:'Mon ',1:'Tues',2:'Wed ',3:'Thur',4:'Fri ',5:'Sat ',6:'Sun '}
         if difference == 1:
            if assignment[key] in listWeek:
              print(assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' + wdaydict[weekdayCode] +  " (tomorrow)")
            else:
              print bcolors.WARNING + (assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' + wdaydict[weekdayCode] + " (tomorrow)") + bcolors.ENDC
         elif difference == 0:
            if assignment[key] in listWeek:
              print(assignment[key] + diff * " " + bytes(dateFormat(key)) +' ' + wdaydict[weekdayCode] +   " (today)")
            else:
              print bcolors.WARNING+ (assignment[key] + diff * " " + bytes(dateFormat(key)) +' ' + wdaydict[weekdayCode] + " (today)") + bcolors.ENDC
         else:
            if assignment[key] in listWeek:
              print(assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' + wdaydict[weekdayCode] +  " (in " + bytes(difference) + " days)")
            else:
              print bcolors.WARNING+ (assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' +  wdaydict[weekdayCode] +  " (in " + bytes(difference) + " days)") + bcolors.ENDC
       # end for
     #end if-else
     print ''
   elif charArray[0] == 'l' or charArray[0] == 'L' or charArray[0] == "ls":
     listEvents()
   elif charArray[0]=='map':
     # if the time is like 3:00, it will be converted to 15:00
     charArray[-1] = re.sub("[^0-9]", "", charArray[-1])
     if len(charArray[-1])==3:
       if int(charArray[-1][0])<6:
         charArray[-1] = str(int(charArray[-1])+1200)
       else:
         charArray[-1] = str('0' + charArray[-1])




######### This part still has some problems ######


     elif charArray[-1]=="am" or charArray[-1]=="AM" or charArray[-1]=="a.m." or charArray[-1]=="morning":
         ch = re.sub("in the morning","", ch)
         ch = re.sub("AM","",ch)
         ch = re.sub("a.m.","", ch)
         ch = re.sub("am","",ch)
         charArray[-1] = re.findall("[0-9]", ch)
         if len(charArray[-1]==1):
             charArray[-1] = str(int(charArray[-1]) * 100)
             charArray[-1] = ["0"] + charArray[-1]
         elif len(charArray[-1]==2):
             charArray[-1] = str(int(charArray[-1]) * 100)
     elif charArray[-1]=="pm" or charArray[-1]=="PM" or charArray[-1]=="p.m." or charArray[-1]=="afternoon" or charArray[-1]=="evening" or charArray[-1]=="tonight":
         ch = re.sub("in the evening","",ch)
         ch = re.sub("in the afternoon","",ch)
         ch = re.sub("tonight", "",ch)
         ch = re.sub("PM", "",ch)
         ch = re.sub("pm","",ch)
         ch = re.sub("p.m.","",ch)
         charArray[-1] = re.findall("[0-9]", ch)
         if len(charArray[-1])<4:
             if len(charArray[-1])==1:
                 charArray[-1] = str(int(charArray[-1]) * 100)
                 charArray[-1] = ["0"] + charArray[-1]
             elif len(charArray[-1])==2:
                 charArray[-1] = str(int(charArray[-1]) * 100)

             charArray[-1] = str(int(charArray[-1])+1200)


##################################################



     if len(charArray[-1])!=4:
         print("Oops, there is something wrong with \"Time\". Please enter a valid time.")

     if charArray[-2]=="today" or charArray[-2]=="tonight":
       Date = datetime.today().strftime('%Y%m%d')
       Date = Date + str(charArray[-1])
     elif charArray[-2]=='tomorrow':
       Date = str(date.today() + timedelta(days=1))
       Date = Date + str(charArray[-1])
     elif charArray[-2]=="Sun" or charArray[2]=="Sunday":
       # String nextDate;
       nextDate = next_weekday(datetime.today(), 6).strftime('%Y%m%d')
       Date = nextDate + str(charArray[-1])
     elif charArray[-2]=="Mon" or charArray[2]=="Monday":
       # String nextDate;
       nextDate = next_weekday(datetime.today(), 0).strftime('%Y%m%d')
       Date = nextDate + str(charArray[-1])
     elif charArray[-2]=="Tues" or charArray[2]=="Tuesday":
       # String nextDate;
       nextDate = next_weekday(datetime.today(), 1).strftime('%Y%m%d')
       Date = nextDate + str(charArray[-1])
     elif charArray[-2]=="Wed" or charArray[2]=="Wednesday":
       # String nextDate;
       nextDate = next_weekday(datetime.today(), 2).strftime('%Y%m%d')
       Date = nextDate + str(charArray[-1])
     elif charArray[-2]=="Thur" or charArray[2]=="Thurs" or charArray[2]=="Thursday":
       # String nextDate;
       nextDate = next_weekday(datetime.today(), 3).strftime('%Y%m%d')
       Date = nextDate + str(charArray[-1])
     elif charArray[-2]=="Fri" or charArray[2]=="Friday":
       # String nextDate;
       nextDate = next_weekday(datetime.today(), 4).strftime('%Y%m%d')
       Date = nextDate + str(charArray[-1])
     elif charArray[-2]=="Sat" or charArray=='Saturday':
       # String nextDate;
       nextDate = next_weekday(datetime.today(), 5).strftime('%Y%m%d')
       Date = nextDate + str(charArray[-1])
     else:
       if(len(charArray[-1])==12):
         Date = charArray[-1]
       else:
         Date = ''.join(charArray[-2:])
     # end if-else

     Date = re.sub("[^0-9]", "", Date)    # keep only numeric chars
     if len(Date)==4:
       Date = datetime.today().strftime('%Y%m%d') + Date
     if len(Date) != 12:
       print("Please enter a valid date.\n")
       continue

    # time conflict check
     if os.stat("Calendar/DataBase.db").st_size != 0:
        flag = True
        for datE in assignment:
           targetTime = datetime.strptime(datE, "%Y%m%d%H%M") # datetime type
           compTime = datetime.strptime(Date, "%Y%m%d%H%M")   # datetime type
           diffTime = compTime - targetTime     # calculate the time difference
           if diffTime<timedelta(minutes=0):    # absolute value
             diffTime = -diffTime
           if diffTime <= timedelta(minutes=60): # if the absolute value of difference is less than an hour
             print("\n" + str(assignment[datE]) + " is "+ datE)    # print warning message
             ans =raw_input("Are you sure want to insert the event? (y/n)\n")
             if ans=="y" or ans=="yes" or ans=='' or ans=='yup' or ans=='yeah' or ans=='Hell Yeah' or ans=='hell yeah':
                continue
             else:
                flag = False
                break
        # end for
        if flag:   # if approved to insert the event
           if len(charArray[-1])==12:  # if regular format of date
              assignment[Date] = ' '.join(charArray[1:-1])
           elif len(charArray)==3:    # simplified entry
              assignment[Date] = ' '.join(charArray[1:-1])
           else:                  # if not regular (by date code)
              assignment[Date] = ' '.join(charArray[1:-2])
           print bcolors.WARNING + bcolors.BOLD + "map succeeded" + bcolors.ENDC
        print('')
        # end if
     else:      # if File is empty
        if len(charArray[-1])==12:  # if regular format of date
           assignment[Date] = ' '.join(charArray[1:-1])
        elif len(charArray)==3:    # simplified entry
           assignment[Date] = ' '.join(charArray[1:-1])
        else:                  # if not regular (by date code)
           assignment[Date] = ' '.join(charArray[1:-2])
        print bcolors.WARNING + bcolors.BOLD + "map succeeded\n" + bcolors.ENDC
     # end else
   else:      # None of the previous patterns are matched
     if re.search("today's date", ch) or re.search("date of today", ch) or re.search("date today", ch):
        print("Today is " + datetime.today().strftime('%Y-%m-%d') + ".")
     elif re.search("Fuck", ch) or re.search("Bustard", ch) or re.search("asshole", ch) or re.search("shit", ch) or re.search("whore", ch):
        print("No bad words, bitch.")
     elif re.search("I will", ch) or re.search("I want to", ch) or re.search("I plan to", ch) or re.search("I intend to", ch) or re.search("to my plan", ch) or re.search("to my schedule",ch) or re.search("I am going to", ch) or re.search("I'm going to", ch):
       ch = re.sub("to my schedule", "", ch)
       ch = re.sub("I want to", "", ch)
       ch = re.sub("I intend to", "", ch)
       ch = re.sub("I will", "", ch)
       ch = re.sub("I plan to", "", ch)
       ch = re.sub("to my plan", "", ch)
       ch = re.sub("I am going to", "", ch)
       ch = re.sub("I'm going to", "", ch)

       if re.search("tomorrow",ch):
         ch = re.sub("on tomorrow at", "", ch)
         ch = re.sub("tomorrow at", "", ch)
         ch = re.sub("tomorrow","",ch)     # delete "tomorrow"
         ch = re.sub("Tomorrow", "", ch)
         Date = str(date.today() + timedelta(days=1))
       elif re.search("today", ch):
         ch = re.sub("today at", "", ch)
         ch = re.sub("today", "", ch)
         ch = re.sub("Today", "", ch)
         Date = datetime.today().strftime('%Y%m%d')
       elif re.search("Monday",ch):
         ch = re.sub("on next Monday at","",ch)
         ch = re.sub("On next Monday,","",ch)
         ch = re.sub("on next Monday","",ch)
         ch = re.sub("on Monday at","",ch)
         ch = re.sub("On Monday at","",ch)
         ch = re.sub("on Monday","",ch)
         ch = re.sub("On Monday,","",ch)
         Date = next_weekday(datetime.today(), 0).strftime('%Y%m%d')
       elif re.search("Tuesday",ch):
         ch = re.sub("on next Tuesday at","",ch)
         ch = re.sub("On next Tuesday,","",ch)
         ch = re.sub("on next Tuesday","",ch)
         ch = re.sub("On this Tuesday," "", ch)
         ch = re.sub("on this Tuesday at","",ch)
         ch = re.sub("on this Tuesday", "", ch)
         ch = re.sub("on Tuesday at","",ch)
         ch = re.sub("On Tuesday at","",ch)
         ch = re.sub("on Tuesday","",ch)
         ch = re.sub("On Tuesday,","",ch)
         Date = next_weekday(datetime.today(), 1).strftime('%Y%m%d')
       elif re.search("Wednesday",ch):
         ch = re.sub("on next Wednesday at","",ch)
         ch = re.sub("On next Wednesday,","",ch)
         ch = re.sub("on next Wednesday","",ch)
         ch = re.sub("On this Wednesday,", "",ch)
         ch = re.sub("on this Wednesday at", "",ch)
         ch = re.sub("on this Wednesday", "",ch)
         ch = re.sub("on Wednesday at","",ch)
         ch = re.sub("On Wednesday at","",ch)
         ch = re.sub("on Wednesday","",ch)
         ch = re.sub("On Wednesday,","",ch)
         Date = next_weekday(datetime.today(), 2).strftime('%Y%m%d')
       elif re.search("Thursday",ch):
         ch = re.sub("on next Thursday at","",ch)
         ch = re.sub("On next Thursday,","",ch)
         ch = re.sub("on next Thursday","",ch)
         ch = re.sub("On this Thursday,", "",ch)
         ch = re.sub("on this Thursday at", "",ch)
         ch = re.sub("on this Thursday", "",ch)
         ch = re.sub("on Thursday at","",ch)
         ch = re.sub("On Thursday at","",ch)
         ch = re.sub("on Thursday","",ch)
         ch = re.sub("On Thursday,","",ch)
         Date = next_weekday(datetime.today(), 3).strftime('%Y%m%d')
       elif re.search("Friday",ch):
         ch = re.sub("on next Friday at","",ch)
         ch = re.sub("On next Friday,","",ch)
         ch = re.sub("on next Friday","",ch)
         ch = re.sub("On this Friday,", "",ch)
         ch = re.sub("on this Friday at", "",ch)
         ch = re.sub("on this Friday", "",ch)
         ch = re.sub("on Friday at","",ch)
         ch = re.sub("On Friday at","",ch)
         ch = re.sub("on Friday","",ch)
         ch = re.sub("On Friday,","",ch)
         Date = next_weekday(datetime.today(), 4).strftime('%Y%m%d')
       elif re.search("Saturday",ch):
         ch = re.sub("on next Saturday at","",ch)
         ch = re.sub("On next Saturday,","",ch)
         ch = re.sub("on next Saturday","",ch)
         ch = re.sub("On this Saturday,", "",ch)
         ch = re.sub("on this Saturday at", "",ch)
         ch = re.sub("on this Saturday", "",ch)
         ch = re.sub("on Saturday at","",ch)
         ch = re.sub("On Saturday at","",ch)
         ch = re.sub("on Saturday","",ch)
         ch = re.sub("On Saturday,","",ch)
         Date = next_weekday(datetime.today(), 5).strftime('%Y%m%d')
       elif re.search("Sunday",ch):
         ch = re.sub("on next Sunday at","",ch)
         ch = re.sub("On next Sunday,","",ch)
         ch = re.sub("on next Sunday","",ch)
         ch = re.sub("On this Sunday,", "",ch)
         ch = re.sub("on this Sunday at", "",ch)
         ch = re.sub("on this Sunday", "",ch)
         ch = re.sub("on Sunday at","",ch)
         ch = re.sub("On Sunday at","",ch)
         ch = re.sub("on Sunday","",ch)
         ch = re.sub("On Sunday,","",ch)
         Date = next_weekday(datetime.today(), 6).strftime('%Y%m%d')

       ch = re.sub("[^A-Za-z0-9 ]", "", ch)
       timeList=list()
       splitedList = ch.split()
       for s in range(0, len(ch.split())):
         if splitedList[s].isdigit():
            timeList.append(splitedList[s])
            if(splitedList[s-1]=="at" or splitedList[s-1]=="on" or splitedList[s-1]=="in" or splitedList[s-1]=="during"):
              splitedList.pop(s-1)
            break

       ch = " ".join(splitedList)
       if(len(timeList)>2):
         print "Please enter a valid time\n"
         continue

       exactTime = "".join(str(x) for x in timeList)
       if (int(exactTime)>0 and int(exactTime)<500) or re.search("in the afternoon", ch) or re.search("in the evening", ch):
         ch = re.sub("in the afternoon", "", ch)
         ch = re.sub("in the evening", "", ch)
         exactTime = str(int(exactTime) + 1200)
       elif len(exactTime)==3 and int(exactTime)>0:
         exactTime = ["0"] + exactTime
       Date = Date + str(exactTime)
       Date = re.sub("[^0-9]", "", Date)
       if len(Date)==4:
         ch = re.sub("at", "", ch)
         Date = datetime.today().strftime('%Y%m%d') + Date

       if len(Date)!=12:
         print("Please enter a valid date.\n")
         continue

       eventName = re.sub("[^a-zA-Z ]", "", ch);
       eventName = eventName.strip()

       # conflict check
       flag = True
       if os.stat("Calendar/DataBase.db").st_size != 0:
          for datE in assignment:
             targetTime = datetime.strptime(datE, "%Y%m%d%H%M") # datetime type
             compTime = datetime.strptime(Date, "%Y%m%d%H%M")   # datetime type
             diffTime = compTime - targetTime     # calculate the time difference
             if diffTime<timedelta(minutes=0):    # absolute value
                diffTime = -diffTime
             if diffTime <= timedelta(minutes=60): # if the absolute value of difference is less than an hour
                print("\n" + str(assignment[datE]) + " is "+ datE)    # print warning message
                ans =raw_input("Are you sure want to insert the event? (y/n)\n")
                if ans=="y" or ans=="yes" or ans=='' or ans=='yup' or ans=='yeah' or ans=='Hell Yeah' or ans=='hell yeah':
                   continue
                else:
                   flag = False
                   break
          # end for
       # end if

       if flag:   # if approved to insert the event
          assignment[Date] = eventName
          print bcolors.WARNING + bcolors.BOLD + "map succeeded" + bcolors.ENDC
       # end if
     elif re.search("agenda", ch) or re.search('schedule', ch) or re.search("calendar", ch) or re.search("my plan", ch) or re.search("My plan", ch) or re.search("Schedule", ch) or re.search("Agenda", ch) or re.search("Calendar", ch):
       listEvents()
     elif charArray[0]=='I':
       ch = re.sub("\.", "", ch)
       ch += ", too."
       print ch
     else:
       ch = re.sub("\?", "!", ch)
       ch = re.sub("What's your name", "I am ToDo App", ch)
       ch = re.sub("What is your name", "I am ToDo App", ch)
       ch = re.sub("Who are you", "I am ToDo App", ch)
       ch = re.sub("What can you do", "I can do anything", ch)

       ch = re.sub("Are you", "Yes, I am", ch)
       ch = re.sub("are you", "am I", ch)
       ch = re.sub("Can you", "I can", ch)
       ch = re.sub("you are", "I am", ch)
       ch = re.sub("You are", "I am", ch)
       ch = re.sub("Is that", "That is", ch)
       ch = re.sub("Is it", "It is", ch)

       ch = re.sub("Your", "My", ch)
       ch = re.sub("your", "my", ch)
       ch = re.sub("You", "I", ch)
       ch = re.sub("you", "I", ch)
       ch = re.sub(" me", " you", ch)
       ch = re.sub("No", "Yes", ch);
       print ch
     print ""   # print a newline

   # end if-else
# end while

if os.stat("Calendar/DataBase.db").st_size != 0:    # if the database is not empty
    try:
       inputFile.close()
    except:
       a = 1  # do nothing instead
if os.stat("Calendar/Weekly.db").st_size != 0:    # if the weekly file was originally not empty
    nextWeek.close()


