import typing
from Options import TextChoice, Option, Range, Toggle, DeathLink, Choice

# -----------------------Settings for Gameplay decisions ---------------

class InitialWeapon(Choice):
    """Chose your initial weapon. Note you are not be able to equip the sword in the weapon hub in WeaponSanity
     """
    display_name = "Weapon"
    option_Sword = 0
    option_Bow = 1
    option_Spear = 2
    option_Shield = 3
    option_Fist = 4
    option_Gun = 5

class LocationSystem(Choice):
    """Chose how the game gives you items. (1) RoomBased gives items on every new room completed. (2) ScoreBased
    gives items according to score obtained by clearing rooms (even repeated ones). (3) RoomWeaponBased gives
    items on every new room completed with a new weapon (so more locations than the original room based system)"""
    display_name = "Location System"
    option_roombased = 1
    option_scorebased = 2
    option_roomweaponbased = 3
    default = 1
    

class ScoreRewardsAmount(Range):
    """When using score based system, this sets how many checks are available based on the score. 
    Each room in hades gives "its depth" in score when completed, and each new check needs one more 
    point to be unlocked (so check 10 needs 10 points, which can be obtained, for example, 
    by completing rooms 5 and 6)"""
    display_name = "ScoreRewardsAmount"
    range_start = 72
    range_end = 1000
    default = 300

class KeepsakeSanity(Toggle):
    """Shuffles NPCs' keepsakes into the item pool, eand makes each keepsake location a check. 
    For simplicity this does not affects Hades and Persephone."""
    display_name = "KeepsakeSanity"
    option_true = 1
    option_false = 0
    default = 1
    
class WeaponSanity(Toggle):
    """Shuffles weapons (except your initial weapon) into the item pool, and makes obtaining 
    each weapon at the House Contractor's shop a check. 
    Need to be sent the weapon item to gain the skill to equip them."""
    display_name = "WeaponSanity"
    option_true = 1
    option_false = 0
    default = 1 
    
class HiddenAspectSanity(Toggle):
    """Shuffles weapon aspects into the item pool, and makes obtaining each aspect a check 
    (which needs to be unlocked before being able to be bought)."""
    display_name = "HiddenAspectSanity"
    option_true = 1
    option_false = 0
    default = 1 

class StoreSanity(Toggle):
    """Shuffles important items from the House Contractor's shop in the item pool.
    Need to be sent the items to gain the different perks that make runs easier."""
    display_name = "StoreSanity"
    option_true = 1
    option_false = 0
    default = 1 
    
class FateSanity(Toggle):
    """Shuffles most rewards from the Fated List of Prophecies into the item pool, 
    and makes the corresponding items from the list a check. 
    Can make the games significantly longer"""
    display_name = "FateSanity"
    option_true = 1
    option_false = 0
    default = 1 


# -------------------- Endgame settings

class HadesDefeatsNeeded(Range):
    """How many times you need to defeat Hades to win the world. 10 is for credits."""
    display_name = "HadesDefeatsNeeded"
    range_start = 1
    range_end = 20
    default = 1

class WeaponsClearsNeeded(Range):
    """How many different weapons clears are needed to win the world."""
    display_name = "WeaponsClearsNeeded"
    range_start = 1
    range_end = 6
    default = 1
    
class KeepsakesNeeded(Range):
    """How many different keepsake unlocks are needed to win the world."""
    display_name = "KeepsakesNeeded"
    range_start = 0
    range_end = 23
    default = 0

class FatesNeeded(Range):
    """How many different Fated List completions are needed to win the world."""
    display_name = "FatesNeeded"
    range_start = 0
    range_end = 35
    default = 0


# -----------------------Settings for Pact levels ---------------

class HeatSystem(Choice):
    """Choose either ReverseHeat (1), MinimalHeat (2) or VanillaHeat(3) for the game.
    In ReverseHeat you start with heat pacts that cannot be disabled until you get the corresponding pact item.
    In Minimal the settings for the PactsAmounts below set your minimal heat to be set, and cannot go below that level.
    If not wanting to have one of this heat systems on, chose Vanilla heat 
    (then the following options related to pacts do nothing)."""
    display_name = "Heat System"
    option_reverseheat = 1
    option_minimalheat = 2
    option_vanilllaheat = 3
    default = 1


class HardLaborPactAmount(Range):
    """Choose the amount of Hard Labor pacts in the pool."""
    display_name = "Hard Labor Pact Amount"
    range_start = 0
    range_end = 5
    default = 3
    internal_name = "HardLaborPactLevel"

class LastingConsequencesPactAmount(Range):
    """Choose the amount of Lasting Consequences pacts in the pool. """
    display_name = "Lasting Consequences Pact Amount"
    range_start = 0
    range_end = 4
    default = 2
    internal_name = "LastingConsequencesPactLevel"

