def comparator(old_info, new_info):
    if new_info == old_info or new_info == "":
        return False

    elif new_info != old_info:
        return True