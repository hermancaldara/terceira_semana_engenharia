from subscribe.models import ShortCourse


def get_short_course(request, place):
    ShortCourse.objects.get(
        id=int(request.POST.get(place))
    )
