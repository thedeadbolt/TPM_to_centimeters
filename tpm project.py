# This calculator's purpose is to convert TPM into a logarithmic scale of choice and then into centimeters.
# It's main purpose is to facilitate gene expression image making for research papers.
# 26/01/2025 made by thedeadbolt @ CIIMAR

import math  # for the logs

print("Welcome to the TPM to centimeters calculator!")
TPM = float(input("Please input your TPM value: "))
LG_CHOICE = int(input("What is your log of choice: log2 (1) or ln (2)?: "))

# Check if scale_choice is a valid number and non-zero
while True:
    scale_choice = float(input("What is the proportion? How many cm to 1 log/ln(TPM+1) ?: "))
    if scale_choice == 0:
        print("Scale choice cannot be zero. Please enter a non-zero number.")
    else:
        break

if LG_CHOICE == 1:
    LG2 = math.log2(TPM + 1)
    CENT = LG2 / scale_choice

elif LG_CHOICE == 2:
    LN = math.log(TPM + 1)  # (ln)
    CENT = LN / scale_choice

else:
    print("Invalid choice! Please select 1 for log2 or 2 for ln.")
    exit()

print(f"Your inputted TPM value in centimeters is: {CENT:.4f}")  # Output