class ConvenienceFeePactAmount(Range):
    """Choose the amount of Convenience Fee pacts in the pool."""
    display_name = "Convenience Fee Pact Amount"
    range_start = 0
    range_end = 2
    default = 1
    internal_name = "ConvenienceFeePactLevel"

class JurySummonsPactAmount(Range):
    """Choose the amount of Jury Summons pacts in the pool."""
    display_name = "Jury Summons Pact Amount"
    range_start = 0
    range_end = 3
    default = 2
    internal_name = "JurySummonsPactLevel"

class ExtremeMeasuresPactAmount(Range):
    """Choose the amount of Extreme Measures pacts in the pool. """
    display_name = "Extreme Measures Pact Amount"
    range_start = 0
    range_end = 4
    default = 2
    internal_name = "ExtremeMeasuresPactLevel"

class CalisthenicsProgramPactAmount(Range):
    """Choose the amount of Calisthenics Program pacts in the pool."""
    display_name = "Calisthenics Program Pact Amount"
    range_start = 0
    range_end = 2
    default = 1
    internal_name = "CalisthenicsProgramPactLevel"

class BenefitsPackagePactAmount(Range):
    """Choose the amount of Benefits Package pacts in the pool."""
    display_name = "Benefits Package Pact Amount"
    range_start = 0
    range_end = 2
    default = 1
    internal_name = "BenefitsPackagePactLevel"

class MiddleManagementPactAmount(Range):
    """Choose the amount of Middle Management pacts in the pool."""
    display_name = "Middle Management Pact Amount"
    range_start = 0
    range_end = 1
    default = 1
    internal_name = "MiddleManagementPactLevel"

class UnderworldCustomsPactAmount(Range):
    """Choose the amount of Underworld Customs pacts in the pool."""
    display_name = "Underworld Customs Pact Amount"
    range_start = 0
    range_end = 1
    default = 1
    internal_name = "UnderworldCustomsPactLevel"

class ForcedOvertimePactAmount(Range):
    """Choose the amount of Forced Overtime pacts in the pool."""
    display_name = "Forced Overtime Pact Amount"
    range_start = 0
    range_end = 2
    default = 1
    internal_name = "ForcedOvertimePactLevel"

class HeightenedSecurityPactAmount(Range):
    """Choose the amount of Heightened Security pacts in the pool."""
    display_name = "Heightened Security Pact Amount"
    range_start = 0
    range_end = 1
    default = 1
    internal_name = "HeightenedSecurityPactLevel"

class RoutineInspectionPactAmount(Range):
    """Choose the amount of Routine Inspection pacts in the pool."""
    display_name = "Routine Inspection Pact Amount"
    range_start = 0
    range_end = 4
    default = 3
    internal_name = "RoutineInspectionPactLevel"

class DamageControlPactAmount(Range):
    """Choose the amount of Damage Control pacts in the pool."""
    display_name = "Damage Control Pact Amount"
    range_start = 0
    range_end = 2
    default = 1
    internal_name = "DamageControlPactLevel"

class ApprovalProcessPactAmount(Range):
    """Choose the amount of Approval Process pacts in the pool."""
    display_name = "Approval Process Pact Amount"
    range_start = 0
    range_end = 2
    default = 1
    internal_name = "ApprovalProcessPactLevel"

class TightDeadlinePactAmount(Range):
    """Choose the amount of Tight Deadline pacts in the pool."""
    display_name = "Tight Deadline Pact Amount"
    range_start = 0
    range_end = 3
    default = 2
    internal_name = "TightDeadlinePactLevel"

class PersonalLiabilityPactAmount(Range):
    """Choose the amount of Personal Liability pacts in the pool."""
    display_name = "Personal Liability Pact Amount"
    range_start = 0
    range_end = 1
    default = 0
    internal_name = "PersonalLiabilityPactLevel"


# -----------------------Settings for Filler items ---------------

class DarknessPackValue(Range):
    """Choose the value(amount of darkness) of each darkness pack in the pool. 
    If set to 0 Darkness will not appear in the pool."""
    display_name = "Darkness Pack Value"
    range_start = 0
    range_end = 10000
    default = 1000
    internal_name = "DarknessPackValue"

class KeysPackValue(Range):
    """Choose the value(amount of Keys) of each Keys pack in the pool.
    If set to 0 Keys will not appear in the pool"""
    display_name = "Keys Pack Value"
    range_start = 0
    range_end = 500
    default = 20
    internal_name = "KeysPackValue"

class GemstonesPackValue(Range):
    """Choose the value(amount of Gemstones) of each Gemstone pack in the pool. 
    If set to 0 Gems will not appear in the pool"""
    display_name = "Gemstone Pack Value"
    range_start = 0
    range_end = 2500
    default = 100
    internal_name = "GemstonePackValue"

class DiamondsPackValue(Range):
    """Choose the value(amount of diamonds) of each diamond pack in the pool. 
    If set to 0 Diamonds will not appear in the pool"""
    display_name = "Diamonds Pack Value"
    range_start = 0
    range_end = 100
    default = 15
    internal_name = "DiamondsPackValue"

