import urllib.request
import random
def PictureName():
    x =  str(random.randint(1,1001)) + '.png'
    print (x)
    return x

  
urllib.request.urlretrieve('http://shecodesconnect.com/shecodes_python_blog/img/posts/urlretrieve/img0.png', filename=PictureName(), reporthook=None, data=None)
 





