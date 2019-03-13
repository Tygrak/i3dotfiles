import gtk.gdk
import os
import datetime

w = gtk.gdk.get_default_root_window()
sz = w.get_size()
print "The size of the window is %d x %d" % sz
pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
if (pb != None):  
    currenttime = datetime.date.today()
    ctime = datetime.datetime.time(datetime.datetime.now())
    time = ""
    if(len(str(ctime.hour)) == 1):
        time += "0" + str(ctime.hour) + ":"
    else:
        time += str(ctime.hour) + ":"
    if(len(str(ctime.minute)) == 1):
        time += "0" + str(ctime.minute) + ":"
    else:
        time += str(ctime.minute) + ":"
    if(len(str(ctime.second)) == 1):
        time += "0" + str(ctime.second)
    else:
        time += str(ctime.second)
    filename = currenttime.strftime('%Y-%m-%d-') + time + "-screen.png"
    path = "/home/tygrak/Pictures/ScreenShots"
    fullpath = os.path.join(path, filename)
    pb.save(fullpath,"png")
    print "Screenshot saved to " + filename
else:
    print "Unable to get the screenshot."