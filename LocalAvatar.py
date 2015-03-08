from direct.directbase import DirectStart
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
import linecache

base.disableMouse()
 
legsAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-hand-start.bam', 'firehose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_firehose.bam', 'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateL-putt.bam', 'slip-forward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-forward.bam', 'catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eatnrun.bam', 'tickle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_tickle.bam', 'water-gun': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_water-gun.bam', 'leverNeutral': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverNeutral.bam', 'swim': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swim.bam', 'catch-run': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gamerun.bam', 'sad-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_sad-neutral.bam', 'pet-loop': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petloop.bam', 'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zstart.bam', 'wave': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_wave.bam', 'reel-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reelneutral.bam', 'pole-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_poleneutral.bam', 'bank': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_jellybeanJar.bam', 'scientistGame': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistGame.bam', 'right-hand': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-hand.bam', 'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_lookloop-putt.bam', 'victory': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_victory-dance.bam', 'lose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_lose.bam', 'cringe': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_cringe.bam', 'right': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_right.bam', 'headdown-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_headdown-putt.bam', 'conked': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_conked.bam', 'jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump.bam', 'into-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_into-putt.bam', 'fish-end': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishEND.bam', 'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zend.bam', 'shrug': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_shrug.bam', 'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_sprinkle-dust.bam', 'hold-bottle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hold-bottle.bam', 'takePhone': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_takePhone.bam', 'melt': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_melt.bam', 'pet-start': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petin.bam', 'look-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_look-putt.bam', 'loop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_loop-putt.bam', 'good-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_good-putt.bam', 'juggle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_juggle.bam', 'run': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_run.bam', 'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_press-button.bam', 'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-back-right.bam', 'water': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_water.bam', 'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-point-start.bam', 'bad-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_bad-putt.bam', 'struggle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_struggle.bam', 'running-jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_running-jump.bam', 'callPet': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_callPet.bam', 'throw': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_pie-throw.bam', 'catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eat_neutral.bam', 'tug-o-war': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_tug-o-war.bam', 'bow': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bow.bam', 'swing': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swing.bam', 'climb': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_climb.bam', 'scientistWork': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistWork.bam', 'think': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_think.bam', 'catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameThrow.bam', 'walk': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_walk.bam', 'down': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_down.bam', 'pole': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_pole.bam', 'periscope': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_periscope.bam', 'duck': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_duck.bam', 'curtsy': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_curtsy.bam', 'jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zend.bam', 'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_loop_dig.bam', 'angry': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_angry.bam', 'bored': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bored.bam', 'swing-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_swing-putt.bam', 'pet-end': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petend.bam', 'spit': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_spit.bam', 'right-point': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-point.bam', 'start-dig': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_into_dig.bam', 'castlong': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_castlong.bam', 'confused': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_confused.bam', 'neutral': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_neutral.bam', 'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zhang.bam', 'reel': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reel.bam', 'slip-backward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-backward.bam', 'sound': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_shout.bam', 'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_sidestep-left.bam', 'up': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_up.bam', 'fish-again': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishAGAIN.bam', 'cast': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_cast.bam', 'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_phoneBack.bam', 'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_phoneNeutral.bam', 'scientistJealous': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistJealous.bam', 'battlecast': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fish.bam', 'sit-start': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_intoSit.bam', 'toss': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_toss.bam', 'happy-dance': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_happy-dance.bam', 'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zstart.bam', 'teleport': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_teleport.bam', 'sit': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_sit.bam', 'sad-walk': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_losewalk.bam', 'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_give-props-start.bam', 'book': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_book.bam', 'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zhang.bam', 'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistEmcee.bam', 'leverPull': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverPull.bam', 'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_tutorial-neutral.bam', 'badloop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_badloop-putt.bam', 'give-props': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_give-props.bam', 'hold-magnet': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hold-magnet.bam', 'hypnotize': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hypnotize.bam', 'left-point': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_left-point.bam', 'leverReach': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverReach.bam', 'feedPet': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_feedPet.bam', 'reel-H': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reelH.bam', 'applause': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_applause.bam', 'smooch': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_smooch.bam', 'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateR-putt.bam', 'fish-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishneutral.bam', 'push': 'phase_9/models/char/tt_a_chr_dgs_shorts_legs_push.bam', 'catch-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameneutral.bam', 'left': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_left.bam'}
 
torsoAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-hand-start.bam', 'firehose': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_firehose.bam', 'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_rotateL-putt.bam', 'slip-forward': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_slip-forward.bam', 'catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_eatnrun.bam', 'tickle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_tickle.bam', 'water-gun': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_water-gun.bam', 'leverNeutral': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverNeutral.bam', 'swim': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_swim.bam', 'catch-run': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gamerun.bam', 'sad-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_sad-neutral.bam', 'pet-loop': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petloop.bam', 'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zstart.bam', 'wave': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_wave.bam', 'reel-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reelneutral.bam', 'pole-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_poleneutral.bam', 'bank': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_jellybeanJar.bam', 'scientistGame': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistGame.bam', 'right-hand': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-hand.bam', 'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_lookloop-putt.bam', 'victory': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_victory-dance.bam', 'lose': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_lose.bam', 'cringe': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_cringe.bam', 'right': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_right.bam', 'headdown-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_headdown-putt.bam', 'conked': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_conked.bam', 'jump': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump.bam', 'into-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_into-putt.bam', 'fish-end': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishEND.bam', 'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zend.bam', 'shrug': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_shrug.bam', 'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_sprinkle-dust.bam', 'hold-bottle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hold-bottle.bam', 'takePhone': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_takePhone.bam', 'melt': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_melt.bam', 'pet-start': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petin.bam', 'look-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_look-putt.bam', 'loop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_loop-putt.bam', 'good-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_good-putt.bam', 'juggle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_juggle.bam', 'run': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_run.bam', 'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_press-button.bam', 'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-back-right.bam', 'water': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_water.bam', 'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-point-start.bam', 'bad-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_bad-putt.bam', 'struggle': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_struggle.bam', 'running-jump': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_running-jump.bam', 'callPet': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_callPet.bam', 'throw': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_pie-throw.bam', 'catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_eat_neutral.bam', 'tug-o-war': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_tug-o-war.bam', 'bow': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_bow.bam', 'swing': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_swing.bam', 'climb': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_climb.bam', 'scientistWork': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistWork.bam', 'think': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_think.bam', 'catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gameThrow.bam', 'walk': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_walk.bam', 'down': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_down.bam', 'pole': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_pole.bam', 'periscope': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_periscope.bam', 'duck': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_duck.bam', 'curtsy': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_curtsy.bam', 'jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zend.bam', 'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_loop_dig.bam', 'angry': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_angry.bam', 'bored': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_bored.bam', 'swing-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_swing-putt.bam', 'pet-end': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_petend.bam', 'spit': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_spit.bam', 'right-point': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_right-point.bam', 'start-dig': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_into_dig.bam', 'castlong': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_castlong.bam', 'confused': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_confused.bam', 'neutral': 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_neutral.bam', 'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_jump-zhang.bam', 'reel': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reel.bam', 'slip-backward': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_slip-backward.bam', 'sound': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_shout.bam', 'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_sidestep-left.bam', 'up': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_up.bam', 'fish-again': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishAGAIN.bam', 'cast': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_cast.bam', 'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_phoneBack.bam', 'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_phoneNeutral.bam', 'scientistJealous': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistJealous.bam', 'battlecast': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fish.bam', 'sit-start': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_intoSit.bam', 'toss': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_toss.bam', 'happy-dance': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_happy-dance.bam', 'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zstart.bam', 'teleport': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_teleport.bam', 'sit': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_sit.bam', 'sad-walk': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_losewalk.bam', 'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_give-props-start.bam', 'book': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_book.bam', 'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_leap_zhang.bam', 'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_scientistEmcee.bam', 'leverPull': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverPull.bam', 'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_tutorial-neutral.bam', 'badloop-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_badloop-putt.bam', 'give-props': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_give-props.bam', 'hold-magnet': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hold-magnet.bam', 'hypnotize': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_hypnotize.bam', 'left-point': 'phase_3.5/models/char/tt_a_chr_dgl_shorts_torso_left-point.bam', 'leverReach': 'phase_10/models/char/tt_a_chr_dgl_shorts_torso_leverReach.bam', 'feedPet': 'phase_5.5/models/char/tt_a_chr_dgl_shorts_torso_feedPet.bam', 'reel-H': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_reelH.bam', 'applause': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_applause.bam', 'smooch': 'phase_5/models/char/tt_a_chr_dgl_shorts_torso_smooch.bam', 'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgl_shorts_torso_rotateR-putt.bam', 'fish-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_fishneutral.bam', 'push': 'phase_9/models/char/tt_a_chr_dgl_shorts_torso_push.bam', 'catch-neutral': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_gameneutral.bam', 'left': 'phase_4/models/char/tt_a_chr_dgl_shorts_torso_left.bam'}

