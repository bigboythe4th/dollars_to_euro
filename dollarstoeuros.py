
# dollars to euros
# Nate Webberrun
dollar = float(input("Enter dollar amount to be converted: "))
# Step 3:
euro = dollar * 0.94540
# Step 4:
# Use the print() to output the new euro amount with a label beforehand.
print("Converted amount in euros:", euro)
# Step 5:
while True:
    convert_again = input("Would you like to convert dollars to euros? (yes/no): ")
    if convert_again.lower() == "no":
        break
# Step 6:
# Create a Pull Request from the Development Branch to the Main Branch.
# Merge Pull Request into Main branch.