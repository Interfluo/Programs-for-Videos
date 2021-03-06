# This code creates an animation from a collection of images
import cv2

video_name = 'video_nozz_final_1.avi'
video = cv2.VideoWriter(video_name, 0, 100, (1362, 794))  # the 100 controls how fast the video runs (low => slow)
for i in range(2499):
   # Updating name for each frame - depends on the naming scheme you chose for saving
   if i<10:
       k = '000'+str(i)
   elif i<100:
       k = '00' + str(i)
   elif i < 1000:
       k = '0' + str(i)
   else:
       k = str(i)
   filename = ['video_anim/img.', k, '.png']
   img = cv2.imread("".join(filename))
   video.write(img)         # writing to file
   print(k)

cv2.destroyAllWindows()
video.release()