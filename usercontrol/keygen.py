import random, string


def key_generator() -> str:
    """ Generate random secret key """

    secret_key = "".join([random.choice(string.printable) for _ in range(24)])
    return secret_key