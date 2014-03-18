from django_nav import nav_groups, Nav, NavOption

from archiver.conditionals import user_can_manage, user_can_see

class APIOption(NavOption):
    name = u'API'
    url = '/acm_members/api/'

class ManageOption(NavOption):
    """
    This is an Option of an Option, this can go on for the max
    recursion depth of python (Further then you want to try and go)
    """
    name = u'Manage'
    icon = ''
    view = ''
    conditional = {'function': user_can_manage, 'args': [], 'kwargs': {'app_label':'acm_members'}}

class DashboardOption(NavOption):
    name = u'Dashboard'
    view = 'acm_members.views.dashboard'

class AcmMembersNav(Nav):
    """
        This is a primary Navigation link, Most apps should only define one of these
        If the application truly wants to have Navigation links for all of their landing pages
        They can use the NavOption and have the main Nav with their Home state
    """
    name = u'ACM Members'
    icon = 'cog'
    nav_group = 'apis'
    options = [DashboardOption, ManageOption, APIOption]
    conditional = {'function': user_can_see, 'args': [], 'kwargs': {'app_label':'acm_members'}}

nav_groups.register(AcmMembersNav)
