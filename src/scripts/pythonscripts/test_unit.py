import arcemu
from arcemu import Unit

def npc_onCombatStart( unit, event, target ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, "I am going to kill you " + target.getName() + "!" )
	
def npc_onCombatStop( unit, event, target ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "Okay, Okay, I yield." )

def npc_onDamageTaken( unit, event, attacker, amount ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "I am damaged for " + str( amount ) )
	
def npc_onCastSpell( unit, event, spellId ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "I am casting spell " + str( spellId ) )
	
def npc_onTargetParried( unit, event, target ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "I have parried the attack of " + target.getName() )
	
def npc_onTargetDodged( unit, event, target ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "I have dodged the attack of " + target.getName() )
	
def npc_onTargetBlocked( unit, event, target, amount ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "I have blocked " + str( amount ) + " of the attack of " + target.getName() )
	
def npc_onTargetCritHit( unit, event, target, amount ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, target.getName() + " has criticall hit me for " + str( amount ) )	
	
def npc_onParried( unit, event, target ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, target.getName() + " has parried my attack" )
	
def npc_onDodged( unit, event, target ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, target.getName() + " has dodged my attack" )
	
def npc_onBlocked( unit, event, target, amount ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, target.getName() + " has blocked " + str( amount ) + " of my attack" )
	
def npc_onCritHit( unit, event, target, amount ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, target.getName() + " has been critically hit for " + str( amount ) )	
	
def npc_onHit( unit, event, target, amount ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "I have hit " + target.getName() + " for " + str( amount ) )
	
def npc_onDied( unit, event, killer ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, killer.getName() + " has killed me." )
	
def npc_onTargetDied( unit, event, target ):
	unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "Hahahaha. " + target.getName() + " you are not prepared!" )
	
def npc_onLoad( unit, event ):
	print( "Loaded creature " + unit.getName() )
	

arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_ENTER_COMBAT, npc_onCombatStart )
arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_LEAVE_COMBAT, npc_onCombatStop )
arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_HIT, npc_onHit )
arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_DAMAGE_TAKEN, npc_onDamageTaken )
arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_CAST_SPELL, npc_onCastSpell )

arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_TARGET_PARRIED, npc_onTargetParried )
arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_TARGET_DODGED, npc_onTargetDodged )
arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_TARGET_BLOCKED, npc_onTargetBlocked )
arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_TARGET_CRIT_HIT, npc_onTargetCritHit )

arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_PARRY, npc_onParried )
arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_DODGED, npc_onDodged )
arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_BLOCKED, npc_onBlocked )
arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_CRIT_HIT, npc_onCritHit )

arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_DIED, npc_onDied )
arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_TARGET_DIED, npc_onTargetDied )
arcemu.RegisterUnitEvent( 113, arcemu.CREATURE_EVENT_ON_LOAD, npc_onLoad )
