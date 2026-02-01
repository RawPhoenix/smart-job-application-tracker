from datetime import datetime

class JobApplication:
    VALID_STATUSES = [
        "Applied",
        "Interview",
        "Rejected",
        "Offer",
        "Withdrawn",
        "Other"
    ]

    def __init__(self, application_id, company_name, role, location,
                 date_applied, status, application_link="", notes=""):

        if status not in self.VALID_STATUSES:
            raise ValueError("Invalid application status")

        if not isinstance(date_applied, datetime):
            raise TypeError("date_applied must be a datetime object")

        self.application_id = application_id
        self.company_name = company_name
        self.role = role
        self.location = location
        self.date_applied = date_applied
        self.status = status
        self.application_link = application_link
        self.notes = notes

    def to_dict(self):
        return {
            "application_id": self.application_id,
            "company_name": self.company_name,
            "role": self.role,
            "location": self.location,
            "date_applied": self.date_applied.isoformat(),
            "status": self.status,
            "application_link": self.application_link,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            application_id=int(data["application_id"]),
            company_name=data["company_name"],
            role=data["role"],
            location=data["location"],
            date_applied=datetime.fromisoformat(data["date_applied"]),
            status=data["status"],
            application_link=data.get("application_link", ""),
            notes=data.get("notes", "")
        )
