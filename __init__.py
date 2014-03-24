from archiver.models import ArchiverApp

app_info = {
    'name':'ACM Members',
    'app_label':'acm_members',
    'flavor_text':"Tell us about yourself!",
    'description':"ACM Members is a project for recording the current UofL SpeedACM Chapter Members and information about them.",
    'public':True,
    'github':"jgissend10/acm_members"
}

try:
    app = ArchiverApp.objects.get(app_label=app_info['app_label'])
    for key, value in app_info.iteritems():
        setattr(app, key, value)
    app.save()
except ArchiverApp.DoesNotExist:
    app = ArchiverApp(**app_info)
    app.save()
