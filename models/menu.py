# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B(SPAN('T.o.t.M')),XML('&nbsp;'),
                  _class="brand",_href='../')
response.title = "T.o.t.M"
response.subtitle = "TYRANNY OF THE MAJORITY"

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'habib adam, nathan phennel'
response.meta.keywords = 'autocomplete game, google trivia, suggestion, play, search, search term, totm, tyranny of the majority, tyrany of the majority'
response.meta.generator = 'Tyranny of the Majority'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    
    (T('Home'), False, URL( 'default', 'index'), []),
    
    (T('About'), False, URL('default', 'about'), []),
]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
