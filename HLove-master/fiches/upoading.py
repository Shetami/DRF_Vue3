def upload(instance, filename):
    return "{0}/{1}".format(instance.manga.slug, filename)  # на postgres тут какая то хуета творится
