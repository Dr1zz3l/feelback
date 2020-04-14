# feelBack
Pythonista haptic engine and vibration feedback

# Haptic and vibration feedback for the Pythonista iOS app
allows feelable feedback over the haptic engine and vibration.

The iPhone 6s is the first iOS device to come with a haptic engine, which is only supported over a little workaround. This is used automatically. More info below.

## Installation
Copy from [GitHub](https://github.com/Dr1zz3l/feelback)

## Usage

    import feelback
    
    feelback.selectionChanged()
    feelback.impactOccured(workaround = True)
    for id in range (0, 3): feelback.notificationOccured(id)
    feelback.vibrate()
It is actually possible to play predefined [AudioServices](https://iphonedevwiki.net/index.php/AudioServices) by calling `AudioServicesPlaySystemSound(id)`.

### Haptic engine
Apart of simple vibrations, there basically are three different types of haptic feedback. Their intended uses are defined in the Apple developer docs as these:
- `selectionChanged` 
- `impactOccured` - e.g. for games
- `notificationOccured`
Since the iPhone 6s only supports this over a little workaround, the boolean `workaround` is used to change between using the "proper" method and the workaround.
If, for any reason, you need to use the workaround instead of the "proper" method, just pass `workaround = True`.

#### selectionChanged

    selectionChanged(workaround = workaround)
Pretty self-explanatory

#### impactOccured
    selectionChanged(workaround = workaround)
Same as `selectionChanged`

#### notificationOccured
    notificationOccured(id = False, workaround = workaround)
If the "proper" method is used, there are three different types (0, 1 and 2) to choose from. if no id is passed, the workaround is used automatically.

## vibrate
    vibrate()
As far as I know, there is no way to contol the strength or duration of the vibration. The latter can only be achieved by calling the `vibrate` multiple times with a slight delay, so they still overlap.


