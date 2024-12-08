"""
Defines SmartThings capabilities and attributes.

https://smartthings.developer.samsung.com/docs/api-ref/capabilities.html
"""

CAPABILITIES_TO_ATTRIBUTES = {
    "accelerationSensor": ["acceleration"],
    "activityLightingMode": ["lightingMode"],
    "activitySensor": ["activity"],
    "airConditionerFanMode": ["fanMode", "supportedAcFanModes"],
    "airConditionerMode": ["airConditionerMode", "supportedAcModes"],
    "airPurifierFanMode": ["airPurifierFanMode", "supportedAirPurifierFanModes"],
    "airQualityHealthConcern": ["airQualityHealthConcern"],
    "airFlowDirection": ["airFlowDirection"],
    "airQualitySensor": ["airQuality"],
    "alarm": ["alarm"],
    "atmosphericPressureMeasurement": ["atmosphericPressure"],
    "audioMute": ["mute"],
    "audioStream": ["uri"],
    "audioTrackData": ["audioTrackData", "elapsedTime", "totalTime"],
    "audioVolume": ["volume"],
    "batteryLevel": ["battery"],
    "battery": ["battery"],
    "bodyMassIndexMeasurement": ["bmiMeasurement"],
    "bodyWeightMeasurement": ["bodyWeightMeasurement"],
    "button": ["button", "numberOfButtons", "supportedButtonValues"],
    "bypassable": ["bypassStatus"],
    "carbonDioxideHealthConcern": ["carbonDioxideHealthConcern"],
    "carbonDioxideMeasurement": ["carbonDioxide"],
    "carbonMonoxideDetector": ["carbonMonoxide"],
    "carbonMonoxideMeasurement": ["carbonMonoxideLevel"],
    "chime": ["chime"],
    "colorControl": ["color", "hue", "saturation"],
    "colorTemperature": ["colorTemperature"],
    "contactSensor": ["contact"],
    "currentMeasurement": ["current"],
    "demandResponseLoadControl": ["drlcStatus"],
    "dewpoint": ["dewpoint"],
    "dishwasherMode": ["dishwasherMode", "supportedDishwasherModes"], 
    "dishwasherOperatingState": [
        "completionTime",
        "dishwasherJobState",
        "machineState",
        "progress",
        "supportedMachineStates",
    ],
    "doorControl": ["door"],
    "dryerMode": ["dryerMode"],
    "dryerOperatingState": [
        "machineState",
        "supportedMachineStates",
        "dryerJobState",
        "completionTime",
    ],
    "dustHealthConcern": ["dustHealthConcern"],
    "dustSensor": ["fineDustLevel", "dustLevel"],
    "elevatorCall": ["callStatus"],
    "energyMeter": ["energy"],
    "equivalentCarbonDioxideMeasurement": ["equivalentCarbonDioxideMeasurement"],
    "fanOscillationMode": ["availableFanOscillationModes", "fanOscillationMode", "supportedFanOscillationModes"],
    "fanSpeed": ["fanSpeed"],
    "filterState": ["filterLifeRemaining", "supportedFilterCommands"],
    "filterStatus": ["filterStatus"],
    "fineDustHealthConcern": ["fineDustHealthConcern"],
    "fineDustSensor": ["FineDustLevel"],
    "firmwareUpdate": [
        "availableVersion",
        "currentVersion",
        "lastUpdateStatus",
        "lastUpdateStatusReason",
        "lastUpdateTime",
        "state",
        "supportedCommands",
        "updateAvailable",
    ],
    "formaldehydeHealthConcern": ["formaldehydeHealthConcern"],
    "formaldehydeMeasurement": ["formaldehydeLevel"],
    "gasDetector": ["gas"],
    "gasMeter": [
        "gasMeter",
        "gasMeterCalorific",
        "gasMeterConversion",
        "gasMeterPrecision",
        "gasMeterTime",
        "gasMeterVolume",
    ],
    "hardwareFault": ["hardwareFault"],
    "healthCheck": [
        "DeviceWatch-DeviceStatus",
        "DeviceWatch-Enroll",
        "checkInterval",
        "healthStatus",
    ],
    "humidifierMode": ["humidifierMode"],
    "illuminanceMeasurement": ["illuminance"],
    "imageCapture": ["captureTime", "encrypted", "image"],
    "infraredLevel": ["infraredLevel"],
    "keypadInput": ["supportedKeyCodes"],
    "laundryWasherRinseMode": ["rinseMode", "supportedRinseModes"],
    "laundryWasherSpinSpeed": ["spinSpeed", "supportedSpinSpeeds"],
    "lockCodes": [
        "codeChanged",
        "codeLength",
        "codeReport",
        "lock",
        "lockCodes",
        "maxCodeLength",
        "maxCodes",
        "minCodeLength",
        "scanCodes",
    ],
    "lock": ["lock", "supportedLockCommands", "supportedLockValues", "supportedUnlockDirections"],
    "mediaInputSource": ["inputSource", "supportedInputSources"],
    "mediaPlayback": ["playbackStatus", "supportedPlaybackCommands"],
    "mediaPlaybackRepeat": ["playbackRepeatMode"],
    "mediaPlaybackShuffle": ["playbackShuffle"],
    "mediaTrackControl": ["supportedTrackControlCommands"],
    "mode": ["mode", "supportedArguments", "supportedModes"],
    "moldHealthConcern": ["moldHealthConcern"],
    "momentary": ["push"],
    "motionSensor": ["motion"],
    "networkMeter": ["downlinkSpeed", "uplinkSpeed"],
    "nitrogenDioxideHealthConcern": ["nitrogenHealthConcern"],
    "nitrogenDioxideMeasurement": ["nitrogenDioxide"],
    "notification": ["deviceNotification"],
    "objectDetection": ["detected", "supportedValues"],
    "ocf": [
        "st",
        "mnfv",
        "mndt",
        "mnhw",
        "di",
        "mnsl",
        "dmv",
        "n",
        "vid",
        "mnmo",
        "mnmn",
        "mnml",
        "mnpv",
        "mnos",
        "pi",
        "icv",
    ],
    "occupancySensor": ["occupancy"],
    "odorSensor": ["odorLevel"],
    "ovenMode": ["ovenMode", "supportedOvenModes"],
    "ovenOperatingState": [
        "completionTime",
        "machineState",
        "operationTime",
        "ovenJobState",
        "progress",
        "supportedMachineStates",
    ],
    "ovenSetpoint": ["ovenSetpoint"],
    "ozoneHealthConcern": ["ozoneHealthConcern"],
    "ozoneMeasurement": ["ozone"],
    "panicAlarm": ["panicAlarm"],
    "pestControl": ["pestControl"],
    "pHMeasurement": ["pH"],
    "powerConsumptionReport": ["powerConsumption"],
    "powerMeter": ["power"],
    "powerSource": ["powerSource"],
    "precipitationSensor": ["precipitationIntensity"],
    "presenceSensor": ["presence"],
    "radonMeasurement": ["radonLevel"],
    "refresh": ["refresh"],
    "refrigiration": ["defrost", "rapidCooling", "rapidFreezing"],
    "rapidCooling": ["rapidCooling"],
    "refrigerationSetpoint": ["refrigerationSetpoint"],
    "relativeHumidityMeasurement": ["humidity"],
    "remoteControlStatus": ["remoteControlStatus"],
    "riceCooker": [
        "completionTime", 
        "cookerMode", 
        "cookerState",
        "event",
        "menu",
        "schedulableMenus",
        "scheduledTime",
        "schedulingEnabled",
        "startTime",
        "supportedCookerModes",
        "supportedEvents",
        "supportedMenus",
    ],
    "robotCleanerCleaningMode": ["robotCleanerCleaningMode"],
    "robotCleanerMovement": ["robotCleanerMovement"],
    "robotCleanerOperatingState": ["operatingState", "supportedOperatingStates"],
    "robotCleanerTurboMode": ["robotCleanerTurboMode"],
    "securitySystem": [
        "alarm",
        "securitySystemStatus",
        "sensorStatus",
        "supportedSecuritySystemCommands",
        "supportedSecuritySystemStatuses",
    ],
    "signalStrength": ["lqi", "rssi"],
    "sleepSensor": ["sleeping"],
    "smokeDetector": ["smoke"],
    "soundDetection": [
        "soundDetected",
        "soundDetectionState",
        "supportedSoundTypes",
    ],
    "soundPressureLevel": ["soundPressureLevel"],
    "soundSensor": ["sound"],
    "switchLevel": ["level"],
    "switch": ["switch"],
    "tamperAlert": ["tamper"],
    "temperatureAlarm": ["temperatureAlarm"],
    "temperatureLevel": ["supportedTemperatureLevels", "temperatureLevel"],
    "temperatureMeasurement": ["temperature", "temperatureRange"],
    "thermostat": [
        "coolingSetpoint",
        "coolingSetpointRange",
        "heatingSetpoint",
        "heatingSetpointRange",
        "schedule",
        "temperature",
        "thermostatFanMode",
        "supportedThermostatFanModes",
        "thermostatMode",
        "supportedThermostatModes",
        "thermostatOperatingState",
        "thermostatSetpoint",
        "thermostatSetpointRange",
    ],
    "thermostatCoolingSetpoint": ["coolingSetpoint", "coolingSetpointRange"],
    "thermostatFanMode": ["thermostatFanMode", "supportedThermostatFanModes"],
    "thermostatHeatingSetpoint": ["heatingSetpoint", "heatingSetpointRange"],
    "thermostatMode": ["supportedThermostatModes", "thermostatMode"],
    "thermostatOperatingState": ["thermostatOperatingState"],
    "thermostatSetpoint": ["thermostatSetpoint"],
    "threeAxis": ["threeAxis"],
    "tone": ["beep"],
    "tvChannel": ["tvChannel", "tvChannelName"],
    "tvocMeasurement": ["tvocLevel"],
    "ultravioletIndex": ["ultravioletIndex"],
    "valve": ["valve"],
    "veryFineDustHealthConcern": ["veryFineDustHealthConcern"],
    "veryFineDustSensor": ["veryFineDustLevel"],
    "videoCamera": [
        "camera",
        "mute",
        "settings",
        "statusMessage",
    ],
    "videoCapture": [
        "clip",
        "stream",
    ],
    "videoStream": ["stream", "supportedFeatures"],
    "voltageMeasurement": ["voltage"],
    "washerMode": ["washerMode"],
    "washerOperatingState": [
        "machineState",
        "supportedMachineStates",
        "washerJobState",
        "completionTime",
    ],
    "waterSensor": ["water"],
    "webrtc": [
        "audioOnly",
        "deviceIce",
        "sdpAnswer",
        "stunUrl",
        "supportedFeatures",
        "talkback",
        "turnInfo",
    ],
    "windMode": ["supportedWindModes", "windMode"],
    "windowShade": ["supportedWindowShadeCommands", "windowShade"],
    "windowShadeLevel": ["shadeLevel"],
    "windowShadePreset": ["presetPosition"],
    "zwMultiChannel": ["epEvent", "epInfo"],
}
CAPABILITIES = list(CAPABILITIES_TO_ATTRIBUTES)
ATTRIBUTES = {
    attrib
    for attributes in CAPABILITIES_TO_ATTRIBUTES.values()
    for attrib in attributes
}


