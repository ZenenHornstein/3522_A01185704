class Budget:

    """
    Prelim structure for budget DS
     {
    cust_id: {
        catagories: {
            catagory_1: {
                budget: 10
                balance: 10
                locked: bool
                }

            }
        }
    }
    """
    @staticmethod
    def create_test_budget():
        """
        Used for testing.
        :return:
        """
        test_budget = {
            "categories": {
                "games and entertainment": {
                    "budget": 100,
                    "balance": 0,
                    "locked": False
                },
                "Clothing and Accessories": {
                    "budget": 25,
                    "balance": 0,
                    "locked": False
                },
                "Eating Out": {
                    "budget": 50,
                    "balance": 0,
                    "locked": False
                },
                "Misc": {
                    "budget": 50,
                    "balance": 0,
                    "locked": False
                }

            }
        }
        return Budget(**test_budget)

    def __init__(self, **kwargs):
        self._categories = kwargs["categories"]

    def __str__(self):
        return F"\nGames and Entertainment: \n\t Budget:{self._categories['games and entertainment']['budget']} \n\t Balance:{self._categories['games and entertainment']['balance']} \n\t LockStatus {self._categories['games and entertainment']['locked']}" \
               F"\nClothing and Accessories: \n\t Budget:{self._categories['Clothing and Accessories']['budget']} \n\t Balance:{self._categories['Clothing and Accessories']['balance']} \n\t LockStatus {self._categories['Clothing and Accessories']['locked']}" \
               F"\nEating Out: \n\t Budget:{self._categories['Eating Out']['budget']} \n\t Balance:{self._categories['Eating Out']['balance']} \n\t LockStatus {self._categories['Eating Out']['locked']}" \
               F"\nMisc: \n\t Budget:{self._categories['Misc']['budget']} \n\t Balance:{self._categories['Misc']['balance']} \n\t LockStatus {self._categories['Misc']['locked']}"



