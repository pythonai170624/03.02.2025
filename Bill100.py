from typing import override

from Billhandler import BillHandler

class Bill100(BillHandler):

    @override
    def handle(self, amount) -> None:
        left = amount
        if amount >= 100:
            print(f"Giving 100 X {amount // 100}")
            left = amount - (amount // 100) * 100

        if amount % 100 > 0:  # left > 0
            if self.next:
                self.next.handle(amount % 100)