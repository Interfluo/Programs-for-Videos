"""This Code takes an input .mkv file into a .avi file"""
import cv2

input = 'MOC_raw.mkv'                                 # input filename
output = 'MOC.avi'                                             # output filename
cap = cv2.VideoCapture(input)                                    # read the input file
fourcc = cv2.VideoWriter_fourcc(*'XVID')                         # Define the codec
out = cv2.VideoWriter(output, fourcc, 60.0, (1920, 1080))        # create VideoWriter object
while cap.isOpened():
    ret, frame = cap.read()                                      # open input frame by frame
    if ret is True:
        out.write(frame)                                         # save to output frame by frame
    else:
        break
print("Done")
cap.release()
out.release()
cv2.destroyAllWindows()