toontype = linecache.getline('DataFolder/Data.txt', 4)
if toontype == 'duck\n':
	duckHead = loader.loadModel('phase_3/models/char/duck-heads-1000.bam')
	otherParts = duckHead.findAllMatches('**/*long*')
	for partNum in range(0, otherParts.getNumPaths()):
		otherParts.getPath(partNum).removeNode()
	ntrlMuzzle = duckHead.find('**/*muzzle*neutral')
	otherParts = duckHead.findAllMatches('**/*muzzle*')
	for partNum in range(0, otherParts.getNumPaths()):
		part = otherParts.getPath(partNum)
		if part != ntrlMuzzle:
			otherParts.getPath(partNum).removeNode()
if toontype == 'cat\n':
	duckHead = loader.loadModel('phase_3/models/char/cat-heads-1000.bam')
	otherParts = duckHead.findAllMatches('**/*long*')
	for partNum in range(0, otherParts.getNumPaths()):
		otherParts.getPath(partNum).removeNode()
	ntrlMuzzle = duckHead.find('**/*muzzle*neutral')
	otherParts = duckHead.findAllMatches('**/*muzzle*')
	for partNum in range(0, otherParts.getNumPaths()):
		part = otherParts.getPath(partNum)
		if part != ntrlMuzzle:
			otherParts.getPath(partNum).removeNode()
if toontype == 'mouse\n':
	duckHead = loader.loadModel('phase_3/models/char/mouse-heads-1000.bam')
	otherParts = duckHead.findAllMatches('**/*long*')
	for partNum in range(0, otherParts.getNumPaths()):
		otherParts.getPath(partNum).removeNode()
	ntrlMuzzle = duckHead.find('**/*muzzle*neutral')
	otherParts = duckHead.findAllMatches('**/*muzzle*')
	for partNum in range(0, otherParts.getNumPaths()):
		part = otherParts.getPath(partNum)
		if part != ntrlMuzzle:
			otherParts.getPath(partNum).removeNode()
if toontype == 'horse\n':
	duckHead = loader.loadModel('phase_3/models/char/horse-heads-1000.bam')
	otherParts = duckHead.findAllMatches('**/*long*')
	for partNum in range(0, otherParts.getNumPaths()):
		otherParts.getPath(partNum).removeNode()
	ntrlMuzzle = duckHead.find('**/*muzzle*neutral')
	otherParts = duckHead.findAllMatches('**/*muzzle*')
	for partNum in range(0, otherParts.getNumPaths()):
		part = otherParts.getPath(partNum)
		if part != ntrlMuzzle:
			otherParts.getPath(partNum).removeNode()
if toontype == 'pig\n':
	duckHead = loader.loadModel('phase_3/models/char/pig-heads-1000.bam')
	otherParts = duckHead.findAllMatches('**/*long*')
	for partNum in range(0, otherParts.getNumPaths()):
		otherParts.getPath(partNum).removeNode()
	ntrlMuzzle = duckHead.find('**/*muzzle*neutral')
	otherParts = duckHead.findAllMatches('**/*muzzle*')
	for partNum in range(0, otherParts.getNumPaths()):
		part = otherParts.getPath(partNum)
		if part != ntrlMuzzle:
			otherParts.getPath(partNum).removeNode()
if toontype == 'rabbit\n':
	duckHead = loader.loadModel('phase_3/models/char/rabbit-heads-1000.bam')
	otherParts = duckHead.findAllMatches('**/*long*')
	for partNum in range(0, otherParts.getNumPaths()):
		otherParts.getPath(partNum).removeNode()
	ntrlMuzzle = duckHead.find('**/*muzzle*neutral')
	otherParts = duckHead.findAllMatches('**/*muzzle*')
	for partNum in range(0, otherParts.getNumPaths()):
		part = otherParts.getPath(partNum)
		if part != ntrlMuzzle:
			otherParts.getPath(partNum).removeNode()
