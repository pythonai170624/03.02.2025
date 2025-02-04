from typing import override

from Billhandler import BillHandler

class Bill200(BillHandler):

    @override
    def handle(self, amount) -> None:
        left = amount
        if amount >= 200:
            print(f"Giving 200 X {amount // 200}")
            left = amount - (amount // 200) * 200

        # 250 % 200 == 50
        # 420 % 200 = 20
        # 800 % 200 = 0
        if amount % 200 > 0:  # if left > 0:
            if self.next:
                self.next.handle(amount % 200)

