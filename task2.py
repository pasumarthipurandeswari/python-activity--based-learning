
# Campus Event Financial Planning

# Input event expenses
venue_cost = float(input("Enter venue cost: "))
equipment_cost = float(input("Enter equipment cost: "))
catering_cost = float(input("Enter catering cost per participant: "))
transport_cost = float(input("Enter transport cost per participant: "))
certificate_cost = float(input("Enter certificate cost per participant: "))

# Input financial details
participants = int(input("Enter expected number of participants: "))
registration_fee = float(input("Enter registration fee per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))

# Calculate costs
fixed_cost = venue_cost + equipment_cost
variable_cost = catering_cost + transport_cost + certificate_cost

total_variable_cost = variable_cost * participants
total_cost = fixed_cost + total_variable_cost

# Calculate income
participant_contribution = registration_fee * participants
total_funds = participant_contribution + sponsorship

# Calculate sponsorship shortfall
shortfall = max(0, total_cost - total_funds)

# Calculate surplus or deficit
balance = total_funds - total_cost

# Calculate minimum registrations to break even
contribution_per_participant = registration_fee - variable_cost

if contribution_per_participant > 0:
    required_registrations = max(
        0,
        int((fixed_cost - sponsorship +
             contribution_per_participant - 1e-9)
            / contribution_per_participant)
    )
    # Ensure the answer is rounded up correctly
    import math
    required_registrations = max(
        0,
        math.ceil((fixed_cost - sponsorship) /
                  contribution_per_participant)
    )
else:
    required_registrations = None

# Display results
print("\n--- CAMPUS EVENT FINANCIAL REPORT ---")
print("Fixed Costs:", fixed_cost)
print("Variable Cost per Participant:", variable_cost)
print("Total Event Cost:", total_cost)
print("Participant Contributions:", participant_contribution)
print("Sponsorship:", sponsorship)
print("Total Available Funds:", total_funds)
print("Sponsorship/Funding Shortfall:", shortfall)
print("Financial Balance:", balance)

if balance > 0:
    print("Status: Event has a surplus.")
elif balance < 0:
    print("Status: Event has a deficit.")
else:
    print("Status: Event breaks even.")

if required_registrations is not None:
    print("Minimum Registrations to Break Even:",
          required_registrations)
else:
    print("Break-even is not possible with the current "
          "registration fee and variable cost.")
