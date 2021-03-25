from markupsafe import Markup  # inside template ??

mk = Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
print(mk)
#Markup(u'<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
mk = Markup.escape('<blink>hacker</blink>')
print(mk)
#Markup(u'&lt;blink&gt;hacker&lt;/blink&gt;')
mk = Markup('<em>Marked up</em> &raquo; HTML').striptags()
print(mk)
#u'Marked up \xbb HTML'