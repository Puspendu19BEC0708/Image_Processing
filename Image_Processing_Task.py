#!/usr/bin/env python
# coding: utf-8

# # Image_Processing
# <u><h3>Import the PIL libary</h3></u>
# <ul>
#   <li>To resize the image</li>
#   <p>To resize the image use Image.resize() before that store the image in the variable name image after resizing the image store the image in the new variable and 
#   name it as  new_image </p>
#     
#   <li>To rotate the image</li>
#   <p>Perform the rotation operation on the new_image and store it in the new variable  rotated_image1</p>
#   
# </ul>
# <p>To repeat the above process for 5 different images put the above process in the for loop</p>
# <p>To fit all the thereat object into the Baggage  boundary  i apply an if condition and rotate and resize the image accoringly</p>

# In[1]:


from PIL import Image 
for i in range(1,6):
    if i==5 or i==3:
        image = Image.open('T'+str(i)+'.jpg')
        new_image = image.resize((600, 600))
        rotated_image1 =  new_image.rotate(360)
        rotated_image1.save('Z'+str(i)+'.jpg')
        continue;
    if i==4:
        image = Image.open('T'+str(i)+'.jpg')
        new_image = image.resize((600, 700))
        rotated_image1 =  new_image.rotate(190)
        rotated_image1.save('Z'+str(i)+'.jpg')
        continue;
    image = Image.open('T'+str(i)+'.jpg')
    new_image = image.resize((400, 700))
    rotated_image1 =  new_image.rotate(180)
    rotated_image1.save('Z'+str(i)+'.jpg')


# <u><h3>Import pixellib</h3></u>
#   <ul>
#   <li>To segmented the image from the frame and place the segmented image in the  background according to our need </li>
#    <p>From the pixellib import the class alter_bg()
#      create the instances of alter_bg() class to load the deeplabv3+ trained model to  segment the image of the required object and remove the back ground
#      to load the model use the function load_pascalvoc_model() this function will take the deeplabv3+ trained model in h5 file format
#      Now change the back ground of the image accordingly by using change_bg_img() This will take the following parameter</p>
#     <ul>
#     <li>Foreground image whose background need to be change</li>
#     <li>Back ground image use to set the back ground of the foreground image</li>
#     <li>The new image with the change back ground</li>
#     </ul>
#   </ul>
#  <p>Put the above proces in for loop to apply it for n different images 
#     
#  

# In[3]:


import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg()
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
for i in range(1,6):
    change_bg.change_bg_img(f_image_path = "Z"+str(i)+".jpg",b_image_path = "B"+str(i)+".jpg", output_image_name="V"+str(i)+".jpg")
    


# In[8]:



    


# In[9]:


get_ipython().run_line_magic('pylab', 'inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
for i in range(1,6):
    img = mpimg.imread('V'+str(i)+'.jpg')
    imgplot = plt.imshow(img)
    plt.show()


# In[ ]:




