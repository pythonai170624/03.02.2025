from typing import override

from Billhandler import BillHandler

class Bill50(BillHandler):

    @override
    def handle(self, amount) -> None:
        left = amount
        if amount >= 50:
            print(f"Giving 50 X {amount // 50}")
            left = amount - (amount // 50) * 50

        if amount % 50 > 0:  # left > 0
            if self.next:
                self.next.handle(amount % 50)