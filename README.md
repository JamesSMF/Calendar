===========================================
Welcome to Todo App developed by James Li.
This app is a schedule management app which
helps you to keep track on your working
process.

===========================================
Current Version: 2.1.1
This app is still under modification and
enhancement.

===========================================

Basic operations:

1. Enter "i" to insert a new event
-- After entering "i", you will be prompted to enter a 
   date. You can enter the date in any format you like 
	(e.g. 20180114 or 2018/04/26 or 2018-06-15). But be
	careful that year should come first followed by month 
	and date subsequently.
-- Then you will be prompted to enter a time. You can
   also enter the time in any format that you like.
	But hour should come before minute.

2. Enter "d" to delete an old event
-- Enter the name of the assignment which you want to
   delete to delete the assignment.

3. Enter "c" to check the date of a specific event

4. Enter "t" to get a list of things to do tomorrow

5. Enter "o" to get a list of things to do today

6. Enter "l" to get 10 deadline-in-the-ass events
-- In order not to make the screen seem messed. Only
   most recent 16 events will pop up. (enter "more"
	to show more)

7. Enter "r" to revise the date of a certain event

8. Press "q" to exit

=========================================== 

Features to mention:
~ When you start this app, old assignments (prior to today)
  will be automatically deleted.
~ Weekly schedule will always be in this app, no matter you
  delete it or not (this will be improved sooner or later).

===========================================




=========================================== 
Updated on Jan 16th, 2019.

Current Version: 2.2.1
===========================================

New features:
1. map function:
--- map <event name> <date and time>
--- This function accepts regular form of time (e.g. 201901161800), 
	 as well as date codes, such as "today" and "tomorrow"
--- For "today" or "tomorrow", there should be three inputs: 
    map <event name> <"today" or "tomorrow"> <specific time>

2. ls, rm ,and mv
--- Programmers should be familiar with these three commands
--- Note that mv is only used for changing name, if you want to 
    revise the date, just use map function

3. weekday auto-calculation
--- When you insert something, you can use weekday as date code. 
    For example, map whatever Mon 14:30 will map whatever to next 
	 upcoming Monday. So you don't have to worry about date calculation.

4. fixed some bugs in weekly calendar





=========================================== 
Updated on Jan 20th, 2019

Current Version 2.2.2
=========================================== 

New features:
-- Multi-deletion: use rm + <a list of shit to be deleted splited by 
   space>
-- Weekday manifestation: clearly shows the weekday of each event
-- Auto-save: everytime listing things out or inserting something in,
	the dict() gets automatically saved. So even if something happens,
	you are still able to keep your latest process undisrupted.




===========================================
Version 2.3.1

Release Date: Jan 22nd, 2019
===========================================

New Features:
-- Conflict check. When you insert something, the program automatically
   does schedule check to make sure that your agenda will not be too
	crowded.
-- Fixed some bugs regarding some basic operations.






===========================================
Version 3.1.1

Release Date: Jan 27th, 2019
===========================================

New Features:
-- Restructured the code. Now you can insert two events with the same
   name! (but at different times. You cannot, technically, do two 
	things at the simultaneously.)

	===============================================
   | previously: map event name to date and time |
   |     												    |
	| Now: map date and time to event name        |
	===============================================

-- Want to add space inside event name? Fed up with programmer style of
   naming events? No problem! Now you can.

-- HOWEVER, unfortunately, good things come along bad news. Multi-del
   function is no longer available now. BUT, don't get frustrated by
	that. James is working on a new solution to enable nulti-del and
	input with space simultaneously.






===========================================
Version 3.1.2

Release Date: Feb 1st, 2019
===========================================

New Features:
-- Colors of the text. If you are using ls, only events not in your
   weekly calendar will be highlighted.
-- Fixed some bugs in map function.
-- Time entry is enhanced. If you are entering 4:00, it will be
   converted to 16:00 aotumatically.
-- ls only shows most recent 16 activities. Want more? Just type "more".




===========================================
Version 3.2.1

Release Date: Feb 10th, 2019
===========================================

New Features:
-- Added a simple robot. You can chat with it!
-- You can type in natural language. This feature is still under
   development. The final goal is to fulfill natural language input.









===========================================
Version 3.2.2

Release Date: Feb 12th, 2019
===========================================

-- Improved the performance of the robot.
-- Added colors for titles so that it is more differentiable from
	commands and results.
-- fixed bugs in 'map' function for regular date mapping.



===========================================
Version 3.3.1

Release Date: March 22nd, 2019
===========================================

-- Added natural language map in psuedo-AI. For example: "I want to 
   have a hair cut tomorrow at 07:00" will be automatically mapped
	as "map have a hair cut tomorrow 0700 "