if toontype == 'monkey\n':
	duckHead = loader.loadModel('phase_3/models/char/monkey-heads-1000.bam')
	otherParts = duckHead.findAllMatches('**/*long*')
	for partNum in range(0, otherParts.getNumPaths()):
		otherParts.getPath(partNum).removeNode()
	ntrlMuzzle = duckHead.find('**/*muzzle*neutral')
	otherParts = duckHead.findAllMatches('**/*muzzle*')
	for partNum in range(0, otherParts.getNumPaths()):
		part = otherParts.getPath(partNum)
		if part != ntrlMuzzle:
			otherParts.getPath(partNum).removeNode()
if toontype == 'bear\n':
	duckHead = loader.loadModel('phase_3/models/char/bear-heads-1000.bam')
	otherParts = duckHead.findAllMatches('**/*long*')
	for partNum in range(0, otherParts.getNumPaths()):
		otherParts.getPath(partNum).removeNode()
	ntrlMuzzle = duckHead.find('**/*muzzle*neutral')
	otherParts = duckHead.findAllMatches('**/*muzzle*')
	for partNum in range(0, otherParts.getNumPaths()):
		part = otherParts.getPath(partNum)
		if part != ntrlMuzzle:
			otherParts.getPath(partNum).removeNode()
if toontype == 'dog\n':
		duckHead = loader.loadModel('phase_3/models/char/tt_a_chr_dgm_skirt_head_1000.bam')

duckTorso = loader.loadModel('phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam')
duckLegs  = loader.loadModel('phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000.bam')
otherParts = duckLegs.findAllMatches('**/boots*')+duckLegs.findAllMatches('**/shoes')
for partNum in range(0, otherParts.getNumPaths()):
    otherParts.getPath(partNum).removeNode()
 
duckBody = Actor({'head':duckHead, 'torso':duckTorso, 'legs':duckLegs},
                {'torso':torsoAnimDict, 'legs':legsAnimDict})
duckBody.attach('head', 'torso', 'def_head')
duckBody.attach('torso', 'legs', 'joint_hips')
 
gloves = duckBody.findAllMatches('**/hands')
ears = duckBody.findAllMatches('**/*ears*')
head = duckBody.findAllMatches('**/head*') 
sleeves = duckBody.findAllMatches('**/sleeves')
shirt = duckBody.findAllMatches('**/torso-top')
shorts = duckBody.findAllMatches('**/torso-bot')
neck = duckBody.findAllMatches('**/neck')
arms = duckBody.findAllMatches('**/arms')
legs = duckBody.findAllMatches('**/legs')
feet = duckBody.findAllMatches('**/feet')
 
bodyNodes = []
bodyNodes += [gloves]
bodyNodes += [head, ears]
bodyNodes += [sleeves, shirt, shorts]
bodyNodes += [neck, arms, legs, feet]

if linecache.getline('DataFolder/Data.txt', 3) == 'red\n':
	bodyNodes[0].setColor(1, 1, 1, 1)
	bodyNodes[1].setColor(0.863281, 0.40625, 0.417969, 1.0)
	bodyNodes[2].setColor(0.863281, 0.40625, 0.417969, 1.0)
	bodyNodes[3].setColor(1, 1, 1, 1)
	bodyNodes[4].setColor(1, 1, 1, 1)
	bodyNodes[5].setColor(1, 1, 1, 1)
	bodyNodes[6].setColor(0.863281, 0.40625, 0.417969, 1.0)
	bodyNodes[7].setColor(0.863281, 0.40625, 0.417969, 1.0)
	bodyNodes[8].setColor(0.863281, 0.40625, 0.417969, 1.0)
	bodyNodes[9].setColor(0.863281, 0.40625, 0.417969, 1.0)
if linecache.getline('DataFolder/Data.txt', 3) == 'blue\n':
	bodyNodes[0].setColor(1, 1, 1, 1)
	bodyNodes[1].setColor(0.191406, 0.5625, 0.773438, 1.0)
	bodyNodes[2].setColor(0.191406, 0.5625, 0.773438, 1.0)
	bodyNodes[3].setColor(1, 1, 1, 1)
	bodyNodes[4].setColor(1, 1, 1, 1)
	bodyNodes[5].setColor(1, 1, 1, 1)
	bodyNodes[6].setColor(0.191406, 0.5625, 0.773438, 1.0)
	bodyNodes[7].setColor(0.191406, 0.5625, 0.773438, 1.0)
	bodyNodes[8].setColor(0.191406, 0.5625, 0.773438, 1.0)
	bodyNodes[9].setColor(0.191406, 0.5625, 0.773438, 1.0)
