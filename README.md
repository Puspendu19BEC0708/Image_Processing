# Image_Processing
<u><h3>Import the PIL libary</h3></u>
<ul>
  <li>To resize the image</li>
  <p>To resize the image use Image.resize() before that store the image in the variable name image after resizing the image store the image in the new variable and 
  name it as  new_image </p>
    
  <li>To rotate the image</li>
  <p>Perform the rotation operation on the new_image and store it in the new variable  rotated_image1</p>
  
</ul>
<p>To repeat the above process for 5 different images put the above process in the for loop</p>
<p>To fit all the thereat object into the Baggage  boundary  i apply an if condition and rotate and resize the image accoringly</p>

<u><h3>Import pixellib</h3><u>
  <ul>
  <li>To segmented the image from the frame and place the segmented image in the  background according to our need </li>
   <p>From the pixellib import the class alter_bg()</p>
   <p>create the instances of alter_bg() class to load the deeplabv3+ trained model to  segment the image of the required object and remove the back ground</p>
   <p>to load the model use the function load_pascalvoc_model() this function will take the deeplabv3+ trained model in h5 file format</p>
   <p>Now change the back ground of the image accordingly by using change_bg_img() This will take the following parameter</p>
    <li>Foreground image whose background need to be change</li>
    <li>Back ground image use to set the back ground of the foreground image</li>
    <li>The new image with the change back ground</li>
  </ul>
 <p>Put the above proces in for loop to apply it for n different images 
    

  


