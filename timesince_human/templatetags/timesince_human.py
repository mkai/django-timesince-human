from django import template
from django.utils.translation import ugettext, ungettext
from django.utils import timezone

register = template.Library()


@register.filter(name='timesince_human')
def humanize_timesince(date):  # TODO: let user specify format strings
    """
    Returns a translated, humanized representation of the time delta between
    a given date and the current date.

    Originally from: http://djangosnippets.org/snippets/2275/

    """
    delta = timezone.now() - date

    num_years = delta.days / 365
    if (num_years > 0):
        return ungettext(u"%d year ago", u"%d years ago", num_years) % (
            num_years,)

    num_months = delta.days / 30
    if (num_months > 0):
        return ungettext(u"%d month ago", u"%d months ago",
            num_months) % num_months

    num_weeks = delta.days / 7
    if (num_weeks > 0):  # TODO: "last week" if num_weeks == 1
        return ungettext(u"%d week ago", u"%d weeks ago",
            num_weeks) % num_weeks

    if (delta.days > 0):  # TODO: "yesterday" if days == 1
        return ungettext(u"%d day ago", u"%d days ago",
            delta.days) % delta.days

    num_hours = delta.seconds / 3600
    if (num_hours > 0):  # TODO: "an hour ago" if num_hours == 1
        return ungettext(u"%d hour ago", u"%d hours ago",
            num_hours) % num_hours

    num_minutes = delta.seconds / 60
    if (num_minutes > 0):  # TODO: "a minute ago" if num_minutes == 1
        return ungettext(u"%d minute ago", u"%d minutes ago",
            num_minutes) % num_minutes

    return ugettext(u"just now")
