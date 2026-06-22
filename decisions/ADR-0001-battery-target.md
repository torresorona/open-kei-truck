# ADR-0001: Battery Target Window

## Status
Proposed

## Context
Battery research quickly expands into many options, including commercial OEM packs, modular conversion packs, and custom China-sourced packs.

## Decision
Evaluate candidate batteries against this target:
- 35–55 kWh.
- LFP preferred.
- 300–430 V operating window.
- >=60 kW continuous output.
- >=120 kW peak output.
- MOQ 1 preferred.
- Integrated BMS, contactors, fuse, precharge, HVIL, isolation monitoring, CAN, and liquid cooling preferred.

## Consequences
- 70+ kWh packs are not reference-pack candidates unless a long-range variant is later defined.
- 144S / 460.8 V nominal LFP packs are out of scope for a <=430 V motor/inverter target.
- Supplier data must include weight and dimensions before package decisions.