class Capability:
    """Define common capabilities."""

    acceleration_sensor = "accelerationSensor"
    activity_lighting_mode = "activityLightingMode"
    activity_sensor = "activitySensor"
    air_conditioner_fan_mode = "airConditionerFanMode"
    air_conditioner_mode = "airConditionerMode"
    air_flow_direction = "airFlowDirection"
    air_purifier_fan_mode = "airPurifierFanMode"
    air_quality_health_concern = "airQualityHealthConcern"
    air_quality_sensor = "airQualitySensor"
    alarm = "alarm"
    atmospheric_pressure_measurement= "atmosphericPressureMeasurement"
    audio_mute = "audioMute"
    audio_volume = "audioVolume"
    audio_notification = "audioNotification"
    audio_stream = "audioStream"
    audio_track_data = "audioTrackData"
    audio_volume = "audioVolume"
    battery_level = "batteryLevel"
    battery = "battery"
    body_mass_index_measurement = "bodyMassIndexMeasurement"
    body_weight_measurement = "bodyWeightMeasurement"
    button = "button"
    bypassable = "bypassable"
    carbon_dioxide_health_concern = "carbonDioxideHealthConcern"
    carbon_dioxide_measurement = "carbonDioxideMeasurement"
    carbon_monoxide_detector = "carbonMonoxideDetector"
    carbon_monoxide_measurement = "carbonMonoxideMeasurement"
    chime = "chime"
    color_control = "colorControl"
    color_temperature = "colorTemperature"
    configuration = "configuration"
    contact_sensor = "contactSensor"
    current_measurement = "currentMeasurement"
    demand_response_load_control = "demandResponseLoadControl"
    dew_point = "dewPoint"
    dishwasher_mode = "dishwasherMode"
    dishwasher_operating_state = "dishwasherOperatingState"
    door_control = "doorControl"
    dryer_mode = "dryerMode"
    dryer_operating_state = "dryerOperatingState"
    dust_health_concern = "dustHealthConcern"
    dust_sensor = "dustSensor"
    elevator_call = "elevatorCall"
    energy_meter = "energyMeter"
    equivalent_carbon_dioxide_measurement = "equivalentCarbonDioxideMeasurement"
    execute = "execute"
    fan_oscillation_mode = "fanOscillationMode"
    fan_speed = "fanSpeed"
    filter_state = "filterState"
    filter_status = "filterStatus"
    fine_dust_health_concern = "fineDustHealthConcern"
    fine_dust_sensor = "fineDustSensor"
    firmware_update = "firmwareUpdate"
    formaldehyde_health_concern = "formaldehydeHealthConcern"
    formaldehyde_measurement = "formaldehydeMeasurement"
    gas_detector = "gasDetector"
    garage_door_control = "garageDoorControl"
    gas_meter = "gasMeter"
    hardware_fault = "hardwareFault"
    health_check = "healthCheck"
    humidifier_mode = "humidifierMode"
    illuminance_measurement = "illuminanceMeasurement"
    image_capture = "imageCapture"
    infrared_level = "infraredLevel"
    keypad_input = "keypadInput"
    laundry_washer_rinse_mode = "laundryWasherRinseMode"
    laundry_washer_spin_speed = "laundryWasherSpinSpeed"
    lock_codes = "lockCodes"
    lock = "lock"
    media_input_source = "mediaInputSource"
    media_playback = "mediaPlayback"
    media_playback_repeat = "mediaPlaybackRepeat"
    media_playback_shuffle = "mediaPlaybackShuffle"
    media_track_control = "mediaTrackControl"
    mode = "mode"
    mold_health_concern = "moldHealthConcern"
    momentary = "momentary"
    motion_sensor = "motionSensor"
    network_meter = "networkMeter"
    nitrogen_dioxide_health_concern = "nitrogenDioxideHealthConcern"
    nitrogen_dioxide_measurement = "nitrogenDioxideMeasurement"
    notification = "notification"
    object_detection = "objectDetection"
    occupancy_sensor = "occupancySensor"
    ocf = "ocf"
    odor_sensor = "odorSensor"
    oven_mode = "ovenMode"
    oven_operating_state = "ovenOperatingState"
    oven_setpoint = "ovenSetpoint"
    ozone_health_concern = "ozoneHealthConcern"
    ozone_measurement = "ozoneMeasurement"
    panic_alarm = "panicAlarm"
    pest_control = "pestControl"
    ph_measurement = "pHMeasurement"
    power_consumption_report = "powerConsumptionReport"
    power_meter = "powerMeter"
    power_source = "powerSource"
    precipitation_sensor = "precipitationSensor"
    presence_sensor = "presenceSensor"
    radon_measurement = "radonMeasurement"
    refresh = "refresh"
    refrigiration = "refrigiration"
    rapid_cooling = "rapidCooling"
    refrigeration_setpoint = "refrigerationSetpoint"
    relative_humidity_measurement = "relativeHumidityMeasurement"
    remote_control_status = "remoteControlStatus"
    rice_cooker = "riceCooker"
    robot_cleaner_cleaning_mode = "robotCleanerCleaningMode"
    robot_cleaner_movement = "robotCleanerMovement"
    robot_cleaner_operating_state = "robotCleanerOperatingState"
    robot_cleaner_turbo_mode = "robotCleanerTurboMode"
    security_system = "securitySystem"
    signal_strength = "signalStrength"
    sleep_sensor = "sleepSensor"
    smoke_detector = "smokeDetector"
    sound_detection = "soundDetection"
    sound_pressure_level = "soundPressureLevel"
    sound_sensor = "soundSensor"
    switch_level = "switchLevel"
    switch = "switch"
    switch_level = "switchLevel"
    tamper_alert = "tamperAlert"
    temperature_alarm = "temperatureAlarm"
    temperature_measurement = "temperatureMeasurement"
    temperature_setpoint = "temperatureSetpoint"
    thermostat = "thermostat"
    thermostat_cooling_setpoint = "thermostatCoolingSetpoint"
    thermostat_fan_mode = "thermostatFanMode"
    thermostat_heating_setpoint = "thermostatHeatingSetpoint"
    thermostat_mode = "thermostatMode"
    thermostat_operating_state = "thermostatOperatingState"
    thermostat_setpoint = "thermostatSetpoint"
    three_axis = "threeAxis"
    tone = "tone"
    tv_channel = "tvChannel"
    tvoc_measurement = "tvocMeasurement"
    ultraviolet_index = "ultravioletIndex"
    valve = "valve"
    very_fine_dush_health_concern = "veryFineDustHealthConcern"
    very_fine_dust_sensor = "veryFineDustSensor"
    video_camera = "videoCamera"
    video_capture = "videoCapture"
    video_stream = "videoStream"
    voltage_measurement = "voltageMeasurement"
    washer_mode = "washerMode"
    washer_operating_state = "washerOperatingState"
    water_sensor = "waterSensor"
    webrtc = "webrtc"
    wind_mode = "windMode"
    window_shade = "windowShade"
    window_shade_level = "windowShadeLevel"
    window_shade_preset = "windowShadePreset"
    zw_multichannel= "zwMultichannel"


