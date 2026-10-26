
# Bus Passenger Occupancy Simulation

# Input bus details
capacity = int(input("Enter maximum bus capacity: "))
passengers = int(input("Enter initial number of passengers: "))
stops = int(input("Enter number of stops: "))

# Validate initial passenger count
if capacity <= 0 or passengers < 0 or passengers > capacity:
    print("Invalid bus capacity or initial passenger count.")

else:
    total_boarded = 0
    total_alighted = 0
    violations = 0

    print("\n--- BUS OCCUPANCY REPORT ---")
    print("Initial passengers:", passengers)

    for i in range(1, stops + 1):
        print("\nStop", i)

        boarding = int(input("Enter passengers boarding: "))
        alighting = int(input("Enter passengers alighting: "))

        # Validate passenger counts
        if boarding < 0 or alighting < 0:
            print("Invalid count! Counts cannot be negative.")
            print("Stop ignored.")
            continue

        elif alighting > passengers:
            print("Invalid transaction! More passengers alighting than onboard.")
            print("Stop ignored.")
            continue

        # Calculate passenger count
        passengers = passengers - alighting + boarding

        total_boarded += boarding
        total_alighted += alighting

        print("Passengers after stop:", passengers)

        # Check capacity violation
        if passengers > capacity:
            print("WARNING: Bus capacity exceeded!")
            violations += 1
        else:
            print("Status: Within capacity.")

    # Final report
    print("\n===== FINAL BUS REPORT =====")
    print("Bus capacity:", capacity)
    print("Final passengers:", passengers)
    print("Total passengers boarded:", total_boarded)
    print("Total passengers alighted:", total_alighted)
    print("Capacity violations:", violations)

    if violations == 0:
        print("Result: No capacity violations.")
    else:
        print("Result: Capacity violations detected.")
