import matplotlib.pyplot as plt
import csv

def record_expenses():
    expenses = {}
    while True:
        category = input("Enter expense category (or type 'done' to finish): ").strip()
        if category.lower() == 'done':
            break
        amount = float(input("Enter expense amount for {}: ".format(category)))
        expenses[category] = expenses.get(category, 0) + amount
    return expenses

def display_pie_chart(expenses):
    labels = expenses.keys()
    values = expenses.values()

    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Expense Distribution')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def export_to_csv(expenses):
    with open('expenses.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Category', 'Amount'])
        for category, amount in expenses.items():
            writer.writerow([category, amount])

def load_expenses_from_csv():
    try:
        with open('expenses.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            expenses = {row[0]: float(row[1]) for row in reader}
        return expenses
    except FileNotFoundError:
        return {}

def analyze_expenses(expenses):
    total_expenses = sum(expenses.values())
    print("Total expenses:", total_expenses)

    if expenses:
        max_category = max(expenses, key=expenses.get)
        min_category = min(expenses, key=expenses.get)
        print("Category with highest expense:", max_category, "- Amount:", expenses[max_category])
        print("Category with lowest expense:", min_category, "- Amount:", expenses[min_category])
    else:
        print("No expenses recorded.")

def edit_expenses(expenses):
    print("Current expenses:")
    for category, amount in expenses.items():
        print("- {}: ${}".format(category, amount))
    while True:
        category_to_edit = input("Enter the category to edit (or type 'done' to finish): ").strip()
        if category_to_edit.lower() == 'done':
            break
        if category_to_edit not in expenses:
            print("Category not found. Please enter a valid category.")
            continue
        new_amount = float(input("Enter new amount for {}: ".format(category_to_edit)))
        expenses[category_to_edit] = new_amount
        print("Expense updated successfully.")

def delete_expense(expenses):
    print("Current expenses:")
    for category, amount in expenses.items():
        print("- {}: ${}".format(category, amount))
    category_to_delete = input("Enter the category to delete: ").strip()
    if category_to_delete in expenses:
        del expenses[category_to_delete]
        print("Expense deleted successfully.")
    else:
        print("Category not found. Please enter a valid category.")

if __name__ == "__main__":
    print("Welcome to the Personal Financial Budget Tracker!")

    # Load previously recorded expenses from CSV
    expenses = load_expenses_from_csv()

    # Record new expenses
    new_expenses = record_expenses()
    expenses.update(new_expenses)

    # Display pie chart of expenses
    display_pie_chart(expenses)

    # Export updated expenses to CSV file
    export_to_csv(expenses)

    # Analyze expenses
    analyze_expenses(expenses)

    # Edit expenses
    edit_expenses(expenses)

    # Delete an expense
    delete_expense(expenses)

    # Display pie chart of updated expenses
    display_pie_chart(expenses)

    # Export updated expenses to CSV file
    export_to_csv(expenses)

    print("Expenses recorded, analyzed, and exported successfully.")
