import time

# Countdown from 10 to 0
print("Countdown starts now:\n")

for i in range(10, -1, -1):
    print(i)
    time.sleep(1)  # Wait for 1 second

print("\nTime's up! ⏰")
