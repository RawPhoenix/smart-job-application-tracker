from storage.storage_handler import StorageHandler
from services.application_manager import ApplicationManager
from cli.menu import run

def main():
    storage = StorageHandler("data/applications.csv")
    app_manager = ApplicationManager(storage)
    run(app_manager)

if __name__ == "__main__":
    main()