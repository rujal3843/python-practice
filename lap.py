num_laps = int(input('Enter number of laps you ran: '))


total_time = 0.0
lap_time_list = []

for lap in range(1,num_laps+1):
    lap_time = float(input('nEnter the lap time in minutes for each lap from first to last: '))
    total_time += lap_time
    lap_time_list.append(lap_time)


avg_time = total_time / num_laps
fast_lap = min(lap_time_list)
slowest_lap = max(lap_time_list)

# Display the time of fastest lap, slowest lap and average lap time

print('nAverage lap time:',avg_time,'mins')
print('nFastest lap time:',fast_lap,'mins')
print('nSlowest lap time:',slowest_lap,'mins')