class TitanBloodPackValue(Range):
    """Choose the value(amount of Titan blood) of each Titan blood pack in the pool. 
    If set to 0 Titan blood will not appear in the pool"""
    display_name = "Titan Blood Pack Value"
    range_start = 0
    range_end = 50
    default = 3
    internal_name = "TitanBloodPackValue"

class NectarPackValue(Range):
    """Choose the value(amount of Nectar) of each Nectar pack in the pool. 
    If set to 0 Nectar will not appear in the pool"""
    display_name = "Nectar Pack Value"
    range_start = 0
    range_end = 50
    default = 3
    internal_name = "NectarPackValue"

class AmbrosiaPackValue(Range):
    """Choose the value(amount of Ambrosia) of each Ambrosia pack in the pool. 
    If set to 0 Ambrosia will not appear in the pool"""
    display_name = "Ambrosia Pack Value"
    range_start = 0
    range_end = 50
    default = 3
    internal_name = "AmbrosiaPackValue"

# -----------------------Settings for Trap -------------------------

class FillerTrapPercentage(Range):
    """Choose the percentage of filler items in the pool that will be traps instead. 
    Traps diminish your money or health during a run."""
    display_name = "Filler Trap Percentage"
    range_start = 0
    range_end = 100
    default = 5
    internal_name = "FillerTrapPercentage"

# -----------------------Settings for QoL -------------------------

class ReverseOrderExtremeMeasure(Toggle):
    """When true the order in which extreme meassures applied is reverse 
    so level 1 is applied to Hades, instead to Meg/The Furies). 
    For a more balanced experience"""
    display_name = "ReverseOrderExtremeMeasure"
    option_true = 1
    option_false = 0
    default = 1

class IgnoreGreeceDeaths(Toggle):
    """If deaths on Greece are ignored for deathlink. Leave off for the memes."""
    display_name = "IgnoreGreeceDeaths"
    option_true = 1
    option_false = 0
    default = 1

class StoreGiveHints(Toggle):
    """If seeing an item on the House Contractor's shop/Fated List of Prophecies 
    should give a hint for it on the multiworld."""
    display_name = "StoreGiveHints"
    option_true = 1
    option_false = 0
    default = 1


# ------------------------------ Building dictionary ------------------------


hades_options: typing.Dict[str, type(Option)] = {
    "initial_weapon": InitialWeapon,
    "location_system": LocationSystem,
    "score_rewards_amount": ScoreRewardsAmount,
    "keepsakesanity": KeepsakeSanity,
    "weaponsanity": WeaponSanity,
    "hidden_aspectsanity": HiddenAspectSanity,
    "storesanity": StoreSanity,
    "fatesanity": FateSanity,
    "hades_defeats_needed" : HadesDefeatsNeeded,
    "weapons_clears_needed": WeaponsClearsNeeded,
    "keepsakes_needed": KeepsakesNeeded,
    "fates_needed": FatesNeeded,
    "heat_system": HeatSystem,
    "hard_labor_pact_amount": HardLaborPactAmount,
    "lasting_consequences_pact_amount": LastingConsequencesPactAmount,
    "convenience_fee_pact_amount": ConvenienceFeePactAmount,
    "jury_summons_pact_amount": JurySummonsPactAmount,
    "extreme_measures_pact_amount": ExtremeMeasuresPactAmount,
    "calisthenics_program_pact_amount": CalisthenicsProgramPactAmount,
    "benefits_package_pact_amount": BenefitsPackagePactAmount,
    "middle_management_pact_amount": MiddleManagementPactAmount,
    "underworld_customs_pact_amount": UnderworldCustomsPactAmount,
    "forced_overtime_pact_amount": ForcedOvertimePactAmount,
    "heightened_security_pact_amount": HeightenedSecurityPactAmount,
    "routine_inspection_pact_amount": RoutineInspectionPactAmount,
    "damage_control_pact_amount": DamageControlPactAmount,
    "approval_process_pact_amount": ApprovalProcessPactAmount,
    "tight_deadline_pact_amount": TightDeadlinePactAmount,
    "personal_liability_pact_amount": PersonalLiabilityPactAmount,
    "darkness_pack_value": DarknessPackValue,
    "keys_pack_value": KeysPackValue,
    "gemstones_pack_value": GemstonesPackValue,
    "diamonds_pack_value": DiamondsPackValue,
    "titan_blood_pack_value": TitanBloodPackValue,
    "nectar_pack_value": NectarPackValue,
    "ambrosia_pack_value": AmbrosiaPackValue,
    "filler_trap_percentage": FillerTrapPercentage,
    "reverse_order_em": ReverseOrderExtremeMeasure,
    "ignore_greece_deaths": IgnoreGreeceDeaths,
    "store_give_hints": StoreGiveHints,
    "death_link": DeathLink,
}
