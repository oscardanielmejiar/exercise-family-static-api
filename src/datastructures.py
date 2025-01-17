
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self.members = [{
        "first_name": "Tommy",
        "last_name": self.last_name,
        "id": int(),
		"age": 23,
		"lucky_numbers": [32,12]
	}]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self) -> int:
        return randint(0, 99999999)

    def add_member(self, member: dict) -> None:
        # fill this method and update the return
        self.members.append(member)

    def delete_member(self, id):
        # fill this method and update the return
        pass

    def get_member(self, id):
        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self.members
