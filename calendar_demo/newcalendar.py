"""
Extends the stdlib calendaring module to create calendars with extra information in them
"""
import calendar

class LinkyCalendar(calendar.HTMLCalendar):

    monthclass = "month"
    navlinkstext = ["&lt;&lt;","&gt;&gt;"]
    navlinksurl = "/{0}/{1}/"

    def formatday(self, day, weekday, data=None):
        """
        Returns a day as a table cell (With a link, if included)
        """
        if day == 0:
            return '<td class="noday">&nbsp;</td>'
        elif data == None:
            return '<td class="%s">%d</td>' % (self.cssclasses[weekday], day)
        else:
            return '<td class="%s"><a href="%s">%d</a></td>' % (self.cssclasses[weekday], data, day)

    def formatweek(self, theweek, data):
        """
        Returns a full week, with data
        """
        if data:
            s = ''.join(self.formatday(d,wd,data[d]) for (d,wd) in theweek)
        return "<tr>%s</tr>" % s
 
    def formatmonth(self, theyear, themonth, withyear=True, data=None, withnav=True):
        """
        Returns a full, formatted month
        """
        localdata = {a:None for a in self.itermonthdays(theyear,themonth)}
        if data:
            for key in data.keys():
                localdata[key] = data[key]
        v = []
        a = v.append
        a('<table class="{0}">'.format(self.monthclass))
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear,themonth):
            a(self.formatweek(week, localdata))
            a('\n')
        if withnav:
            a(self.formatnav(theyear, themonth))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)  

    def formatnav(self, year, month):
        """
        Returns a nav bar
        """
        def fix_date(month):
            if month < 10:
                month = "0" + str(month)
            return month
        if month == 1:
            last_url = self.navlinksurl.format(year-1, 12)
            next_url = self.navlinksurl.format(year, '02')
        else:
            if month == 12:
                next_url = self.navlinksurl.format(year+1, '01')
            else:
               next_url = self.navlinksurl.format(year, fix_date(month+1))
            last_url = self.navlinksurl.format(year, fix_date(month-1))
        return "<tr> <th colspan='7' class='nav'> <a href={0}>{1}</a> -- <a href={2}>{3}</a> </th> </tr>".format(
                                       last_url, self.navlinkstext[0], 
                                       next_url, self.navlinkstext[1],
                                                                    )



