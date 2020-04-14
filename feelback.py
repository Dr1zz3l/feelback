import platform
import ctypes #needed for workaround
import objc_util #used if workaround is unnecessary
workaround = True if platform.machine() == 'iPhone8,1' else False #iphone 6s is the first device with haptic engine and supports haptic feedback differently than newer models

#for workaround and vibration:
AudioServicesPlaySystemSound = ctypes.CDLL(None).AudioServicesPlaySystemSound
impactID, selectionID, notificationID, vibrateID = 1519, 1520, 1521, 4095

#if workaround is unnecessary:
objc_util.NSBundle.bundle(Path="/System/Library/Frameworks/UIKit.framework").load()
UIImpactFeedbackGenerator = objc_util.ObjCClass('UIImpactFeedbackGenerator').new()
UISelectionFeedbackGenerator = objc_util.ObjCClass('UISelectionFeedbackGenerator').new()
UINotificationFeedbackGenerator = objc_util.ObjCClass('UINotificationFeedbackGenerator').new()
	

def selectionChanged(workaround = workaround):
	if workaround:
		AudioServicesPlaySystemSound(selectionID)
	else: 
		#UISelectionFeedbackGenerator.prepare()
		UISelectionFeedbackGenerator.selectionChanged()
		
def impactOccured(workaround = workaround):
	if workaround:
		AudioServicesPlaySystemSound(impactID)
	else:
		#UIImpactFeedbackGenerator.prepare()
		UIImpactFeedbackGenerator.impactOccurred()
		
def notificationOccured(id = False, workaround = workaround): #3 different ids if workaround is not used
	if workaround or not id:
		AudioServicesPlaySystemSound(notificationID)
	else: 
		#UINotificationFeedbackGenerator.prepare()
		UINotificationFeedbackGenerator.notificationOccurred_(id)

def vibrate():
	AudioServicesPlaySystemSound(vibrateID)
	
if __name__ == '__main__':
	import time
	dt = 1
	selectionChanged()
	time.sleep(dt)
	impactOccured()
	time.sleep(dt)
	for id in range(0, 3):
		notificationOccured(id)
		time.sleep(dt)
	vibrate()
	
	
	
