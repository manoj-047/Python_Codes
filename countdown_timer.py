import time

print("Countdown Timer ")
# Setting the duration of the countdown timer
duration = int(input("Enter the time duration for countdown: "))


def countdown_timer(seconds):
    while seconds >= 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)  # Pause for 1 second
        seconds -= 1
    print("Time's up!")


# Start the countdown timer
countdown_timer(duration)
