import random
import string


print("".join([random.choice(string.printable) for _ in range(24)]))
