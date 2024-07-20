from dataclasses import dataclass, field
import json
from typing import Optional


@dataclass(slots=True)
class Contact:
    id: int | None = 0
    first: str = ""
    last: str = ""
    phone: str = ""
    email: str = ""
    errors: dict[str] = field(default_factory=dict)

    def contains(self, value: str) -> bool:
        for var in [self.first, self.last, self.phone, self.email]:
            if var is not None and value in str(var).lower():
                return True
        return False


class ContactStore:
    def __init__(self):
        self._contacts: list[Contact] = []

        with open("contacts.json", "r") as file:
            contacts: list[dict] = json.load(file)

        for contact in contacts:
            self._contacts.append(
                Contact(
                    contact.get("id"),
                    contact.get("first"),
                    contact.get("last"),
                    contact.get("phone"),
                    contact.get("email"),
                )
            )

    @property
    def count(self):
        return len(self._contacts)

    @property
    def contacts(self):
        return self._contacts

    def search(self, value: str) -> list[Contact]:
        return [c for c in self._contacts if c.contains(value)]

    def validate(self, contact: Contact, ignore: Optional[str] = None) -> bool:
        if not contact.email:
            contact.errors["email"] = "Email required"
        if not contact.email == ignore:
            if contact.email in [c.email for c in self._contacts]:
                contact.errors["email"] = "Email must be unique"
        if contact.id in [c.id for c in self._contacts]:
            contact.errors["id"] = "ID must be unique"
        return len(contact.errors) == 0

    def save(self, contact: Contact) -> bool:
        if not self.validate(contact):
            return False
        if contact.id is None:
            if len(self._contacts) == 0:
                contact.id = 0
            else:
                contact.id = max([c.id for c in self._contacts]) + 1
        # save to file
        self._contacts.append(contact)
        return True

    def find(self, contact_id: str) -> Contact | None:
        for contact in self._contacts:
            if str(contact.id) == contact_id:
                return contact
        return None

    def remove(self, contact_id: str) -> bool:
        for i, contact in enumerate(self._contacts):
            if str(contact.id) == contact_id:
                self._contacts.pop(i)
                return True
        return False
