#!/usr/bin/python

import cgi, cgitb
import os
import time
import shutil

filepath  ="/usr/lib/cgi-bin/uploads/"
resultpath="/usr/lib/cgi-bin/results/"
recipepath="/usr/lib/cgi-bin/recipes/"
savepath  ="/usr/lib/cgi-bin/savefiles/"




f=open(savepath +'recipe.txt','r')
recipe=f.read()
f.close()
recipes=recipe.split(',')




cgitb.enable()
print "Content-Type: text/html"
print

print "<HTML><BODY>"
#print recipes[0]+'x<br>'

# start with the Buttons
print '<form action="/cgi-bin/uploadcgi_1.py" method="post" enctype="multipart/form-data">'

print "Select Operation :<br>"
print '<select name="operation">'
print '<option value="classify">classify</option>'
print '<option value="stylize_gatys">stylize_gatys</option>'
print '<option value="stylize_msg">stylize_msg</option>'
print '<option value="style_add">style_add</option>'
print '<option value="style_train">style_train</option>'
print '<option value="loopback">loopback</option>'
#print '<option selected value="' , recipes[0].strip(), '">',recipes[0].strip(),'</option>'

print '</select><br><br>'


print "Input styledir name (brad,sandy...) :<br>"
print '<input type="text" name="style" id="style"><br><br>'



print '</select><br><br>'


print "Select image to upload :<br>"
print '<input type="file"  name="fileToUpload" id="IDfileToUpload"><br><br>'

# select render options
#print 'Select style : candy,  composition_vii,  feathers,  la_muse mosaic,  starry_night,  the_scream,  udnie,  wave <br>'
#print '<input type="text" name="style"        id="IDstyle"><br><br>'

print "Press Go to upload image and apply operation :<br>"

print '<input type="submit" value="Go" name="submit"><br>'
print "</form>"


form = cgi.FieldStorage()
#print form
fileitem = form["fileToUpload"]

operation = form["operation"].value
style     = form["style"].value
print '> operation=' + operation + '<br>'
print '> style='     + style + '<br>'
print '> file='      + fileitem.filename + '<br>'




#file transfer
if fileitem.filename: #it has a name
  filepath+=fileitem.filename
  if fileitem.file: #it has data.
    with file(filepath, 'w') as outfile:
      outfile.write(fileitem.file.read())
    print "<br>"
    print ">The image you uploaded<br>"
    print "<img src=/uploads/"+fileitem.filename+">"
    print "<br>"
    print "<br>"


    #now write the recipe file to trigger the action
    recipefile=recipepath+'recipe.txt'
    f=open(recipefile,'w')

    f.write(
        operation    + ','
        + style      + ','
        + filepath   + ','
        + resultpath + fileitem.filename

        )
    f.close()
    shutil.copy(recipefile,savepath )




#    wait for source file to be consumed
#    while os.path.isfile(filepath):
#        time.sleep(.25)
#        print("+")
#    print "<br><br>"


    #now wait for the recipe to be consumed
    done=0
    while not os.path.isfile(resultpath+fileitem.filename):
        time.sleep(.25)
        print(".")
        done +=1
        if done > 100 : break
    print "<br>"

    if operation== 'classify':
        print ">The classification <br>"
        print "<img src=/results/"+fileitem.filename+">"


    if operation== 'stylize':
        print ">The stylized image<br>"
        print "<img src=/results/"+fileitem.filename+">"





else:
    print "No File Name"

print "<br>"
print "<br>"
cgi.test()
print "</BODY></HTML>"
