def processor(request):
    context = {
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    return context
