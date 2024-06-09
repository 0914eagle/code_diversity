
def get_plural_form(singular_form):
    if singular_form.endswith('s'):
        return singular_form + 'es'
    else:
        return singular_form + 's'

