import math
from PIL import Image
import blurs

imagen = Image.open("Michelangelo's_David.png")

imagen = imagen.convert("RGB")

imagen.show()

newone = blurs.errorDiff(imagen)

newone.show()