if linecache.getline('DataFolder/Data.txt', 3) == 'yellow\n':
	bodyNodes[0].setColor(1, 1, 1, 1)
	bodyNodes[1].setColor(0.996094, 0.898438, 0.320312, 1.0)
	bodyNodes[2].setColor(0.996094, 0.898438, 0.320312, 1.0)
	bodyNodes[3].setColor(1, 1, 1, 1)
	bodyNodes[4].setColor(1, 1, 1, 1)
	bodyNodes[5].setColor(1, 1, 1, 1)
	bodyNodes[6].setColor(0.996094, 0.898438, 0.320312, 1.0)
	bodyNodes[7].setColor(0.996094, 0.898438, 0.320312, 1.0)
	bodyNodes[8].setColor(0.996094, 0.898438, 0.320312, 1.0)
	bodyNodes[9].setColor(0.996094, 0.898438, 0.320312, 1.0)
if linecache.getline('DataFolder/Data.txt', 3) == 'white\n':
	bodyNodes[0].setColor(1, 1, 1, 1)
	bodyNodes[1].setColor(1, 1, 1, 1)
	bodyNodes[2].setColor(1, 1, 1, 1)
	bodyNodes[3].setColor(1, 1, 1, 1)
	bodyNodes[4].setColor(1, 1, 1, 1)
	bodyNodes[5].setColor(1, 1, 1, 1)
	bodyNodes[6].setColor(1, 1, 1, 1)
	bodyNodes[7].setColor(1, 1, 1, 1)
	bodyNodes[8].setColor(1, 1, 1, 1)
	bodyNodes[9].setColor(1, 1, 1, 1)
if linecache.getline('DataFolder/Data.txt', 3) == 'brown\n':
	bodyNodes[0].setColor(1, 1, 1, 1)
	bodyNodes[1].setColor(0.640625, 0.355469, 0.269531, 1.0)
	bodyNodes[2].setColor(0.640625, 0.355469, 0.269531, 1.0)
	bodyNodes[3].setColor(1, 1, 1, 1)
	bodyNodes[4].setColor(1, 1, 1, 1)
	bodyNodes[5].setColor(1, 1, 1, 1)
	bodyNodes[6].setColor(0.640625, 0.355469, 0.269531, 1.0)
	bodyNodes[7].setColor(0.640625, 0.355469, 0.269531, 1.0)
	bodyNodes[8].setColor(0.640625, 0.355469, 0.269531, 1.0)
	bodyNodes[9].setColor(0.640625, 0.355469, 0.269531, 1.0)
if linecache.getline('DataFolder/Data.txt', 3) == 'orange\n':
	bodyNodes[0].setColor(1, 1, 1, 1)
	bodyNodes[1].setColor(0.992188, 0.480469, 0.167969, 1.0)
	bodyNodes[2].setColor(0.992188, 0.480469, 0.167969, 1.0)
	bodyNodes[3].setColor(1, 1, 1, 1)
	bodyNodes[4].setColor(1, 1, 1, 1)
	bodyNodes[5].setColor(1, 1, 1, 1)
	bodyNodes[6].setColor(0.992188, 0.480469, 0.167969, 1.0)
	bodyNodes[7].setColor(0.992188, 0.480469, 0.167969, 1.0)
	bodyNodes[8].setColor(0.992188, 0.480469, 0.167969, 1.0)
	bodyNodes[9].setColor(0.992188, 0.480469, 0.167969, 1.0)
if linecache.getline('DataFolder/Data.txt', 3) == 'green\n':
	bodyNodes[0].setColor(1, 1, 1, 1)
	bodyNodes[1].setColor(0.304688, 0.96875, 0.402344, 1.0)
	bodyNodes[2].setColor(0.304688, 0.96875, 0.402344, 1.0)
	bodyNodes[3].setColor(1, 1, 1, 1)
	bodyNodes[4].setColor(1, 1, 1, 1)
	bodyNodes[5].setColor(1, 1, 1, 1)
	bodyNodes[6].setColor(0.304688, 0.96875, 0.402344, 1.0)
	bodyNodes[7].setColor(0.304688, 0.96875, 0.402344, 1.0)
	bodyNodes[8].setColor(0.304688, 0.96875, 0.402344, 1.0)
	bodyNodes[9].setColor(0.304688, 0.96875, 0.402344, 1.0)
