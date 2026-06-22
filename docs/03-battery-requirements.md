# Battery Requirements Draft

| Requirement | Target |
|---|---:|
| Chemistry | LFP preferred |
| Energy | 35–55 kWh |
| Nominal voltage | 307–384 V preferred |
| Operating voltage | 300–430 V target |
| Continuous output | >=60 kW |
| Peak output | >=120 kW for 10–30 seconds |
| Cooling | Liquid preferred |
| CAN | Required or strongly preferred |
| BMS | Integrated preferred |
| Contactors | Integrated preferred |
| Precharge | Integrated preferred |
| Fuse | Integrated preferred |
| Isolation monitoring | Integrated preferred |
| HVIL | Required/preferred |
| Service disconnect | Required |
| CAD | STEP or package drawing required before chassis freeze |
| MOQ | 1 preferred; MOQ 10 rejected for open builder accessibility |

## Voltage guidance

Avoid packs where the normal maximum voltage exceeds the motor/inverter safe DC limit.

For LFP:
- 96S: ~307.2 V nominal, ~345.6 V max.
- 108S: ~345.6 V nominal, ~394.2 V max.
- 120S: ~384 V nominal, ~438 V max. This may work only if charger/BMS top voltage is limited to the inverter safe limit.
- 144S: ~460.8 V nominal, ~525 V max. This is not appropriate for a <=430 V target system.
