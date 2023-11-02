class ReservationSystem:
    def __init__(user):
        user.reservations = []

    def makeReservation(user):
        print("MAKE RESERVATIONS")
        name = input("Name: ")
        date = input("Date (mm-dd-yyy): ")
        time = input("Time: ")
        adults = int(input("No. of adults: "))
        children = int(input("No. of children: "))

        reservation_id = len(user.reservations) + 1
        payment = (adults * 500) + (children * 250)

        reservation_details = {
            "ID": reservation_id,
            "Name": name,
            "Date": date,
            "Time": time,
            "Adults": adults,
            "Children": children,
            "Payment": payment,
        }

        user.reservations.append(reservation_details)
        print("Reservation made successfully.")

    def viewReservation(user):
        print("VIEW RESERVATIONS")
        if not user.reservations:
            print("No reservations found.")
            return

        print("# Date Time Name Adults Children")
        for reservation in user.reservations:
            print(
                f"{reservation['ID']} {reservation['Date']} {reservation['Time']} {reservation['Name']} {reservation['Adults']} {reservation['Children']}"
            )

    def updateReservation(user):
        print("UPDATE RESERVATIONS")
        if not user.reservations:
            print("No reservations found.")
            return

        try:
            update_id = int(input("Enter ID no. to update: "))
        except ValueError:
            print("Please enter valid ID no.")
            return

        found = False
        for reservation in user.reservations:
            if reservation['ID'] == update_id:
                found = True
                print("Enter the new details")
                reservation['Name'] = input("Update Name: ")
                reservation['Date'] = input("Update Date: ")
                reservation['Time'] = input("Update Time: ")
                reservation['Adults'] = int(input("Update No. of Adults: "))
                reservation['Children'] = int(input("Update No. of Children: "))
                reservation['Payment'] = (reservation['Adults'] * 500) + (reservation['Children'] * 250)
                print("Reservation updated successfully.")
                
                print("# Date Time Name Adults Children")
                print(f"{reservation['ID']} {reservation['Date']} {reservation['Time']} {reservation['Name']} {reservation['Adults']} {reservation['Children']}")
                break

        if not found:
            print("No record found.")

    def deleteReservation(user):
        print("DELETE RESERVATIONS")
        if not user.reservations:
            print("No reservations found.")
            return

        try:
            delete_id = int(input("Enter ID no. to remove: "))
        except ValueError:
            print("Please enter valid ID no.")
            return

        found = False
        for reservation in user.reservations:
            if reservation['ID'] == delete_id:
                found = True
                user.reservations.remove(reservation)
                print(f"Reservation number {delete_id} is deleted.")
                break

        if not found:
            print("Reservation number not found.")

        if found:
            if user.reservations:
                print("# Date Time Name Adults Children")
                for reservation in user.reservations:
                    print(f"{reservation['ID']} {reservation['Date']} {reservation['Time']} {reservation['Name']} {reservation['Adults']} {reservation['Children']}")
            else:
                print("No remaining reservations.")

    def generateReport(user):
        print("GENERATE REPORT")
        if not user.reservations:
            print("No reservations found.")
            return

        total_adults = sum(reservation['Adults'] for reservation in user.reservations)
        total_children = sum(reservation['Children'] for reservation in user.reservations)
        grand_total = sum(reservation['Payment'] for reservation in user.reservations)

        print("# Date Time Name Adults Children Payment")
        for reservation in user.reservations:
            print(f"{reservation['ID']} {reservation['Date']} {reservation['Time']} {reservation['Name']} {reservation['Adults']} {reservation['Children']} {reservation['Payment']}")

        print(f"Total number of adults: {total_adults}")
        print(f"Total number of Kids: {total_children}")
        print(f"Grand Total: PHP {grand_total:.2f}")

    def start(user):
        while True:
            print("\nRESTAURANT RESERVATION SYSTEM")
            print("System Menu:")
            print("a. Make Reservation")
            print("b. View Reservations")
            print("c. Update Reservation")
            print("d. Delete Reservation")
            print("e. Generate Report")
            print("f. Exit")

            choice = input("\nEnter your choice: ").lower()

            if choice == 'a':
                user.makeReservation()
            elif choice == 'b':
                user.viewReservation()
            elif choice == 'c':
                user.updateReservation()
            elif choice == 'd':
                user.deleteReservation()
            elif choice == 'e':
                user.generateReport()
            elif choice == 'f':
                print("Thank you for using the RESERVATION SYSTEM!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    system = ReservationSystem()
    system.start()