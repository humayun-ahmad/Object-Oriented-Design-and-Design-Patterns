from remote_control import RemoteControl
from tv import TV
from projector import Projector

tv = TV()
tv_remote = RemoteControl(tv)

print("=== Testing TV ===")
tv_remote.power_on()
tv_remote.volume_up()
tv_remote.volume_down()
tv_remote.power_off()

projector = Projector()
projector_remote = RemoteControl(projector)

print("\n=== Testing Projector ===")
projector_remote.power_on()
projector_remote.volume_up()
projector_remote.volume_down()
projector_remote.power_off()
