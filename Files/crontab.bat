@echo OFF 
SCHTASKS /Create /tn 5MON10 /tr "CMD /k cd /d \"G:\python apps\ImSleepy\" && python IamSleepy.py  5 55" /sc weekly /d MON /st 10:00 /et 10:55 /K
SCHTASKS /Create /tn 5MON16 /tr "CMD /k cd /d \"G:\python apps\ImSleepy\" && python IamSleepy.py  5 55" /sc weekly /d MON /st 16:00 /et 16:55 /K
SCHTASKS /Create /tn 3TUE10 /tr "CMD /k cd /d \"G:\python apps\ImSleepy\" && python IamSleepy.py  3 55" /sc weekly /d TUE /st 10:00 /et 10:55 /K
SCHTASKS /Create /tn 4TUE11 /tr "CMD /k cd /d \"G:\python apps\ImSleepy\" && python IamSleepy.py  4 55" /sc weekly /d TUE /st 11:00 /et 11:55 /K
SCHTASKS /Create /tn 3TUE16 /tr "CMD /k cd /d \"G:\python apps\ImSleepy\" && python IamSleepy.py  3 55" /sc weekly /d TUE /st 16:00 /et 16:55 /K
SCHTASKS /Create /tn 5WED11 /tr "CMD /k cd /d \"G:\python apps\ImSleepy\" && python IamSleepy.py  5 55" /sc weekly /d WED /st 11:00 /et 11:55 /K
SCHTASKS /Create /tn 6WED13 /tr "CMD /k cd /d \"G:\python apps\ImSleepy\" && python IamSleepy.py  6 55" /sc weekly /d WED /st 13:00 /et 13:55 /K
SCHTASKS /Create /tn 2THU11 /tr "CMD /k cd /d \"G:\python apps\ImSleepy\" && python IamSleepy.py  2 115" /sc weekly /d THU /st 11:00 /et 12:55 /K
SCHTASKS /Create /tn 7THU14 /tr "CMD /k cd /d \"G:\python apps\ImSleepy\" && python IamSleepy.py  7 55" /sc weekly /d THU /st 14:00 /et 14:55 /K
SCHTASKS /Create /tn 8THU16 /tr "CMD /k cd /d \"G:\python apps\ImSleepy\" && python IamSleepy.py  8 55" /sc weekly /d THU /st 16:00 /et 16:55 /K
SCHTASKS /Create /tn 6FRI14 /tr "CMD /k cd /d \"G:\python apps\ImSleepy\" && python IamSleepy.py  6 55" /sc weekly /d FRI /st 14:00 /et 14:55 /K
pause