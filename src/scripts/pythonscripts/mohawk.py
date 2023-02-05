import arcemu
from arcemu import GossipMenu
from arcemu import Player
from arcemu import Unit

def mohawk_onHello( unit, event, player ):
	print( player.getName() + " said gossip hello to " + unit.getName() )
	print( "Event id: " + str( event ) )
	
	menu = GossipMenu( 1, unit, arcemu.GOSSIP_AUTOSEND_FALSE )
	menu.addItem( arcemu.ICON_CHAT, "Give me a vehicle!", 1, 0 )
	menu.addItem( arcemu.ICON_CHAT, "Dismiss my vehicle!", 2, 0 )
	menu.addItem( arcemu.ICON_CHAT, "Am I on a vehicle?", 3, 0 )
	menu.addItem( arcemu.ICON_CHAT, "Add a passenger to my vehicle!", 4, 0 )
	menu.sendToPlayer( player )
	
def mohawk_onSelectOption( unit, player, id, enteredCode ):
	GossipMenu.complete( player )
	
	pu = player.toUnit()
	
	if id == 1:
		if pu.isOnVehicle():
			unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "You are already on a vehicle. Fool!" )
		else:
			unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "Here it is, Fool!" )
			player.spawnAndEnterVehicle( 28605, 1000 )
			
	elif id == 2:
		if pu.isOnVehicle():
			unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "Go away, Fool!" )
			pu.dismissVehicle()
		else:
			unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "You don't have a vehicle, Fool!" )
			
	elif id == 3:
		if pu.isOnVehicle():
			unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "Ofc you are on a vehicle, Fool!" )
		else:
			unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "Ofc you are not on a vehicle, Fool!" )
			
	elif id == 4:
		if pu.isOnVehicle():
			if pu.hasEmptyVehicleSeat():
				unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "Here you go, Fool!" )
				pu.addVehiclePassenger( 31111 )
			else:
				unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "You don't event have a free seat, Fool!" )
		else:
			unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "You don't even have a vehicle, Fool!" )


def mohawk_onEnterVehicle( unit ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "Nice I am on a vehicle now!" )
	
def mohawk_onExitVehicle( unit ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "Aw I got booted :(" )

arcemu.RegisterUnitGossipEvent( 31111, arcemu.GOSSIP_EVENT_HELLO, mohawk_onHello )
arcemu.RegisterUnitGossipEvent( 31111, arcemu.GOSSIP_EVENT_SELECT, mohawk_onSelectOption )
arcemu.RegisterUnitEvent( 31111, arcemu.CREATURE_EVENT_ON_ENTER_VEHICLE, mohawk_onEnterVehicle )
arcemu.RegisterUnitEvent( 31111, arcemu.CREATURE_EVENT_ON_EXIT_VEHICLE, mohawk_onExitVehicle )
		