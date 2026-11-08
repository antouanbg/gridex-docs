"""Bilingual possible-integration catalogue, grounded in the project device list."""

def chapter(bg, en, rows, intro_bg, intro_en, detail_bg, detail_en):
    return dict(title=[bg,en], location=['Интеграции · възможности и комуникации','Integrations · possibilities and communications'],
                intro=[intro_bg,intro_en], rows=rows, detail=[detail_bg,detail_en])

def row(name, bg, en=None):
    labels = name.split(' / ',1) if any('\u0400' <= ch <= '\u04ff' for ch in name) else [name,name]
    return [labels[0],labels[-1],bg,en or bg]

INTRO_BG='Възможни интеграции от продуктовия каталог. Съвместимостта се определя за конкретния модел, firmware, протоколна карта и избраните функции; името на производителя само по себе си не е универсална гаранция.'
INTRO_EN='Possible integrations from the product catalogue. Compatibility is determined for the exact model, firmware, protocol map and selected functions; a manufacturer name alone is not a universal compatibility guarantee.'

def catalogue(bg,en,rows,detail_bg,detail_en):
    return chapter(bg,en,rows,INTRO_BG,INTRO_EN,detail_bg,detail_en)

chapters = [
 chapter('Интеграции: Edge инфраструктура','Integrations: Edge infrastructure',[
 row('Radxa ROCK Pi E','Централен Linux ARM64 контролер с RK3328. Локална логика, ограничения, опрашване на нодовете и драйвер за BESS.','Central Linux ARM64 controller with RK3328. Local logic, limits, node polling and BESS driver.'),
 row('OLIMEX ESP32-EVB-EA-IND','Индустриален нод с Ethernet и CAN. Един конкретен драйвер за свързаното устройство. ESP32-EVB е лабораторният вариант.','Industrial node with Ethernet and CAN. One specific driver for the attached device. ESP32-EVB is the laboratory variant.'),
 row('RS485 / UEXT / UART','Външен галванично изолиран RS485 трансивър за серийния профил на ESP32. Параметрите се задават по устройството.','External galvanically isolated RS485 transceiver for the ESP32 serial profile. Settings follow the device specification.'),
 row('Site Router / WireGuard','Рутерът поддържа защитения тунел за Обекта. ROCK Pi и ESP32 не изпълняват WireGuard.','The router owns the secure Site tunnel. ROCK Pi and ESP32 do not run WireGuard.'),
 row('OT Ethernet / Modbus TCP','Изолирана локална мрежа между ROCK Pi и ESP32 нодовете; каноничен endpoint на порт 1502.','Isolated local network between ROCK Pi and ESP32 nodes; canonical endpoint on port 1502.'),
 row('MQTT / TLS','ROCK Pi е мостът за телеметрия към частния broker през VPN. ESP32 нодовете нямат директен облачен MQTT достъп.','ROCK Pi bridges telemetry to the private broker over VPN. ESP32 nodes have no direct cloud MQTT access.')],
 'Edge свързва енергийните активи с GrideX, като запазва локалните защити и разделя производствената мрежа от облачните услуги.',
 'Edge connects energy assets to GrideX while retaining local protections and separating the operational network from cloud services.',
 'Телеметрия: устройство → CAN/RS485 → ESP32 → Modbus TCP → ROCK Pi → защитен тунел → MQTT → GrideX. Suntech STE-261L се свързва директно към ROCK Pi по Modbus TCP, без ESP32 посредник.',
 'Telemetry: device → CAN/RS485 → ESP32 → Modbus TCP → ROCK Pi → secure tunnel → MQTT → GrideX. Suntech STE-261L connects directly to ROCK Pi over Modbus TCP, without an ESP32 intermediary.'),
 catalogue('Възможни интеграции: инвертори I','Possible integrations: inverters I',[
 row('Deye','String, hybrid, P3, micro; Modbus RTU / Solarman; CAN BMS профил. SUN-xK-SG и пример SUN-50K-SG01HP3 (TCP).','String, hybrid, P3, micro; Modbus RTU / Solarman; CAN BMS profile. SUN-xK-SG and SUN-50K-SG01HP3 example (TCP).'),
 row('Sungrow','SH-RS / SH-RT: Pylon-compatible CAN път; SG125CX-P2: Modbus TCP пример. iSolarCloud конектор.','SH-RS / SH-RT: Pylon-compatible CAN path; SG125CX-P2: Modbus TCP example. iSolarCloud connector.'),
 row('Huawei','Modbus профил; SUN2000-100KTL: TCP пример. FusionSolar конектор.','Modbus profile; SUN2000-100KTL: TCP example. FusionSolar connector.'),
 row('Growatt','Modbus / RS485, LV/HV CAN; SPF 5000 ES, ES 5000, SPH, SPF 3000 ES, SPH TL3 BH UP; MAX 125KTL3-X: RTU пример.','Modbus / RS485, LV/HV CAN; SPF 5000 ES, ES 5000, SPH, SPF 3000 ES, SPH TL3 BH UP; MAX 125KTL3-X: RTU example.'),
 row('Sofar','HYD, G3, string: Modbus RTU / Solarman. HYD-ES / ME-3000SP: CAN bridge път.','HYD, G3, string: Modbus RTU / Solarman. HYD-ES / ME-3000SP: CAN bridge path.'),
 row('Solis','Hybrid, 1P-5G, 3P-4G: Modbus RTU / Solarman; HV CAN BMS профил.','Hybrid, 1P-5G, 3P-4G: Modbus RTU / Solarman; HV CAN BMS profile.'),
 row('GoodWe','ET / EH / EM; HV CAN и Pylon-compatible bridge профили.','ET / EH / EM; HV CAN and Pylon-compatible bridge profiles.'),
 row('SMA','Sunny Island 4.0H, 6.0H, 8.0H, 4548-US, 6048-US; CAN BMS профил.','Sunny Island 4.0H, 6.0H, 8.0H, 4548-US, 6048-US; CAN BMS profile.'),
 row('Victron','Cerbo GX / Multi RS; Pylon-compatible CAN и отделен нативен bridge профил.','Cerbo GX / Multi RS; Pylon-compatible CAN and a separate native bridge profile.'),
 row('SolaX','X1 / X3: Pylon-compatible CAN bridge път.','X1 / X3: Pylon-compatible CAN bridge path.')],
 'BMS интерфейсът подава заряд, ограничения и състояние към инвертора. Той не е равнозначен на пълен интерфейс за всички настройки на инвертора.',
 'The BMS interface supplies charge state, limits and status to the inverter. It is not equivalent to a full interface for every inverter setting.'),
 catalogue('Възможни интеграции: инвертори II','Possible integrations: inverters II',[
 row('Afore','T4, T6, 2MPPT, BNT-TL, hybrid; Modbus RTU / Solarman.'),
 row('Megarevo','R-3H, R6-15KH3; Modbus RTU / Solarman.'),
 row('KSTAR / xStorage','Hybrid; Modbus RTU / Solarman.'),
 row('CHINT / INVT','Hybrid; Modbus RTU.'),
 row('SRNE','Monitoring-v2; Modbus RTU.'),
 row('Bluesun','BSE12KH3 / BSE15KH3; Modbus RTU / Solarman.'),
 row('Anenji','12K-H3; RS232 сериен профил.','12K-H3; RS232 serial profile.'),
 row('Inhenergy','GPRS-WIFI профил; Modbus RTU.','GPRS-WIFI profile; Modbus RTU.'),
 row('EG4','18KPV-12LV; Modbus RTU.'),
 row('iStorage / Hinen','iStoragE / hybrid-v1.62; Modbus RTU.'),
 row('Swatten / Selfa','SiH-TH: Modbus RTU / Solarman; SFH hybrid: Modbus RTU.'),
 row('Luxpower / Sol-Ark / BYD','CAN профили за BMS връзката към инвертор.','CAN profiles for the inverter-facing BMS link.')],
 'Облачните конектори Deye Cloud, iSolarCloud, FusionSolar и ShineServer са отделен път с доставчически достъп и условия. Наличието на logger не означава автоматичен пряк Modbus TCP достъп.',
 'Deye Cloud, iSolarCloud, FusionSolar and ShineServer cloud connectors are separate paths with provider access and terms. A logger does not automatically imply direct Modbus TCP access.'),
 catalogue('Възможни интеграции: батерии и BESS','Possible integrations: batteries and BESS',[
 row('Suntech / SunStorage Pro','STE-261L / STE-261L-125P: 261 kWh / 125 kW AC-coupled BESS; Modbus TCP, порт 3200, Unit ID 1.','STE-261L / STE-261L-125P: 261 kWh / 125 kW AC-coupled BESS; Modbus TCP, port 3200, Unit ID 1.'),
 row('Sinexcel','PCS профил в Suntech STE-261L; Modbus TCP, активна/реактивна мощност и динамични лимити.','PCS profile within Suntech STE-261L; Modbus TCP, active/reactive power and dynamic limits.'),
 row('BCQ','Контролер / BMS gateway за 261 kWh кабинет; Modbus TCP, SOC, аларми и енергийни броячи.','Controller / BMS gateway for the 261 kWh cabinet; Modbus TCP, SOC, alarms and energy counters.'),
 row('Pylontech','FH3X: Modbus RTU; LV: CAN / RS485 / UART; HV PowerCube X1/X2: CAN.','FH3X: Modbus RTU; LV: CAN / RS485 / UART; HV PowerCube X1/X2: CAN.'),
 row('BYD','CAN BMS профил; Premium HV/LV протоколни семейства за bridge връзка.','CAN BMS profile; Premium HV/LV protocol families for a bridge link.'),
 row('GivEnergy','Classic Gen 2 LV, 9.5 kWh: RS485 / Modbus. Този профил не обхваща HV и All-in-one.','Classic Gen 2 LV, 9.5 kWh: RS485 / Modbus. This profile excludes HV and All-in-one.'),
 row('Pytes','RS485 V1.21 батериен профил.','RS485 V1.21 battery profile.'),
 row('Deye / TESVOLT','BOS-G: CAN / TCP пример; TPS-E PCS: Modbus TCP пример.','BOS-G: CAN / TCP example; TPS-E PCS: Modbus TCP example.'),
 row('Growatt / Huawei','Growatt LV/HV: CAN; Huawei BMS: Modbus.')],
 'Обменят се SOC/SOH, напрежение, ток, температури, аларми и разрешени граници за заряд/разряд според наличните регистри. Изборът на интерфейс не отменя BMS защитите.',
 'Data includes SOC/SOH, voltage, current, temperatures, alarms and permitted charge/discharge limits according to available registers. Interface selection does not override BMS protections.'),
 catalogue('Възможни интеграции: BMS профили','Possible integrations: BMS profiles',[
 row('Daly','CAN / RS485 / RS232-UART.'),
 row('JBD','RS485 / RS232-UART.'),
 row('JK','CAN / Modbus / RS485 / RS232-UART.'),
 row('HNGCE / MPP Solar','Modbus.'),
 row('Narada / Shoto','Modbus.'),
 row('TianPower','TP-BMS48100-LT-06, YouSolar 51.2 V rack: Modbus.'),
 row('Voltronic / ZTE','Modbus.'),
 row('LIA / Luxpower / Megarevo','CAN.'),
 row('PACE / SMA','CAN; SMA Sunny Island BMS binding.'),
 row('Samsung / Vertiv','CAN.'),
 row('Seplos','CAN / RS485.'),
 row('SacredSun','RS485.')],
 'RS485 и UART са физически интерфейси; за всеки профил се задава точният формат на съобщенията. Не всеки RS485 BMS използва Modbus и не всеки CAN профил е взаимозаменяем.',
 'RS485 and UART are physical interfaces; the exact message format is selected per profile. Not every RS485 BMS uses Modbus and CAN profiles are not automatically interchangeable.'),
 catalogue('Възможни интеграции: смартметри','Possible integrations: smart meters',[
 row('Solarman DTSD422-D3','Трифазен електромер; Modbus RTU / Solarman logger.','Three-phase meter; Modbus RTU / Solarman logger.'),
 row('Solarman DDZY422-D2','Еднофазен електромер; Modbus RTU / Solarman logger.','Single-phase meter; Modbus RTU / Solarman logger.'),
 row('Janitza UMG 604','Модел в продуктовия пример за мрежово измерване; Modbus TCP.','Model in the product grid-metering example; Modbus TCP.'),
 row('Schneider PM8000','Модел в продуктовия пример за измерване на товар; Modbus TCP.','Model in the product load-metering example; Modbus TCP.'),
 row('Modbus RTU','Сериен път през изолиран RS485 адаптер и моделно-специфична карта.','Serial path through an isolated RS485 adapter and a model-specific map.'),
 row('Modbus TCP','Ethernet път с IP/порт, Unit ID и регистрова карта за конкретния модел.','Ethernet path with IP/port, Unit ID and a register map for the exact model.')],
 'Измерването може да покрива PCC, производство и товари: мощност, напрежения, токове, честота и енергия според уреда. Посоката на токовите трансформатори, отношението им и знакът за внос/износ се задават при внедряване.',
 'Metering may cover PCC, generation and loads: power, voltages, currents, frequency and energy according to the meter. CT orientation, CT ratio and import/export sign are set during commissioning.'),
 catalogue('Възможни интеграции: протоколни мостове','Possible integrations: protocol bridges',[
 row('Pylon-compatible CAN','LV/HV BMS данни към съответстващ инвертор: лимити, SOC/SOH, pack telemetry и защитни флагове.','LV/HV BMS data to a matching inverter: limits, SOC/SOH, pack telemetry and protection flags.'),
 row('Pylon-compatible RS485','RS485 / Modbus bridge и отделни RS485 v1/v2 профили. Точният вариант се избира по двете устройства.','RS485 / Modbus bridge and separate RS485 v1/v2 profiles. The exact variant follows both devices.'),
 row('BYD-compatible CAN','Отделна CAN карта за съответното Premium HV/LV семейство.','A separate CAN map for the matching Premium HV/LV family.'),
 row('Victron native','Нативни VE.Can / VE.Bus интерфейси са отделни профили, не общ взаимозаменяем CAN порт.','Native VE.Can / VE.Bus interfaces are separate profiles, not a generic interchangeable CAN port.'),
 row('SunSpec Modbus','Стандартизирани модели за обмен; избират се точните SunSpec модели и допустими операции.','Standardised exchange models; exact SunSpec models and permitted operations are selected.'),
 row('GivEnergy → bridge','RS485/Modbus източник към избран съвместим BMS профил; превод на единици, лимити и състояния.','RS485/Modbus source to a selected compatible BMS profile; translation of units, limits and states.')],
 'Протоколният мост преобразува информацията между два конкретни интерфейса. Електрическата съвместимост, нивото на напрежение и защитите на батерията остават отделни изисквания.',
 'A protocol bridge translates information between two specific interfaces. Electrical compatibility, voltage level and battery protections remain separate requirements.'),
 chapter('Modbus: избор и съвместимост','Modbus: selection and compatibility',[
 row('TCP / RTU','TCP работи по Ethernet; RTU обикновено през RS485. Logger тунел и директен TCP endpoint са различни пътища.','TCP runs over Ethernet; RTU typically over RS485. A logger tunnel and a direct TCP endpoint are different paths.'),
 row('Адресиране / Addressing','Точен Unit ID, порт или baud/parity/stop bits; база на адресите без непроверено +1/-1 преобразуване.','Exact Unit ID, port or baud/parity/stop bits; address base without an unverified +1/-1 conversion.'),
 row('Карта / Register map','Coils, holding/input registers, function codes, размер, signed/unsigned, byte/word order и мащаб.','Coils, holding/input registers, function codes, width, signed/unsigned, byte/word order and scale.'),
 row('Данни / Data','Единици, знак за заряд/разряд и внос/износ, свежест и качество; енергийни броячи и rollover според модела.','Units, charge/discharge and import/export signs, freshness and quality; energy counters and rollover per model.'),
 row('Управление / Control','Само изрично разрешени записи; локални лимити, режим, fault/heartbeat проверки и срок на командата.','Only explicitly permitted writes; local limits, operating mode, fault/heartbeat checks and command expiry.'),
 row('Внедряване / Commissioning','Проверка на прочетените стойности срещу локалния дисплей, после проверка на разрешените действия и безопасното състояние.','Compare readings with the local display, then verify permitted actions and the safe state.')],
 'Modbus съвместимостта е съчетание от транспорт, точна регистрова карта и функции. Друг Modbus уред може да се включи с подходящ моделно-специфичен профил; наличието на порт само по себе си не определя данните.',
 'Modbus compatibility combines transport, the exact register map and functions. Another Modbus device can be integrated through a suitable model-specific profile; a port alone does not define its data.',
 'Suntech пример: ROCK Pi → Modbus TCP :3200 / Unit ID 1. Нодовете използват локален каноничен Modbus TCP :1502. Драйверът превежда картата на производителя; облачните клиенти не пишат директно към BESS или серийната шина.',
 'Suntech example: ROCK Pi → Modbus TCP :3200 / Unit ID 1. Nodes use local canonical Modbus TCP :1502. The driver translates the vendor map; cloud clients do not write directly to the BESS or serial bus.')
]
