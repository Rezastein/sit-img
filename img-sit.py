from PIL import Image
from kav import k
bg = Image.open("img/sit.jpg")

r = Image.open("img/r.png")
y = Image.open("img/y.png")
b = Image.open("img/b.png")

k.a11()
bg.paste(r, (k.kav_[0], k.kav_[1]))
# bg.paste(r, (1240, 4310))
# bg.paste(r, (1520, 4490))
# bg.paste(r, (1730, 4570))
# bg.paste(r, (1960, 4610))

bg.show()
