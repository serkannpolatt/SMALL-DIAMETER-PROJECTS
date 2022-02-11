import calendar
yil=int(input("takvim yılını giriniz:"))

cal=calendar.LocaleTextCalendar(0,"turkish")
cal.pryear(yil)