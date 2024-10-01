Weather Man

Attached files contain weather data for different areas and different time spans. Write an application that generates the following reports.

1. For a given year display the highest temperature and day, lowest temperature and day, most humid day and humidity.

ruby weatherman.rb -e 2002 /path/to/filesFolder
Highest: 45C on June 23
Lowest: 01C on December 22
Humid: 95% on August 14

2. For a given month display the average highest temperature, average lowest temperature, average humidity.

ruby weatherman.rb -a 2005/6 /path/to/files
Highest Average: 39C
Lowest Average: 18C
Average Humidity: 71%

3. For a given month draw two horizontal bar charts on the console for the highest and lowest temperature on each day. Highest in red and lowest in blue.

ruby weatherman.rb -c 2011/03 /path/to/files
March 2011
01 ++++++++++++++++++++++++ 25C
01 +++++++++++ 11C
02 +++++++++++++++++++++ 22C
02 ++++++++ 08C

4. BONUS TASK. For a given month draw one horizontal bar chart on the console for the highest and lowest temperature on each day. Highest in red and lowest in blue.

ruby weatherman.rb -c 2011/3 /path/to/files
March 2011
01 +++++++++++++++++++++++++++++++++++ 11C - 25C
02 +++++++++++++++++++++++++++++ 08C - 22C


In case of any question, please feel free to ask.
