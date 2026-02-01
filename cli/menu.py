from datetime import datetime
from models.job_application import JobApplication

def show_menu():
    print("=" * 40)
    print("Smart Job Application Tracker")
    print("=" * 40)
    print()
    print("1. Add application")
    print("2. View all applications")
    print("3. Update application status")
    print("4. Withdraw application")
    print("5. Filter applications by status")
    print("6. Exit")
    print()

def get_user_choice():
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        return -1

def print_application(application):
    print("-" * 30)
    print(f"Application ID : {application.application_id}")
    print(f"Company        : {application.company_name}")
    print(f"Role           : {application.role}")
    print(f"Location       : {application.location}")
    print(f"Date Applied   : {application.date_applied.strftime('%Y-%m-%d')}")
    print(f"Status         : {application.status}")
    print("-" * 30)


def run(app_manager):
    while True:
        show_menu()
        choice = get_user_choice()

        if choice == 1:
            company_name = input("Company Name:")
            role = input("Role:")
            location = input("Location:")
            try:
                date_str = input("Enter application date (YYYY-MM-DD): ")
                date_applied = datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                print("Enter the date in given format")
                continue
            print("Application Statuses: ")
            print("|".join(JobApplication.VALID_STATUSES))
            status = input("Status:").strip().title()

            application_link = input("Application Link:")
            notes = input("Notes:")
            try:
                application = app_manager.add_application(company_name,role,location,date_applied,status,application_link,notes)
                print(f"Your application is added with application-id: {application.application_id}")
            except ValueError as e:
                print(e)
                continue

        elif choice == 2:
            applications = app_manager.get_all_applications()
            if not applications:
                print("Sorry there are no applications to view.")
                continue
            print("---- All Job Applications ----")
            for app in applications:
                print_application(app)

        elif choice == 3:
            try:
                application_id = int(input("Enter the application id of the application you want to update: "))
            except ValueError:
                print("Invalid id")
                continue
            print("Application Statuses: ")
            print("|".join(JobApplication.VALID_STATUSES))
            new_status = input("Enter the new status:").strip().title()
            try:
                updated_application = app_manager.update_status(application_id,new_status)
                print(f"Your application status with application id : {application_id} is successfully updated to {updated_application.status} ")
            except ValueError as e :
                print(e)
                continue

        elif choice == 4:
            try:
                withdraw_id = int(input("Enter the application id of the application you want to withdraw: "))
            except ValueError:
                print("Invalid id")
                continue
            try:
                withdrawn_application = app_manager.withdraw_application(withdraw_id)
                print(f"Your application status with application id: {withdraw_id} is successfully withdrawn")
            except ValueError as e:
                print(e)
                continue

        elif choice == 5:
            print("Application Statuses: ")
            print(" | ".join(JobApplication.VALID_STATUSES))
            search_status = input("Enter the status you want applications for: ").strip().title()
            try:
                filtered_applications = app_manager.filter_by_status(search_status)
            except ValueError:
                print("Invalid Status")
                continue
            if not filtered_applications:
                print(f"Sorry there are no applications with status: {search_status}")
                continue
            print(f"---- Status:{search_status} Applications")
            for result in filtered_applications:
                print_application(result)


        elif choice == 6:
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please try again.")
