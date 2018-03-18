#begin

import gtk,webkit
import pygtk
import tkMessageBox as m
import Tkinter
from backblazeb2 import BackBlazeB2
from stem import Signal
import os
from stem.control import Controller
root=Tkinter.Tk()
root.withdraw()
import tkFileDialog
import shutil
import os
from urllib import urlretrieve
#WOW
global table
class Doge():

    def __init__(self):
        # Create window
        self.much_window = gtk.Window()
        #self.much_window.set_icon_from_file('doge.png')
        self.much_window.connect('destroy', lambda w: gtk.main_quit())
        self.much_window.set_default_size(1000, 700)
	
	
	# Create navigation bar
        self.so_navigation = gtk.HBox()
	
	
        self.many_back = gtk.ToolButton(gtk.STOCK_GO_BACK)
        self.such_forward = gtk.ToolButton(gtk.STOCK_GO_FORWARD)
        self.very_refresh = gtk.ToolButton(gtk.STOCK_REFRESH)
	self.newwindow=gtk.ToolButton(gtk.STOCK_NEW)
        self.test_tor_connect = gtk.ToolButton(gtk.STOCK_CONNECT)
        self.test_tor_disconnect=gtk.ToolButton(gtk.STOCK_DISCONNECT)
        self.log=gtk.ToolButton(gtk.STOCK_DIALOG_AUTHENTICATION)
        self.wow_address_bar = gtk.Entry()
        self.file=gtk.ToolButton(gtk.STOCK_FILE)
        self.video=gtk.ToolButton(gtk.STOCK_MEDIA_RECORD)
	self.sync=gtk.ToolButton(gtk.STOCK_GO_UP)
	self.account=gtk.ToolButton(gtk.STOCK_OPEN)
	self.newtabopen=gtk.ToolButton(gtk.STOCK_MEDIA_NEXT)
	
	

        self.many_back.connect('clicked', self.go_back)
        self.such_forward.connect('clicked', self.go_forward)
        self.very_refresh.connect('clicked', self.refresh_page)
	self.newwindow.connect("clicked",self.newwind)
        self.wow_address_bar.connect('activate', self.load_page)
        self.test_tor_connect.connect('clicked',self.torstart)
	self.test_tor_disconnect.connect("clicked",self.torstop)
        self.log.connect("clicked",self.lodlog)
        self.file.connect("clicked",self.loadfile)
        self.video.connect("clicked",self.loadvideo)
        self.sync.connect("clicked",self.syncing)
	self.account.connect("clicked",self.accountinfo)
	self.newtabopen.connect("clicked",self.newt1)

        self.so_navigation.pack_start(self.many_back, False)
        self.so_navigation.pack_start(self.such_forward, False)
        self.so_navigation.pack_start(self.very_refresh, False)
	self.so_navigation.pack_start(self.newwindow,False)
        self.so_navigation.pack_start(self.test_tor_connect, False)
	self.so_navigation.pack_start(self.test_tor_disconnect,False)
       	self.so_navigation.pack_start(self.log,False)
        self.so_navigation.pack_start(self.wow_address_bar)
        self.so_navigation.pack_start(self.file,False)
        self.so_navigation.pack_start(self.video,False)
	self.so_navigation.pack_start(self.sync,False)
	self.so_navigation.pack_start(self.account,False)
	self.so_navigation.pack_start(self.newtabopen,False)

        # Create view for webpage
        self.very_view = gtk.ScrolledWindow()
        self.such_webview = webkit.WebView()
        self.such_webview.open('http://google.com')
        self.such_webview.connect('title-changed', self.change_title)
        self.such_webview.connect('load-committed', self.change_url)
        self.such_webview.connect('download-requested', self.download_requested)
	self.such_webview.connect('mime-type-policy-decision-requested', self.policy_decision_requested)
	self.very_view.add(self.such_webview)


        #Settings
	self.settings=webkit.WebSettings()
	self.settings.set_property('enable-scripts', True)
        self.such_webview.set_settings(self.settings);

	
 
        # Add everything and initialize
        self.wow_container = gtk.VBox()
        self.wow_container.pack_start(self.so_navigation, False)
        self.wow_container.pack_start(self.very_view)
	if os.path.exists("temp"):
		shutil.rmtree("temp")
	os.mkdir("temp")
        self.much_window.add(self.wow_container)
        self.much_window.show_all()
        gtk.main()
	
    def download_requested(self,view,download):
      name = download.get_suggested_filename()
      path = os.getcwd()+"/temp/"+name
      urlretrieve(download.get_uri(), path) 
      return False

    def policy_decision_requested(self,view,frame,request, mimetype, policy_decision):
      if mimetype != 'text/html':
        policy_decision.download()
        return True

    def lodlog(self,widget):
       self.such_webview.open("http://smartbrowser.pythonanywhere.com")
       self.wow_address_bar.set_text("http://smartbrowser.pythonanywhere.com")

    def load_page(self, widget):
        so_add = self.wow_address_bar.get_text()
        if so_add.startswith('http://') or so_add.startswith('https://'):
            self.such_webview.open(so_add)
        else:
            so_add = 'http://' + so_add
            self.wow_address_bar.set_text(so_add)
            self.such_webview.open(so_add)

    def change_title(self, widget, frame, title):
        self.much_window.set_title('Smart Browser ' + title)

    def accountinfo(self , widget):
	os.system("chromium-browser --app=https://smartbrowser.pythonanywhere.com/data")

    def newwind(self , widget):
	wow1 = Doge()	

    def change_url(self, widget, frame):
        uri = frame.get_uri()
        self.wow_address_bar.set_text(uri)

    def go_back(self, widget):
        self.such_webview.go_back()

    def newt1(self, widget):
	self.much_window1 = gtk.Window()
        #self.much_window.set_icon_from_file('doge.png')
        self.much_window1.connect('destroy', lambda w: gtk.main_quit())
        self.much_window1.set_default_size(1000, 700)

    def go_forward(self, widget):
        self.such_webview.go_forward()

    def refresh_page(self, widget):
        self.such_webview.reload()

    def torstart(self,widget):
         m.showinfo("Warning","Tor Starting")
         os.system("sudo systemctl start tor.service")
         with Controller.from_port(port = 9051) as controller:
	    controller.authenticate(password='')
	    print("Success!")
	    controller.signal(Signal.NEWNYM)
	    print("New Tor connection processed")
    def torstop(self,widget):
	m.showinfo("Warining","Tor Stoping")
        os.system("sudo systemctl stop tor.service")
    def loadfile(self,widget):
       path=tkFileDialog.askopenfilename()
       fi=open(path,'rb+')
       l=fi.read().split(".")
       data=l[0].split(" ")
       st=""
       for i in data:
         st=st+i+"+"
       self.such_webview.open("http://google.com/search?q="+st)
       self.wow_address_bar.set_text("http://google.com/search?q="+st)
    def loadvideo(self,widget):
       os.system("chromium-browser --app=https://smartbrowser2.pythonanywhere.com")
    def syncing(self,widget):
        s=os.listdir("temp")
        f=[]
        for i in s:
           f.append("temp/"+i)
        for i in f:
         try:
            b2 = BackBlazeB2("4f42d08b88de","000d67122d844449b6f3c77d6f79bd7dde49a3ddcb")
            print 1
            b2.upload_file(i, bucket_name='amalamal')
            print "success"
         except Exception,e:
            print e
wow = Doge()






