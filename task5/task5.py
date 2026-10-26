
# Hospital Billing and Patient Classification

print("===== HOSPITAL BILLING SYSTEM =====")

# Input patient details
patient_name = input("Enter patient name: ")
patient_type = input("Enter patient type (General/Senior): ")

# Input charges
consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Validate billing constraints
if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Error: Charges cannot be negative.")

else:
    # Calculate total bill
    total_bill = consultation + diagnostic + treatment

    # Apply conditional concessions
    if patient_type.lower() == "senior":
        concession_rate = 10
    else:
        concession_rate = 0

    concession = total_bill * concession_rate / 100
    final_bill = total_bill - concession

    # Classify patient according to sample payment policy
    if final_bill <= 1000:
        payment_category = "Low Payment"
    elif final_bill <= 5000:
        payment_category = "Medium Payment"
    else:
        payment_category = "High Payment"

    # Display bill
    print("\n===== PATIENT BILL =====")
    print("Patient Name:", patient_name)
    print("Patient Type:", patient_type)
    print("Consultation Charges: Rs.", consultation)
    print("Diagnostic Charges: Rs.", diagnostic)
    print("Treatment Charges: Rs.", treatment)
    print("Total Bill: Rs.", total_bill)
    print("Concession: Rs.", concession)
    print("Final Bill: Rs.", final_bill)
    print("Payment Classification:", payment_category)