class Attribute:
    """Define common attributes."""

    acceleration = "acceleration"
    activity = "activity"
    audio_track_data = "audioTrackData"
    air_conditioner_mode = "airConditionerMode"
    air_flow_direction = "airFlowDirection"
    air_purifier_fan_mode = "airPurifierFanMode"
    air_quality = "airQuality"
    air_quality_health_concern = "airQualityHealthConcern"
    alarm = "alarm"
    atmospheric_pressure = "atmosphericPressure"
    audio_only = "audioOnly"
    available_ac_fan_modes = "availableAcFanModes"
    available_ac_modes = "availableAcModes"
    available_fan_oscillation_modes = "availableFanOscillationModes"
    available_version = "availableVersion"
    battery = "battery"
    beep = "beep"
    bmi_measurement = "bmiMeasurement"
    body_weight_measurement = "bodyWeightMeasurement"
    button = "button"
    bypass_status = "bypassStatus"
    camera = "camera"
    call_status = "callStatus"
    capture_time = "captureTime"
    carbon_dioxide = "carbonDioxide"
    carbon_dioxide_health_concern = "carbonDioxideHealthConcern"
    carbon_monoxide = "carbonMonoxide"
    carbon_monoxide_level = "carbonMonoxideLevel"
    check_interval = "checkInterval"
    chime = "chime"
    clip = "clip"
    code_changed = "codeChanged"
    code_length = "codeLength"
    code_report = "codeReport
    color = "color"
    color_temperature = "colorTemperature"
    completion_time = "completionTime"
    contact = "contact"
    cooker_mode = "cookerMode"
    cooker_state = "cookerState"
    cooling_setpoint = "coolingSetpoint"
    cooling_setpoint_range = "coolingSetpointRange"
    current = "current"
    current_version = "currentVersion"
    data = "data"
    defrost = "defrost"
    detected = "detected"
    device_ice = "deviceIce"
    device_watch_device_status = "DeviceWatch-DeviceStatus"
    device_watch_enroll = "DeviceWatch-Enroll"
    dewpoint = "dewpoint"
    di = "di"
    dishwasher_job_state = "dishwasherJobState"
    dishwasher_mode = "dishwasherMode"
    dmv = "dmv"
    door = "door"
    downlink_speed = "downlinkSpeed"
    drlc_status = "drlcStatus"
    dryer_job_state = "dryerJobState"
    dryer_mode = "dryerMode"
    dust_health_concern = "dustHealthConcern"
    dust_level = "dustLevel"
    encrypted = "encrypted"
    energy = "energy"
    elapsed_time = "elapsedTime"
    equivalent_carbon_dioxide_measurement = "equivalentCarbonDioxideMeasurement"
    event = "event"
    ep_event = "epEvent"
    ep_info = "epInfo"
    fan_mode = "fanMode"
    fan_oscillation_mode = "fanOscillationMode"
    fan_speed = "fanSpeed"
    filter_life_remaining = "filterLifeRemaining"
    filter_status = "filterStatus"
    fine_dust_health_concern = "fineDustHealthConcern"
    fine_dust_level = "fineDustLevel"
    formaldehyde_level = "formaldehydeLevel"
    formaldehyde_health_concern = "formaldehydeHealthConcern"
    gas = "gas"
    gas_meter = "gasMeter"
    gas_meter_calorific = "gasMeterCalorific"
    gas_meter_conversion = "gasMeterConversion"
    gas_meter_precision = "gasMeterPrecision"
    gas_meter_time = "gasMeterTime"
    gas_meter_volume = "gasMeterVolume"
    hardware_fault = "hardwareFault"
    health_status = "healthStatus"
    heating_setpoint = "heatingSetpoint"
    heating_setpoint_range = "heatingSetpointRange"
    hue = "hue"
    humidifier_mode = "humidifierMode"
    humidity = "humidity"
    icv = "icv"
    illuminance = "illuminance"
    image = "image"
    infrared_level = "infraredLevel"
    input_source = "inputSource"
    last_update_status = "lastUpdateStatus"
    last_update_status_reason = "lastUpdateStatusReason"
    last_update_time = "lastUpdateTime"
    level = "level"
    level_range = "levelRange"
    lighting_mode = "lightingMode"
    lock = "lock"
    lock_codes = "lockCodes"
    lqi = "lqi"
    machine_state = "machineState"
    max_code_length = "maxCodeLength"
    max_codes = "maxCodes"
    menu = "menu"
    min_code_length = "minCodeLength"
    mndt = "mndt"
    mnfv = "mnfv"
    mnhw = "mnhw"
    mnml = "mnml"
    mnmn = "mnmn"
    mnmo = "mnmo"
    mnos = "mnos"
    mnpv = "mnpv"
    mnsl = "mnsl"
    mode = "mode"
    mold_health_concern = "moldHealthConcern"
    motion = "motion"
    mute = "mute"
    n = "n"
    nitrogen_dioxide_health_concern = "nitrogenDioxideHealthConcern"
    nitrogen_dioxide_measurement = "nitrogenDioxideMeasurement"
    number_of_buttons = "numberOfButtons"
    occupancy = "occupancy"
    odor_level = "odorLevel"
    operation_time = "operationTime"
    operating_state = "operatingState"
    oven_job_state = "ovenJobState"
    oven_mode = "ovenMode"
    oven_setpoint = "ovenSetpoint"
    ozone = "ozone"
    ozone_health_concern = "ozoneHealthConcern"
    panic_alarm = "panicAlarm"
    pest_control = "pestControl"
    ph = "pH"
    pi = "pi"
    playback_repeat_mode = "playbackRepeatMode"
    playback_shuffle = "playbackShuffle"
    playback_status = "playbackStatus"
    power = "power"
    power_consumption = "powerConsumption"
    power_source = "powerSource"
    precipitation_intensity = "precipitationIntensity"
    presence = "presence"
    preset_position = "presetPosition"
    progress = "progress"
    push = "push"
    quantity = "quantity"
    radon_level = "radonLevel"
    rapid_cooling = "rapidCooling"
    rapid_freezing = "rapidFreezing"
    refresh = "refresh"
    refrigeration_setpoint = "refrigerationSetpoint"
    remote_control_enabled = "remoteControlEnabled"
    rinse_mode = "rinseMode"
    robot_cleaner_cleaning_mode = "robotCleanerCleaningMode"
    robot_cleaner_movement = "robotCleanerMovement"
    robot_cleaner_turbo_mode = "robotCleanerTurboMode"
    rssi = "rssi"
    saturation = "saturation"
    sdp_answer = "sdpAnswer"
    sound_detected = "soundDetected"
    sound_detection_state = "soundDetectionState"
    sound_pressure_level = "soundPressureLevel"
    scan_codes = "scanCodes"
    schedule = "schedule"
    schedulable_menus = "schedulableMenus"
    scheduled_time = "scheduledTime"
    scheduling_enabled = "schedulingEnabled"
    security_system_status = "securitySystemStatus"
    sensor_status = "sensorStatus"
    settings = "settings"
    shade_level = "shadeLevel"
    smoke = "smoke"
    sound = "sound"
    spin_speed = "spinSpeed"
    st = "st"
    state = "state"
    status_message = "statusMessage"
    start_time = "startTime"
    stream = "stream"
    stun_url = "stunUrl"
    supported_ac_fan_modes = "supportedAcFanModes"
    supported_ac_modes = "supportedAcModes"
    supported_air_purifier_fan_modes = "supportedAirPurifierFanModes"
    supported_arguments = "supportedArguments"
    supported_button_values = "supportedButtonValues"
    supported_commands = "supportedCommands"
    supported_cooker_modes = "supportedCookerModes"
    supported_events = "supportedEvents"
    supported_fan_oscillation_modes = "supportedFanOscillationModes"
    supported_features = "supportedFeatures"
    supported_filter_commands = "supportedFilterCommands"
    supported_key_codes = "supportedKeyCodes"
    supported_input_sources = "supportedInputSources"
    supported_lock_commands = "supportedLockCommands"
    supported_lock_values = "supportedLockValues"
    supported_machine_states = "supportedMachineStates"
    supported_menus = "supportedMenus"
    supported_modes = "supportedModes"
    supported_operating_states = "supportedOperatingStates"
    supported_playback_commands = "supportedPlaybackCommands"
    supported_rinse_modes = "supportedRinseModes"
    supported_security_system_commands = "supportedSecuritySystemCommands"
    supported_security_system_statuses = "supportedSecuritySystemStatuses"
    supported_sound_types = "supportedSoundTypes"
    supported_spin_speeds = "supportedSpinSpeeds"
    supported_temperature_levels = "supportedTemperatureLevels"
    supported_thermostat_fan_modes = "supportedThermostatFanModes"
    supported_thermostat_modes = "supportedThermostatModes"
    supported_track_control_commands = "supportedTrackControlCommands"
    supported_unlock_directions = "supportedUnlockDirections"
    supported_values = "supportedValues"
    supported_wind_modes = "supportedWindModes"
    switch = "switch"
    talkback = "talkback"
    tamper = "tamper"
    temperature = "temperature"
    temperature_alarm = "temperatureAlarm"
    temperature_level = "temperatureLevel"
    thermostat_fan_mode = "thermostatFanMode"
    thermostat_mode = "thermostatMode"
    thermostat_operating_state = "thermostatOperatingState"
    thermostat_setpoint = "thermostatSetpoint"
    thermostat_setpoint_range = "thermostatSetpointRange"
    three_axis = "threeAxis"
    total_time = "totalTime"
    turn_info = "turnInfo"
    tv_channel = "tvChannel"
    tv_channel_name = "tvChannelName"
    tvoc_level = "tvocLevel"
    type = "type"
    ultraviolet_index = "ultravioletIndex"
    update_available = "updateAvailable"
    uplink_speed = "uplinkSpeed"
    uri = "uri"
    valve = "valve"
    very_fine_dust_health_concern = "veryFineDustHealthConcern"
    very_fine_dust_level = "veryFineDustLevel"
    vid = "vid"
    voltage = "voltage"
    volume = "volume"
    washer_job_state = "washerJobState"
    washer_mode = "washerMode"
    water = "water"
    wind_mode = "windMode"
    window_shade = "windowShade"


ATTRIBUTE_ON_VALUES = {
    Attribute.acceleration: "active",
    Attribute.contact: "open",
    Attribute.filter_status: "replace",
    Attribute.motion: "active",
    Attribute.mute: "muted",
    Attribute.playback_shuffle: "enabled",
    Attribute.presence: "present",
    Attribute.sound: "detected",
    Attribute.switch: "on",
    Attribute.tamper: "detected",
    Attribute.valve: "open",
    Attribute.water: "wet",
}

ATTRIBUTE_OFF_VALUES = {
    Attribute.acceleration: "inactive",
    Attribute.contact: "closed",
    Attribute.filter_status: "normal",
    Attribute.motion: "inactive",
    Attribute.mute: "unmuted",
    Attribute.playback_shuffle: "disabled",
    Attribute.presence: "not present",
    Attribute.sound: "not detected",
    Attribute.switch: "off",
    Attribute.tamper: "clear",
    Attribute.valve: "closed",
    Attribute.water: "dry",
}
