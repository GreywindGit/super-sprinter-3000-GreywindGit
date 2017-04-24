def load_stories(filename):
    stories = list()
    id = 1
    try:
        with open(filename, 'r') as workfile:
            for line in workfile:
                stories.append(list(str(id)) + line.split(','))
                id += 1
    except FileNotFoundError:
        stories = None
    return stories