if linecache.getline('DataFolder/Data.txt', 3) == 'black\n':
	bodyNodes[0].setColor(1, 1, 1, 1)
	bodyNodes[1].setColor(0.3, 0.3, 0.35, 1.0)
	bodyNodes[2].setColor(0.3, 0.3, 0.35, 1.0)
	bodyNodes[3].setColor(1, 1, 1, 1)
	bodyNodes[4].setColor(1, 1, 1, 1)
	bodyNodes[5].setColor(1, 1, 1, 1)
	bodyNodes[6].setColor(0.3, 0.3, 0.35, 1.0)
	bodyNodes[7].setColor(0.3, 0.3, 0.35, 1.0)
	bodyNodes[8].setColor(0.3, 0.3, 0.35, 1.0)
	bodyNodes[9].setColor(0.3, 0.3, 0.35, 1.0)
if linecache.getline('DataFolder/Data.txt', 3) == 'purple\n':
	bodyNodes[0].setColor(1, 1, 1, 1)
	bodyNodes[1].setColor(0.546875, 0.28125, 0.75, 1.0)
	bodyNodes[2].setColor(0.546875, 0.28125, 0.75, 1.0)
	bodyNodes[3].setColor(1, 1, 1, 1)
	bodyNodes[4].setColor(1, 1, 1, 1)
	bodyNodes[5].setColor(1, 1, 1, 1)
	bodyNodes[6].setColor(0.546875, 0.28125, 0.75, 1.0)
	bodyNodes[7].setColor(0.546875, 0.28125, 0.75, 1.0)
	bodyNodes[8].setColor(0.546875, 0.28125, 0.75, 1.0)
	bodyNodes[9].setColor(0.546875, 0.28125, 0.75, 1.0)
if linecache.getline('DataFolder/Data.txt', 3) == 'pink\n':
	bodyNodes[0].setColor(1, 1, 1, 1)
	bodyNodes[1].setColor(0.898438, 0.617188, 0.90625, 1.0)
	bodyNodes[2].setColor(0.898438, 0.617188, 0.90625, 1.0)
	bodyNodes[3].setColor(1, 1, 1, 1)
	bodyNodes[4].setColor(1, 1, 1, 1)
	bodyNodes[5].setColor(1, 1, 1, 1)
	bodyNodes[6].setColor(0.898438, 0.617188, 0.90625, 1.0)
	bodyNodes[7].setColor(0.898438, 0.617188, 0.90625, 1.0)
	bodyNodes[8].setColor(0.898438, 0.617188, 0.90625, 1.0)
	bodyNodes[9].setColor(0.898438, 0.617188, 0.90625, 1.0)
if linecache.getline('DataFolder/Data.txt', 3) == 'gray\n' or linecache.getline('DataFolder/Data.txt', 3) == 'grey\n':
	bodyNodes[0].setColor(1, 1, 1, 1)
	bodyNodes[1].setColor(0.7, 0.7, 0.8, 1.0)
	bodyNodes[2].setColor(0.7, 0.7, 0.8, 1.0)
	bodyNodes[3].setColor(1, 1, 1, 1)
	bodyNodes[4].setColor(1, 1, 1, 1)
	bodyNodes[5].setColor(1, 1, 1, 1)
	bodyNodes[6].setColor(0.7, 0.7, 0.8, 1.0)
	bodyNodes[7].setColor(0.7, 0.7, 0.8, 1.0)
	bodyNodes[8].setColor(0.7, 0.7, 0.8, 1.0)
	bodyNodes[9].setColor(0.7, 0.7, 0.8, 1.0)
	
if toontype == 'dog\n':
	duckBody.find('**/ears').setColor(0, 0, 0, 1)
	
if toontype == 'monkey\n':
	duckBody.findAllMatches('**/*ears*').setColor(0.996094, 0.957031, 0.597656, 1.0)
 
topTex = loader.loadTexture('phase_3/maps/desat_shirt_5.jpg')
botTex = loader.loadTexture('phase_4/maps/CowboyShorts1.jpg')
sleeveTex = loader.loadTexture('phase_3/maps/desat_sleeve_5.jpg')
 
bodyNodes[3].setTexture(sleeveTex, 1)
bodyNodes[4].setTexture(topTex, 1)
bodyNodes[5].setTexture(botTex, 1)
 
