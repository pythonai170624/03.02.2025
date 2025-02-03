from Bill100 import Bill100
from Bill200 import Bill200
from Bill50 import Bill50

chain200 = Bill200()
chain100 = Bill100()
chain50 = Bill50()

chain200.next = chain100
chain100.next = chain50
chain50.next = None  # just for clarification
print('handle 600')
chain200.handle(600)
print('handle 580')
chain200.handle(580)

# add Bill 20
# add coin 5
# attach them
# 980, 400, 575
# what if the 100 has been removed? handle 500
