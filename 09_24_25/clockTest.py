from clock import Clock, HourError, MinuteError, SecondError

c = None
hour = False
minute = False
second = False
while c == None:
    
    try:
        if not hour:
            h = int(input("Enter the clock hour: "))
            hour = True
        if not minute:
            m = int(input("Enter the clock minute: "))
            minute = True
        if not second:
            s = int(input("Enter the clock second: "))
            second = True
        c = Clock(h, m, s)
    except ValueError:
        print("The input is not a number.")
    except HourError as hrerr:
        print(hrerr)
        hour = False
    except MinuteError as minerr:
        print(minerr)
        minute = False
    except SecondError as secerr:
        print(secerr)
        second = False

plus_one_hr = Clock(23, 59, 59)

answer = c + plus_one_hr
print()