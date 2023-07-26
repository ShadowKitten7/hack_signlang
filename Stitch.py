import cv2
import pickle
class Displayer:
  def __init__(self,windowName='Sign') -> None:
    self.delay_bw_signs=1000//30
    self.frameRate=60
    with open('known_words.dat','rb') as file:
      self.knownWords=pickle.load(file)
    self.name=windowName
    self.rescale=2
    self.createWindow()
  def known(self, word):
    
    low = 0
    high = len(self.knownWords) - 1
    mid = 0
    while low <= high:
        mid = (high + low) //2
        if self.knownWords[mid] < word:
            low = mid + 1
        elif self.knownWords[mid] > word:
            high = mid - 1
        else:
            return True
    return False
  def createWindow(self):
    cap=cv2.VideoCapture('Dataset/0.mp4')
    h,w=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cv2.namedWindow(self.name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(self.name,w//self.rescale,h//self.rescale)
    cap.release()
  def displayWord(self,path):
    cap=cv2.VideoCapture(path)
    if (cap.isOpened()== False):
      print("Does not exist",path[8:-4])
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            if cv2.getWindowProperty(self.name,cv2.WND_PROP_VISIBLE)<1:
              self.createWindow()
            cv2.imshow(self.name, frame)
            if cv2.waitKey(1000//self.frameRate) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()  
  def show(self,l):
    for i in l:
      if self.known(i.capitalize()):
        self.displayWord('Dataset/'+i.capitalize()+'.mp4')
      else:  
        for char in i:
          self.displayWord('Dataset/'+char.capitalize()+'.mp4')
  def destroy(self):
    cv2.destroyWindow(self.name)
  def destroyDelayed(self):
    try:
      
      cv2.waitKey(1000)
      self.destroy()
    except:
      pass
def read():
  sent=input()
  a=Displayer()
  a.show(sent.split())
  a.destroyDelayed()
read()