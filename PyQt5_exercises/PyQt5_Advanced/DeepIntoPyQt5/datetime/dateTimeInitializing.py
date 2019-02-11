#!/usr/bin/env python3

from PyQt5.QtCore import QDate , QTime , QDateTime , Qt, QLocale
d1 = QDate(2017, 12, 9)
t1 = QTime(18, 50, 59)
dt1 = QDateTime(d1, t1, Qt.LocalTime)
print("Datetime: {0}".format(dt1.toString()))
print("Date: {0}".format(d1.toString()))
print("Time: {0}".format(t1.toString()))

now = QDate.currentDate()
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))
datetime = QDateTime.currentDateTime()
print(datetime.toString())

dayOfWeek = now.dayOfWeek()
print(QDate.shortDayName(dayOfWeek))
print(QDate.longDayName(dayOfWeek))
locale = QLocale(QLocale.Russian, QLocale.RussianFederation)
print(locale.toString(now, 'dddd'))

# prints current time
time = QTime.currentTime()
print(time.toString(Qt.DefaultLocaleLongDate))

now = QDateTime.currentDateTime()
print("Local datetime: ", now.toString(Qt.ISODate))
print("Universal datetime: ", now.toUTC().toString(Qt.ISODate))
print("The offset from UTC is: {0} seconds".format(now.offsetFromUtc()))


# comparing two dates
d1 = QDate(2017, 4, 5)
d2 = QDate(2016, 4, 5)
if d1 < d2:
    print("{0} comes before {1}".format(d1.toString(Qt.ISODate), d2.toString(Qt.ISODate)))
else:
    print("{0} comes after {1}".format(d1.toString(Qt.ISODate),d2.toString(Qt.ISODate)))


print('-------------------------------------------------')
now = QDate.currentDate()
d = QDate(1945, 5, 7)
print("Days in month: {0}".format(d.daysInMonth()))
print("Days in year: {0}".format(d.daysInYear()))

print('-------------------------------------------------')
now = QDate.currentDate()
print("Day of month: {0}".format(now.day()))
print("Day of week: {0}".format(now.dayOfWeek()))
print("Day of year: {0}".format(now.dayOfYear()))

print('-------------------------------------------------')
xmas1 = QDate(2017, 12, 24)
xmas2 = QDate(2018, 12, 24)
now = QDate.currentDate()
dayspassed = xmas1.daysTo(now)
print("{0} days have passed since last XMas".format(dayspassed))
nofdays = now.daysTo(xmas2)
print("There are {0} days until next XMas".format(nofdays))
print('-------------------------------------------------')
now = QDateTime.currentDateTime()
print("Today:", now.toString(Qt.ISODate))
print("Adding 12 days: {0}".format(
now.addDays(12).toString(Qt.ISODate)))
print("Subtracting 22 days: {0}".format(
now.addDays(-22).toString(Qt.ISODate)))
print("Adding 50 seconds: {0}".format(
now.addSecs(50).toString(Qt.ISODate)))
print("Adding 3 months: {0}".format(
now.addMonths(3).toString(Qt.ISODate)))
print("Adding 12 years: {0}".format(
now.addYears(12).toString(Qt.ISODate)))
print("Time zone: {0}".format(now.timeZoneAbbreviation()))
if now.isDaylightTime():
    rint("The current date falls into DST time")
else:
    print("The current date does not fall into DST time")
print('-------------------------------------------------')
unix_time = now.toSecsSinceEpoch()
print('Unix time - ',unix_time)
d = QDateTime.fromSecsSinceEpoch(unix_time)
print('ISO date and time',d.toString(Qt.ISODate))

