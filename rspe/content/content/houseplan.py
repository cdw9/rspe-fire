# -*- coding: utf-8 -*-
from collective import dexteritytextindexer
from zope import schema

from plone.app.textfield import RichText
from plone.supermodel import model

SimpleVocabulary = schema.vocabulary.SimpleVocabulary

PropertyVocab = SimpleVocabulary.fromValues([
    u"Residence",
    u"Business",
    u"Farm Operation",
    u"Rental Property",
    u"Other"],
)
ConstructionVocab = SimpleVocabulary.fromValues([
    u"Wood Frame",
    u"Prefab",
    u"Steel Frame",
    u"Concrete/Masonry", ],
)
HeatVocab = SimpleVocabulary.fromValues([
    u"LP",
    u"Natural Gas",
    u"Wood",
    u"Other", ],
)
SwitchesVocab = SimpleVocabulary.fromValues([
    u"No switch",
    u"Automatic switch",
    u"Manual switch", ],
)
WaterVocab = SimpleVocabulary.fromValues([
    u"Pool",
    u"Wall or Large Capacity Pump",
    u"Lagoon, Pond, or Lake", ],
)
HeatUtilVocab = SimpleVocabulary.fromValues([
    u"LP",
    u"Natural Gas",
    u"Wood",
    u"Electric",
    u"Solar/Geo-Thermal",
    u"Wood Stove",
    u"Fireplace", ],
)
ConcernsVocab = SimpleVocabulary.fromValues([
    u"Machine Shed",
    u"On Farm Chemical Storage",
    u"Utility/Maintenance Shed",
    u"Diesel Fuel Storage",
    u"Gasoline Storage",
    u"Livestock Confinement",
    u"Livestock Waste Pit",
    u"Harvester Type Storage",
    u"Grain Facility",
    u"Grain Dryer Bin",
    u"Continuous Flow Grain Dryer",
    u"Ammunition Black Powder or Reloading Supplies",
    u"Home Oxygen Bottles"],
)


