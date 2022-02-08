def serialize(skeleton, values):

    serialized = dict()

    for i, key in enumerate(skeleton):
        serialized[key] = values[i]

    return serialized
