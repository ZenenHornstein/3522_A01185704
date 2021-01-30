from item import Item


class DVD(Item):
    def __init__(self, call_number=None, name=None, release_date=None, region_code=None):

        if not call_number:
            call_number = input("Please enter a call number ")

        if not name:
            name = input("Please enter a name ")

        if not release_date:
            release_date = input("Please enter a release date. ")

        if not region_code:
            region_code = input("Please enter a region code ")

        super().__init__(call_number, name)

        self._release_date = release_date
        self._region_code = region_code

    def __str__(self):
        return f"---- DVD: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Release data: {self._release_date}\n" \
               f"Region code: {self._region_code}\n"\
               f"Number of copies {self._num_copies}"
