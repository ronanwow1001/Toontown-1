from panda3d.core import ConfigVariableString

myGameServer = ConfigVariableString('my-game-server', '127.0.0.1')
print('Server specified in config file: ', mygameserver.getValue()

if (sys.argv[1] == '--server'):
	myGameServer.setValue(sys.argv[2])
print('Server that we will use: ', mygameserver.getValue()

print(ConfigVariableString("my-game-server"))

print(cpMgr)

from panda3d.core import loadPrcFile

loadPrcFile('Config.prc')

from panda3d.core import loadPrcFileData

loadPrcFileData('', 'fullscreen 1')