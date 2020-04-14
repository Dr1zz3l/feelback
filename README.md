# feelBack
Pythonista haptic engine and vibration feedback

### features
allows feelable feedback over the haptic engine and vibrator in iOS and iPadOS devices

## usage
iPhone 6s is the first iOS device to come with a haptic engine, which is only supported over a little workaround, which is used automatically. More info below.

Apart of simple vibrations, there basically are three different types of haptic feedback. Their intended uses are defined in the Apple developer docs as these:
- selectionChanged
- impactOccured
- notificationOccured

for any of the haptic feedbacks, just pass workaround 

### selectionChanged

    selectionChanged(workaround = workaround)
S
