import cv2, time
video=cv2.VideoCapture("C:\\Users\Yashashvi\Downloads\WhatsApp Video 2022-11-23 at 10.47.39 AM.mp4")
a=0
while True:
 a=a+1
 check, frame = video.read()
 print(frame)
 cv2.imshow("capturing", frame)
 key=cv2.waitKey(1)
 
 if key == ord('q'):
  break
video.release()
cv2.destroyAllWindows()