duckBody.reparentTo(render)
 
geom = duckBody.getGeomNode()
geom.getChild(0).setSx(0.730000019073)
geom.getChild(0).setSz(0.730000019073)


posList = [(0,-6,3),
          (0, 1, 3.5),
          (8, 15, 5.5),
          (0, 17, 2.5),
          (0, -26, 7),
          (0, -19, 6.5),
          (0, -13.5, 3.0),
          (0, -13.5, 3.0)]
 
hprList = [(0,15,0),
          (0, 0, 0),
          (150, -5.5, 0),
          (180, 5.5, 0),
          (0, -5.5, 0),
          (0, -8.0, 0),
          (0, 0, 0),
          (0, 0, 0)]

offset = 3.2375
 
base.camera.reparentTo(duckBody)
base.camera.setPos(0, -10.0 - offset, offset)

class Views:
	def __init__(self):
		base.accept('tab', self.changeView)
		base.accept('shift-tab', self.changeViewRev)
		self.objectId = 0
	def changeView(self):
		if self.objectId != 7:
			base.camera.posHprInterval(0.5, posList[self.objectId], hprList[self.objectId]).start()
			self.objectId += 1
		else:
			self.objectId = 0
			base.camera.posHprInterval(0.5, posList[self.objectId], hprList[self.objectId]).start()
			self.objectId += 1
	def changeViewRev(self):
		if self.objectId != -1:
			base.camera.posHprInterval(0.5, posList[self.objectId], hprList[self.objectId]).start()
			self.objectId -= 1
		else:
			self.objectId = 6
			base.camera.posHprInterval(0.5, posList[self.objectId], hprList[self.objectId]).start()
			self.objectId -= 1
Views = Views()
wallBitmask = BitMask32(1)
floorBitmask = BitMask32(2)
base.cTrav = CollisionTraverser()
def getAirborneHeight():
    return offset + 0.025000000000000001
walkControls = GravityWalker(legacyLifter=True)
walkControls.setWallBitMask(wallBitmask)
walkControls.setFloorBitMask(floorBitmask)
walkControls.setWalkSpeed(20.0, 24.0, 12.0, 84.0)
walkControls.initializeCollisions(base.cTrav, duckBody, floorOffset=0.025, reach=4.0)
walkControls.setAirborneHeightFunc(getAirborneHeight)
walkControls.enableAvatarControls()
duckBody.physControls = walkControls
 
def setWatchKey(key, input, keyMapName):
    def watchKey(active=True):
        if active == True:
            inputState.set(input, True)
            keyMap[keyMapName] = 1
        else:
            inputState.set(input, False)
            keyMap[keyMapName] = 0
    base.accept(key, watchKey, [True])
    base.accept(key+'-up', watchKey, [False])
 
keyMap = {'left':0, 'right':0, 'forward':0, 'backward':0, 'control':0}
 
setWatchKey('arrow_up', 'forward', 'forward')
setWatchKey('control-arrow_up', 'forward', 'forward')
setWatchKey('alt-arrow_up', 'forward', 'forward')
setWatchKey('shift-arrow_up', 'forward', 'forward')
setWatchKey('arrow_down', 'reverse', 'backward')
setWatchKey('control-arrow_down', 'reverse', 'backward')
setWatchKey('alt-arrow_down', 'reverse', 'backward')
setWatchKey('shift-arrow_down', 'reverse', 'backward')
setWatchKey('arrow_left', 'turnLeft', 'left')
setWatchKey('control-arrow_left', 'turnLeft', 'left')
setWatchKey('alt-arrow_left', 'turnLeft', 'left')
setWatchKey('shift-arrow_left', 'turnLeft', 'left')
setWatchKey('arrow_right', 'turnRight', 'right')
setWatchKey('control-arrow_right', 'turnRight', 'right')
setWatchKey('alt-arrow_right', 'turnRight', 'right')
setWatchKey('shift-arrow_right', 'turnRight', 'right')
setWatchKey('control', 'jump', 'control')
 
movingNeutral, movingForward = (False, False)
movingRotation, movingBackward = (False, False)
movingJumping = False
 
