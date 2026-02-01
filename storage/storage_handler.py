import csv
import os
from models.job_application import JobApplication

class StorageHandler:
    FIELDNAMES = [
        "application_id",
        "company_name",
        "role",
        "location",
        "date_applied",
        "status",
        "application_link",
        "notes"
    ]

    def __init__(self, file_path):
        self.file_path = file_path
        self._initialize_file()

    def _initialize_file(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=self.FIELDNAMES)
                writer.writeheader()

    def load_all(self):
        applications = []

        with open(self.file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                application = JobApplication.from_dict(row)
                applications.append(application)

        return applications

    def save_all(self, applications):
        with open(self.file_path,mode="w",newline="",encoding="utf-8") as file:
            writer = csv.DictWriter(file,fieldnames=self.FIELDNAMES)
            writer.writeheader()

            for application in applications:
                writer.writerow((application.to_dict()))

    def append(self, application):
        with open(self.file_path, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.FIELDNAMES)
            writer.writerow(application.to_dict())

