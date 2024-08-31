
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
        self._members = []

    # def print_last_name(self):
    #     print(self.last_name)
    # read-only: Use this method to generate random members ID's when adding members into the list
    
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Add a member to the members list
        if "id" not in member:
            member["id"] = self._generateId()
        self._members.append(member)
        return member  # Returning the added member can be useful


    def delete_member(self, id):
        # fill this method and update the return
        self._members = list(filter(lambda member: member["id"] != id, self._members))
        
    def get_member(self, id):
        # Return a member from the members list by id
        for member in self._members:
            if member["id"] == id:
                return member
        return None
        
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
