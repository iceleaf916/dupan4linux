#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 ~ 2013 Deepin, Inc.
#               2012 ~ 2013 Kaisheng Ye
# 
# Author:     Kaisheng Ye <kaisheng.ye@gmail.com>
# Maintainer: Kaisheng Ye <kaisheng.ye@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gtk
from dtk.ui.browser import WebView
from loading_widget import Loading
import webkit

api_key = "tunONwA8nHpkCH8hxOzrAk29"
secret_key = "tS41qB5DBTDZftqGDoyCGLLEklOxPGyB"
login_url = "http://openapi.baidu.com/oauth/2.0/authorize?response_type=token&client_id=%s&redirect_uri=oob&scope=netdisk" % api_key

class MainWin(gtk.Window):
    def __init__(self):
        super(MainWin, self).__init__()

        self.set_size_request(600, 400)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)
        
        cookie_file = "/tmp/dupan4linux.txt"
        self.web_view = WebView(cookie_file)
        self.web_view.connect("notify::load-status", self.web_view_load_status)
        self.web_view.open(login_url)

        self.loading = Loading()
        
        self.main_vbox = gtk.VBox()
        self.main_vbox.pack_start(self.web_view)

        self.add(self.main_vbox)
        self.show_all()
        gtk.main()

    def web_view_load_status(self, web_view, status):
        state = web_view.get_property("load-status")
        uri = web_view.get_property("uri")
        if state == webkit.LOAD_COMMITTED:
            print "Commited:"
            print uri
        elif status == webkit.LOAD_FINISHED:
            print "Finished:"
            print uri.split("&")

MainWin()