def setMovementAnimation(loopName, playRate=1.0):
    global movingNeutral
    global movingForward
    global movingRotation
    global movingBackward
    global movingJumping
    if 'jump' in loopName:
        movingJumping = True
        movingForward = False
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    elif loopName == 'run':
        movingJumping = False
        movingForward = True
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    elif loopName == 'walk':
        movingJumping = False
        movingForward = False
        movingNeutral = False
        if playRate == -1.0:
            movingBackward = True
            movingRotation = False
        else:
            movingBackward = False
            movingRotation = True
    elif loopName == 'neutral':
        movingJumping = False
        movingForward = False
        movingNeutral = True
        movingRotation = False
        movingBackward = False
    else:
        movingJumping = False
        movingForward = False
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    ActorInterval(duckBody, loopName, playRate=playRate).loop()
 
def handleMovement(task):
    global movingNeutral, movingForward
    global movingRotation, movingBackward, movingJumping
    if keyMap['control'] == 1:
        if keyMap['forward'] or keyMap['backward'] or keyMap['left'] or keyMap['right']:
            if movingJumping == False:
                if duckBody.physControls.isAirborne:
                    setMovementAnimation('running-jump-idle')
                else:
                    if keyMap['forward']:
                        if movingForward == False:
                            setMovementAnimation('run')
                    elif keyMap['backward']:
                        if movingBackward == False:
                            setMovementAnimation('walk', playRate=-1.0)
                    elif keyMap['left'] or keyMap['right']:
                        if movingRotation == False:
                            setMovementAnimation('walk')
            else:
                if not duckBody.physControls.isAirborne:
                    if keyMap['forward']:
                        if movingForward == False:
                            setMovementAnimation('run')
                    elif keyMap['backward']:
                        if movingBackward == False:
                            setMovementAnimation('walk', playRate=-1.0)
                    elif keyMap['left'] or keyMap['right']:
                        if movingRotation == False:
                            setMovementAnimation('walk')
        else:
            if movingJumping == False:
                if duckBody.physControls.isAirborne:
                    setMovementAnimation('jump-idle')
                else:
                    if movingNeutral == False:
                        setMovementAnimation('neutral')
            else:
                if not duckBody.physControls.isAirborne:
                    if movingNeutral == False:
                        setMovementAnimation('neutral')
    elif keyMap['forward'] == 1:
        if movingForward == False:
            if not duckBody.physControls.isAirborne:
                setMovementAnimation('run')
    elif keyMap['backward'] == 1:
        if movingBackward == False:
            if not duckBody.physControls.isAirborne:
                setMovementAnimation('walk', playRate=-1.0)
    elif keyMap['left'] or keyMap['right']:
        if movingRotation == False:
            if not duckBody.physControls.isAirborne:
                setMovementAnimation('walk')
    else:
        if not duckBody.physControls.isAirborne:
            if movingNeutral == False:
                setMovementAnimation('neutral')
    return Task.cont
 
base.taskMgr.add(handleMovement, 'controlManager')
 
def collisionsOn():
    duckBody.physControls.setCollisionsActive(True)
    duckBody.physControls.isAirborne = True
def collisionsOff():
    duckBody.physControls.setCollisionsActive(False)
    duckBody.physControls.isAirborne = True
def toggleCollisions():
    if duckBody.physControls.getCollisionsActive():
        duckBody.physControls.setCollisionsActive(False)
        duckBody.physControls.isAirborne = True
    else:
        duckBody.physControls.setCollisionsActive(True)
        duckBody.physControls.isAirborne = True
base.accept('f1', toggleCollisions)
duckBody.collisionsOn = collisionsOn
duckBody.collisionsOff = collisionsOff
duckBody.toggleCollisions = toggleCollisions
 
localAvatar = duckBody
base.localAvatar = localAvatar

font = loader.loadFont('phase_3/models/fonts/ImpressBT.ttf')

tag = OnscreenText(text = "swag", mayChange = True, scale=.20,font=font,pos=(0,3.25),bg=(.9,.9,.9,.3),fg=(0,0,1,1),wordwrap=7,decal=True,parent=duckBody)
tag.setBillboardAxis(2)

name = linecache.getline('DataFolder/Data.txt', 2)
tag.setText(name)

onScreenDebug.enabled = True
 
def updateOnScreenDebug(task):
 
    onScreenDebug.add('Avatar Position', localAvatar.getPos())
    onScreenDebug.add('Avatar Angle', localAvatar.getHpr())
 
    return Task.cont
 
base.taskMgr.add(updateOnScreenDebug, 'UpdateOSD')
