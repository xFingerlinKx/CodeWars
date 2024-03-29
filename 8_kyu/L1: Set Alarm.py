"""
Write a function named setAlarm which receives two parameters.
The first parameter, employed, is true whenever you are employed and the second parameter,
vacation is true whenever you are on vacation.

The function should return true if you are employed and not on vacation (because these are the
circumstances under which you need to set an alarm). It should return false otherwise.

Examples:

setAlarm(true, true) -> false setAlarm(false, true) -> false setAlarm(false, false) -> false setAlarm(true, false) -> true

setalarm(true, true) -> false
setalarm(false, true) -> false
setalarm(false, false) -> false
setalarm(true, false) -> true
"""


def set_alarm_1(employed, vacation):
    return True if employed and not vacation else False


def set_alarm_2(employed, vacation):
    return employed and not vacation


def set_alarm_3(employed, vacation):
    if employed:
        if vacation:
            return False
        return True
    return False
