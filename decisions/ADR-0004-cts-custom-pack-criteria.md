# ADR-0004: CTS Custom Pack Criteria

## Status
Proposed

## Context
CTS screenshots show standard LFP module families, but standard 70+ kWh and 100+ kWh configurations are too large for the kei-truck reference target.

## Decision
Ask CTS for smaller custom configurations instead of accepting the standard high-capacity rows.

Preferred asks:
1. 120S 135Ah, about 52 kWh, charge-limited to <=430 V.
2. 108S 150Ah, about 52 kWh, max around 394 V.
3. 96S 150–180Ah, about 46–55 kWh, max around 345 V.

## Consequences
- CTS remains a promising budget/custom LFP path.
- CTS is not verified until quote, CAD, BMS/PDU details, CAN docs, and warranty are received.
- MOQ 10 marketplace listings are rejected for community-builder accessibility.
