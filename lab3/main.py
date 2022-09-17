# запитати чи це правильно
from stool import Stool
from chair import Chair


tab1 = Stool(50, 'average')
tab2 = Stool(40, 'high')
tab3 = Stool(50, 'low')
tab4 = Stool(50, 'low')
tab5 = tab1 * tab3
print(tab5.height)


if (tab1 == tab3): print("equal")
if (tab1 != tab2): print("not eq")
if (tab1 > tab3): print("greater equal")



# chair1 = Chair(50, 'high', 30)
# chair2 = Chair(40, 'average', 30)
# chair3 = Chair(30, 'average', 30)
# chair1 += chair2 + chair3
# print(chair1.height)

# print(chair1)
# print(chair1.height, chair1.quality, chair1.heightChairBack)
# print(chair1.WoodAmount())
