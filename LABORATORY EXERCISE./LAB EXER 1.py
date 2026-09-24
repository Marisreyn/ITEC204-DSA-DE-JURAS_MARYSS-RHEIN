# sample tickets (list of dictionaries)
tickets = [
    {"id": "INC1392939", "bot": "BOT-Inventory", "desc": "Failed to generate the daily report"},
    {"id": "INC1392940", "bot": "BOT-Email", "desc": "Failed to send the scheduled notification"},
    {"id": "INC1392941", "bot": "BOT-DataSync", "desc": "Encountered an error during data transfer"},
    {"id": "INC1392942", "bot": "BOT-Invoice", "desc": "Failed to process an invoice"},
    {"id": "INC1392943", "bot": "BOT-Report", "desc": "Failed to generate the weekly report"},
    {"id": "INC1392944", "bot": "BOT-FileTransfer", "desc": "Failed to upload the required file"},
    {"id": "INC1392945", "bot": "BOT-DataEntry", "desc": "Encountered an error while entering records"},
    {"id": "INC1392946", "bot": "BOT-Backup", "desc": "Failed to complete the scheduled backup"},
    {"id": "INC1392947", "bot": "BOT-Validation", "desc": "Failed to validate the submitted records"},
    {"id": "INC1392948", "bot": "BOT-Notification", "desc": "Failed to send the system alert"}
]

while True:
    print("\nIncident Ticket Manager")
    print("1. Add Ticket")
    print("2. Display Tickets")
    print("3. Search Ticket")
    print("4. Remove Ticket")
    print("5. Count Tickets")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        i = input("Incident ID: ")
        b = input("Bot: ")
        d = input("Description: ")
        tickets.append({"id": i, "bot": b, "desc": d})
        print("Ticket added!")

    elif choice == "2":
        for t in tickets:
            print(t["id"], "|", t["bot"], "|", t["desc"])

    elif choice == "3":
        i = input("Enter Incident ID: ")
        found = False
        for t in tickets:
            if t["id"] == i:
                print("Found:", t["id"], "|", t["bot"], "|", t["desc"])
                found = True
        if not found:
            print("Ticket not found.")

    elif choice == "4":
        i = input("Enter Incident ID to remove: ")
        removed = False
        for t in tickets:
            if t["id"] == i:
                tickets.remove(t)
                print("Ticket removed!")
                removed = True
                break
        if not removed:
            print("Ticket not found.")

    elif choice == "5":
        print("Total tickets:", len(tickets))

    elif choice == "6":
        print("Exit program...")
        break

    else:
        print("Invalid choice.")
