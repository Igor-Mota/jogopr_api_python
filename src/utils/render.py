
def render__one(argument):

    if isinstance(argument, str):
        return argument
    else:
        render = list(argument[0])
        render = render[:-1]
    return render


def render_many(array):
    elements = []

    for element in array:
        elements.append(element[:-1])
    return elements
