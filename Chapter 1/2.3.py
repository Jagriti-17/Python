#  Start the Python interpreter and use it as a calculator. 

# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?

# Solution:

time_in_minutes=42+42/60
time_in_hours=time_in_minutes/60

distance_in_km=10
distance_in_miles=distance_in_km/1.61

average_pace=time_in_minutes/distance_in_miles
average_speed=distance_in_miles/time_in_hours

print(average_pace)
print(average_speed)
