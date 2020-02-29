def returnDayOfTheWeek(s, k):
    """Question 1 - Given, s = "Sat" and k = 23, the function should return Mon - Python (copy and
    paste it in an online editor to run this code or run it on Atom IDE, any Python IDE ... etc) """
# weekDays list
    weekDays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# dayIndex of weekDays
    dayIndex = weekDays.index(s)
# return the remainder - in our case %7 ((index+k)/7)
    return weekDays[(dayIndex + k) % 7]

print(returnDayOfTheWeek("Sat", 500))
