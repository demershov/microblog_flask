from jinja2 import Markup


class momentjs(object):
    def __init__(self, date):
        self.date = date

    def render(self, format):
        return Markup("<script>\nmoment.locale('ru');\ndocument.write(moment(\"%s\").%s);\n</script>" % (self.date.strftime("%Y-%m-%dT%H:%M:%S Z"), format))

    def format(self, fmt):
        return self.render("format(\"%s\")" % fmt)

    def calendar(self):
        return self.render("calendar()")

    def fromNow(self):
        return self.render("fromNow()")