class IHousePlan(model.Schema):
    """
    House Plan type
    """

    dexteritytextindexer.searchable('address')
    address = schema.TextLine(
        description=u"",
        required=False,
        title=u"911 Address",
    )
    submitter = schema.TextLine(
        description=u"The person that filled out the \
                      Information report, in the Name field",
        required=False,
        title=u"Submitter",
    )
    zip_code = schema.TextLine(
        description=u"",
        required=True,
        title=u"Zip Code",
    )
    adult_occupants = schema.Int(
        description=u"Number of adults in the house",
        required=False,
        title=u"Adult Occupants",
    )
    children_occupants = schema.Int(
        description=u"Number of children in the house",
        required=False,
        title=u"Children Occupants",
    )
    elderly_occupants = schema.Int(
        description=u"Number of elderly persons in the house",
        required=False,
        title=u"Elderly Occupants",
    )
    special_needs = schema.Text(
        description=u"If occupants have any special needs, explain here",
        required=False,
        title=u"Special Needs",
    )
    dexteritytextindexer.searchable('contact_1_name')
    contact_1_name = schema.TextLine(
        description=u"",
        required=False,
        title=u"Contact 1 Name",
    )
    contact_1_number = schema.TextLine(
        description=u"",
        required=False,
        title=u"Contact 1 Number",
    )
    dexteritytextindexer.searchable('contact_2_name')
    contact_2_name = schema.TextLine(
        description=u"",
        required=False,
        title=u"Contact 2 Name",
    )
    contact_2_number = schema.TextLine(
        description=u"",
        required=False,
        title=u"Contact 2 Number",
    )
    property_type = schema.Set(
        description=u"",
        required=False,
        title=u"Property Type",
        value_type=schema.Choice(
            title=u"",
            vocabulary=PropertyVocab
        )
    )
    lessor = schema.TextLine(
        description=u"If this is a rental property, name \
                      of the current Lessor",
        required=False,
        title=u"Lessor",
    )
    property_information = schema.TextLine(
        description=u"If property type is 'other', \
                      provide more information here",
        required=False,
        title=u"Property Information",
    )
    square_footage = schema.Int(
        description=u"",
        required=False,
        title=u"Square Footage",
    )
    multi_level = schema.Bool(
        description=u"Check if house has more than one floor",
        required=False,
        title=u"Multi-level",
    )
    basement = schema.Bool(
        description=u"Check if the building has a basement",
        required=False,
        title=u"Basement",
    )
    year_built = schema.Date(
        description=u"Approximate year of the original construction",
        required=False,
        title=u"Year Built",
    )
    additions = schema.Bool(
        description=u"Check if the building has had additions",
        required=False,
        title=u"Additions",
    )
    construction_type = schema.Set(
        description=u"",
        required=False,
        title=u"Construction Type",
        value_type=schema.Choice(
            title=u"",
            vocabulary=ConstructionVocab,
        )
    )
    basement_sleeping_area = schema.Bool(
        description=u"Check if the basement has a sleeping area",
        required=False,
        title=u"Basement Sleeping Area",
    )
    basement_exterior_entrance = schema.Bool(
        description=u"Check if the basement has an exterior entrance",
        required=False,
        title=u"Basement Exterior Entrance",
    )
    garage = schema.Bool(
        description=u"Check if the house has a garage",
        required=False,
        title=u"Garage",
    )
    garage_attached = schema.Bool(
        description=u"Check if the garage is attached",
        required=False,
        title=u"Garage Attached",
    )
    garage_heated = schema.Bool(
        description=u"Check if the garage is heated",
        required=False,
        title=u"Garage Heated",
    )
    garage_heat_type = schema.Set(
        description=u"",
        required=False,
        title=u"Garage Heat Type",
        value_type=schema.Choice(
            title=u"",
            vocabulary=HeatVocab,
        )
    )
    business = schema.Bool(
        description=u"Check if any type of business is \
                      operated in the residence",
        required=False,
        title=u"Business",
    )
    business_information = schema.TextLine(
        description=u"Details of the business operated in the residence",
        required=False,
        title=u"Business Information",
    )
    operational_smoke_detectors = schema.Bool(
        description=u"Check if the residence has operational smoke detectors",
        required=False,
        title=u"Operational Smoke Detectors",
    )
    co_detectors = schema.Bool(
        description=u"Check if the residence has CO Detector(s)",
        required=False,
        title=u"CO Detectors",
    )
    automated_alarm_system = schema.Bool(
        description=u"Check if the residence has an \
                      automated fire alarm system",
        required=False,
        title=u"Automated Alarm System",
    )
    sprinkler_system = schema.Bool(
        description=u"Check if the building has a sprinkler system",
        required=False,
        title=u"Sprinkler System",
    )
    water_supply = schema.Bool(
        description=u"Check if there is a nearby water \
                      supply for fire-fighting",
        required=False,
        title=u"Water Supply",
    )
    water_supply_type = schema.Set(
        description=u"",
        required=False,
        title=u"Water Supply Type",
        value_type=schema.Choice(
            title=u"",
            vocabulary=WaterVocab,
        )
    )
    water_supply_size = schema.Int(
        description=u"Size in gallons of the pool",
        required=False,
        title=u"Water Supply Size",
    )
    water_supply_access = schema.Bool(
        description=u"Check if there is year-round access for fire trucks",
        required=False,
        title=u"Water Supply Access",
    )
    large_trucks_prohibited = schema.TextLine(
        description=u"If the roadway or driveway prohibits access of \
                      large trucks, provide information",
        required=False,
        title=u"Large Trucks Prohibited",
    )
    special_concerns_text = RichText(
        description=u"Provide information about special concerns or hazards \
                      not already mentioned",
        required=False,
        title=u"Special Concerns",
    )

    model.fieldset('utilities',
        label=u"Utilities",
        fields=['electrical_provider',
                'electrical_shut_off_location',
                'automatic_backup_generator',
                'generator_transfer_switch',
                'generator_location',
                'type_of_heat',
                'gas_provider',
                'gas_shut_off_valve',
                'gas_shut_off_valve_location',
                'lp_tank_location',
                'backup_power_storage']
    )
    electrical_provider = schema.TextLine(
        description=u"",
        required=False,
        title=u"Electrical Provider",
    )
    electrical_shut_off_location = schema.TextLine(
        description=u"Location of the electrical shut off or meter box",
        required=False,
        title=u"Electrical Shut Off Location",
    )
    automatic_backup_generator = schema.Bool(
        description=u"Check if the building has an automatic backup generator",
        required=False,
        title=u"Automatic Backup Generator",
    )
    generator_transfer_switch = schema.Set(
        description=u"If there is an automatic generator, \
                      type of transfer switch",
        required=False,
        title=u"Generator Transfer Switch",
        value_type=schema.Choice(
            title=u"",
            vocabulary=SwitchesVocab,
        )
    )
    generator_location = schema.TextLine(
        description=u"",
        required=False,
        title=u"Generator Location",
    )
    type_of_heat = schema.Set(
        description=u"",
        required=False,
        title=u"Type of Heat",
        value_type=schema.Choice(
            title=u"",
            vocabulary=HeatUtilVocab,
        )
    )
    gas_provider = schema.TextLine(
        description=u"",
        required=False,
        title=u"Gas Provider",
    )
    gas_shut_off_valve = schema.Bool(
        description=u"Check if there is a shut-off valve for the gas",
        required=False,
        title=u"Gas Shut-Off Valve",
    )
    gas_shut_off_valve_location = schema.TextLine(
        description=u"",
        required=False,
        title=u"Gas Shut-Off Valve Location",
    )
    lp_tank_location = schema.TextLine(
        description=u"",
        required=False,
        title=u"LP Tank Location",
    )
    backup_power_storage = schema.Bool(
        description=u"Check if there is solar or battery backup power storage",
        required=False,
        title=u"Backup Power Storage",
    )

    model.fieldset('outbuildings',
        label=u"Outbuildings",
        fields=['special_concerns',
                'diesel_storage_size',
                'gasoline_storage_size',
                'natural_gas_to_buildings',
                'natural_gas_shut_off',
                'lp_gas_to_buildings',
                'lp_tank_location_secondary',
                'lp_tank_size_secondary']
    )
    special_concerns = schema.Set(
        description=u"",
        required=False,
        title=u"Special Concerns",
        value_type=schema.Choice(
            title=u"",
            vocabulary=ConcernsVocab,
        )
    )
    diesel_storage_size = schema.Int(
        description=u"Size of diesel storage in gallons",
        required=False,
        title=u"Diesel Storage Size",
    )
    gasoline_storage_size = schema.Int(
        description=u"Size of gasoline storage in gallons",
        required=False,
        title=u"Gasoline Storage Size",
    )
    natural_gas_to_buildings = schema.Bool(
        description=u"Check if there is natural gas to the grain \
                      dryer and/or buildings",
        required=False,
        title=u"Natural Gas to Buildings",
    )
    natural_gas_shut_off = schema.TextLine(
        description=u"Location of the natural gas shut-off",
        required=False,
        title=u"Natural Gas Shut Off",
    )
    lp_gas_to_buildings = schema.Bool(
        description=u"Check if there is LP gas to the grain \
                      dryer and/or buildings",
        required=False,
        title=u"LP Gas to Buildings",
    )
    lp_tank_location_secondary = schema.TextLine(
        description=u"",
        required=False,
        title=u"LP Tank Location (secondary)",
    )
    lp_tank_size_secondary = schema.Int(
        description=u"Size in gallons of the secondary LP tank",
        required=False,
        title=u"LP Tank Size (secondary)",
    )
