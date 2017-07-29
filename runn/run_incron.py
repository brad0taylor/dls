#!/home/brad/anaconda3/envs/knn/bin/python
# coding: utf-8


import glob
import os
import fileinput


print ( os.getcwd())

imgpath = '/usr/lib/cgi-bin/uploads/'
respath = '/usr/lib/cgi-bin/results/'
recipepath  = '/usr/lib/cgi-bin/recipes/'
stylepath   = '/home/brad/apps/dls/PyTorch-Style-Transfer/styles/user/test/'
done = 0

f=open(recipepath+'recipe.txt','r')
recipe_str=f.read()
f.close()


#recipe file contains list of operations
#1 operation per line
#print( 'recipe found =', recipe_str)
recipe_lines=recipe_str.split('\n')
print(recipe_lines)

for line in recipe_lines:
    print('\nrecipe:')
    recipes=line.split(',')
    recipe=recipes[0];
    print(' 0 ', recipes[0])
    print(' 1 ', recipes[1])
    print(' 2 ', recipes[2])
    print(' 3 ', recipes[3])



    style_image = 'candy'

    if recipe=='stylize' :
        style_image =recipes[1]
        print( 'style found =', style_image)

    if recipe=='style' :
        mode        =recipes[1]
        print( 'mode found =', mode)

#for fullname in glob.glob(os.path.join(imgpath, '*.jpg')):

#    filename=os.path.basename(fullname)
    imgfullname= recipes[2]
    resfullname= recipes[3]
    recfullname= recipepath + 'recipe.txt'

#    styleimgname= stylepath + 'img/' + filename
#    print('style img=styleimg', styleimgname)

    cmd='cmd fail'

    #classify images
    if(recipe=='classify'):
        cmd = "~/apps/dls/classify.py"    + " --image "  + imgfullname  + " --result " + resfullname


    #train style transfer
    if(recipe=='style') and mode=='upload' :
        os.rename( imgfullname , styleimgname )

    if(recipe=='style') and mode=='clear' :
        #delete files in style dir
        files=glob.glob(stylepath + '*')
        for f in files:
            os.remove(f)


    if(recipe=='style') and mode=='train' :
        #delete files in style dir
        cmd = '/home/brad/apps/dls/PyTorch-Style-Transfer/experiments/main.py eval' \
            + ' --style_folder '  + styleimgpath + 'img/' \
            + ' --vgg-model-dir ' + styleimgpath + 'vgg/'  \
            + ' --save-model-dir' + styleimgpath + 'model/' \




    #render style transfer
    if(recipe=='stylize'):
        cmd = '/home/brad/apps/dls/PyTorch-Style-Transfer/experiments/main.py eval' \
            + ' --content-image ' + imgfullname \
            + ' --output ' + resfullname \
            + ' --style-image /home/brad/apps/dls/PyTorch-Style-Transfer/experiments/images/9styles/' + style_image+ '.jpg'\
            + ' --model /home/brad/apps/dls/PyTorch-Style-Transfer/experiments/models/9styles.model' \
            + ' --content-size 1024'

    print('\n\ncmd:\n', cmd ,'\n\n')
    os.system(cmd)
#    get_ipython().magic('run $cmd')

    #remove files from uploads
    #os.remove  (imgfullname)
    #print( 'removed', imgfullname)

    #limit to 4 files
    done +=1
    if done > 4 : break

os.remove  (recfullname)
print( 'removed', recfullname)
