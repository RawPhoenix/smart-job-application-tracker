from models.job_application import JobApplication

class ApplicationManager:
    def __init__(self, storage_handler):
        self.storage = storage_handler

    def _generate_new_id(self):
        applications = self.storage.load_all()

        if not applications:
            return 1

        return max(app.application_id for app in applications ) + 1

    def add_application(self, company_name, role, location,
                        date_applied, status, application_link="", notes=""):

        new_id = self._generate_new_id()

        job_application = JobApplication(
            new_id,
            company_name,
            role,
            location,
            date_applied,
            status,
            application_link,
            notes
        )

        self.storage.append(job_application)
        return job_application

    def update_status(self, application_id, new_status):
        applications = self.storage.load_all()

        for app in applications:
            if app.application_id == application_id:
                if new_status not in JobApplication.VALID_STATUSES:
                    raise ValueError("Invalid application status")

                app.status = new_status
                self.storage.save_all(applications)
                return app

        raise ValueError(f"Application with ID {application_id} not found")

    def withdraw_application(self, application_id):
        return self.update_status(application_id, "Withdrawn")

    def get_all_applications(self):
        return self.storage.load_all()

    def find_by_id(self, application_id):
        applications = self.storage.load_all()

        for app in applications:
            if app.application_id == application_id:
                return app

        raise ValueError(f"Application with ID {application_id} not found")

    def filter_by_status(self, status):
        if status not in JobApplication.VALID_STATUSES:
            raise ValueError("Invalid application status")

        applications = self.storage.load_all()
        return [app for app in applications if app.status == status]
