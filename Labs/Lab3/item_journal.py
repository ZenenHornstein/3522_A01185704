from item import Item

class Journal(Item):

    def __init__(self, call_number=None, name=None, issue_number=None, publisher=None):

        if not call_number:
            call_number = input("Please enter a call number for the journal. ")
        if not name:
            name = input("Please enter a name for the journal. ")
        if not publisher:
            publisher = input("Please enter a Publisher for the journal. ")
        if not issue_number:
            issue_number = int(input("Pleas enter a issue_number for the journal. "))

        super().__init__(call_number, name)
        self._publisher = publisher
        self._issue_number = issue_number




    def __str__(self):
        return f"---- Journal: {self._title} ----\n" \
               f"Call Number: {self._call_number}\n" \
               f"Issue Number: {self._issue_number}\n" \
               f"Publisher: {self._publisher}\n"\
               f"Number of copies : {self._num_copies}"

