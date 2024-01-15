import sys

def cat_shelter(log_file):
    try:
        with open(log_file, 'rt') as file:
            lines = file.readlines()
            
        del lines[-1]

        # declaring variables
        our_cat_visits = 0
        their_cat_visits = 0
        total_stay = 0
        longest_visit = 0
        shortest_visit = float('inf')

        
        for line in lines:
            data = line.strip().split(',')

    
            which_cat = data[0]
            arriving_time = data[1]
            departing_time = data[2]

            arriving_time = int(arriving_time) 
            departing_time = int(departing_time)

            visit_duration = departing_time - arriving_time

            # for OURS
            if which_cat == "OURS":
                our_cat_visits += 1
                total_stay += visit_duration
                longest_visit = max(longest_visit, visit_duration)
                shortest_visit = min(shortest_visit, visit_duration)
                
            # for THEIRS
            elif which_cat == "THEIRS":
                their_cat_visits += 1
                
        # time in hours and minutes
        total_hours = total_stay // 60
        total_minutes = total_stay % 60
        avg_time = total_stay // our_cat_visits
        #avg_time = total_stay // max(1, our_cat_visits) #incase the our cat visits is 0.

        
        print("Log File Analysis")
        print("==================\n")
        print(f"Cat Visits: {our_cat_visits}")
        print(f"other Cats: {their_cat_visits}\n")
        print(f"Total Time in House: {total_hours} Hours, {total_minutes} Minutes\n")
        if avg_time < 60:
            print(f"Average Visit Length: {avg_time} Minutes")
        elif avg_time >= 60:
            print(f"Average Visit Length: {avg_time//60} hours , {avg_time % 60} minutes")
        print(f"Longest Visit: {longest_visit} Minutes")
        print(f"Shortest Visit: {shortest_visit} Minutes")

    except FileNotFoundError:
        print(f'Cannot open "{log_file}"!')

# to check if command-line argument is present
if len(sys.argv) > 2:
    print("Can only send one file at a time!")
elif len(sys.argv) < 2:
    print("Missing command line argument!")
else:
    # Analyze the cat shelter log file
    cat_shelter(sys.argv[1])





