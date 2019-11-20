# Adds a self-referential canonical tag to every page
def processor(request):
    context = {
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    return context
