def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    if phrase[0].islower():
        target = phrase[0]
        cap_it = phrase[0].upper()
        new_phrase = phrase.replace(target,cap_it,1)
       

    return new_phrase