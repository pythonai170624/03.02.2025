from typing import override

from Billhandler import BillHandler

class Bill20(BillHandler):

    @override
    def handle(self, amount) -> None:
        left = amount
        if amount >= 20:
            print(f"Giving 50 X {amount // 20}")
            left = amount - (amount // 20) * 20

        if amount % 20 > 0:  # left > 0
            if self.next:
                self.next.handle(amount % 20)