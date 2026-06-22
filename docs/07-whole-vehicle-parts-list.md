# Whole-Vehicle Parts List

This is the first pass at turning Open Kei Truck from a battery-focused research notebook into a whole-vehicle build list. It does not freeze the chassis, donor model, or legal path. It creates a traceable shopping and verification map for everything around the battery: motor, inverter, drivetrain, bed, hinges, glass, lights, steering, brakes, seats, radio, harnesses, and compliance resources.

The structured source of truth is [data/component-candidates.csv](../data/component-candidates.csv). Unknowns should stay explicit as `UKN` or `needs-*`, not hidden in prose.

## Working Strategy

1. Use a real kei truck parts catalog as the checklist for assemblies a finished truck needs.
2. Use accessible EV suppliers for high-voltage and control components.
3. Use industrial/truck-body suppliers for repeatable fabrication hardware.
4. Keep OEM donor parts for geometry and serviceability, but avoid locking the open-source design to a single imported donor until availability is proven.

## Kei Catalog Baseline

The most useful found baseline is the HA4 Honda Acty parts diagram set from Honda-Acty.com. It covers the same assembly families the open truck must replicate:

| Catalog area | Assemblies to replicate |
|---|---|
| Electrical | Headlights, front combination lamps, tail/license lamps, interior light, combination switch, horn/relay, wiper, washer, radio, heater controls |
| Steering / brake / suspension | Wheels, rear brakes, propeller/front/rear shafts, front differential, rear axle, brake master, brake lines, parking brake, lower arms, dampers, springs, steering gearbox, tie rods |
| Equipment | Floor mat, grommets, instrument panel, ducts, console, roof liner, door liner, seats, seat belts, mirrors, tools |
| Body | Front floor, inner panels, rear floor and gate, roof/front panel, main frame, splash guards, windshield, rear glass, door glass, window regulators, door locks, door panels |

Other useful catalog resources:

- Honda Acty diagrams and parts: https://honda-acty.com/parts-diagrams-ha4-honda-acty-1990-1999-models/
- Honda Acty EPC by frame code: https://honda.epc-data.com/acty_truck/
- Suzuki Carry catalog: https://www.amayama.com/en/genuine-catalogs/epc/suzuki-japan/carry
- JP-CarParts OEM catalog: https://jp-carparts.com/
- Yokohama Motors Suzuki Carry parts/manuals: https://yokohamamotors.net/page63.html and https://yokohamamotors.net/page65.html

## First Reference Choices

These are not final locks; they are the best starting assumptions for the next design pass.

| Area | Reference direction | Why |
|---|---|---|
| Motor | Bosch SMG180 OHW reference target, Fiat 500e salvage as practical source | Already matches current 400V-class, 60 kW continuous project assumption, but Bosch direct should be treated as Tier 1 / B2B only. |
| Motor alternate | Nissan Leaf EM57 drive unit first; Bolt, HyPer 9 HV, HPEVS, Cascadia, and Hypercraft as tracked alternates | Leaf looks like the best affordability/control-support path; the others cover performance, lower-voltage mule, and premium benchmark branches. |
| Battery/HV | Keep current 35-55 kWh, 300-430V pack target | Existing ADRs already set this architecture. |
| Bed | Custom bolt-on drop-side metal bed | Better open-source repeatability than chasing used imported bed panels. |
| Bed hardware | Kei-style latches/hinges first, truck-body hardware fallback | Preserves kei utility behavior while keeping domestic alternatives available. |
| Glass | Use existing kei windshield/rear/door glass for prototype geometry if possible | Custom automotive glass is possible but expensive and should wait until cab geometry is frozen. |
| Lights | DOT/SAE universal truck lights for road-path prototypes; kei lamps for styling studies | Lighting compliance depends on lamp spec and placement, not just appearance. |
| Seats/belts | Compact seats plus FMVSS-labeled 3-point belts; commercial seating as later alternate | Belts and anchorages are safety-critical and need documentation. |
| Steering | Donor kei rack/column for mule; engineered rack/column after suspension geometry is fixed | Rack travel and inner pivot spacing must match suspension. |
| Radio | Simple single-DIN 12V Bluetooth/FM unit | Easy to make optional and low impact on electrical architecture. |

## Supplier Shortlist

| Supplier/resource | Best use |
|---|---|
| Bosch Mobility | SMG180 OHW reference specifications and off-highway/Tier 1 product context, not a consumer purchase path. |
| eBay / salvage yards / EV dismantlers | Only currently tracked individual-builder source for salvaged Fiat 500e Bosch SMG-family motor, inverter, harness, and reduction hardware. |
| Thunderstruck Motors Nissan Leaf Drive System | Used Leaf drive unit source with VCU support for ZE0/AZE0/ZE1 variants. |
| Resolve-EV | Leaf controller and wiring-harness path for plug-and-play-style conversions. |
| Cascadia Motion | Integrated motor/inverter alternate with CAD/manual resources. |
| Hypercraft | Turnkey EV powertrain/battery/control packages. |
| NetGain Motors | HyPer 9 HV lower-voltage DIY kit and WarP brushed-DC comparison motors. |
| HPEVS | AC-50/AC-51 low-voltage AC motor kits for lightweight prototypes. |
| Thunderstruck Motors | EV conversion chargers, DCDC, contactors, fuses, connectors, cooling, displays. |
| Orion BMS | Custom-pack BMS alternate if an integrated-pack BMS is not used. |
| EV West | EV motors, instrumentation, shunts, adapters, conversion support parts. |
| Honda-Acty.com | Acty parts diagrams, replacement parts, seat/radio/body/electrical categories. |
| Yokohama Motors | JDM OEM/aftermarket mini-truck parts and manuals. |
| Mini4x4.ca | Suzuki Carry lights, steering, body, side/tailgate handles and hinges. |
| Oiwa Garage | U.S.-based kei accessories/parts, rubber gate protectors, model-specific parts. |
| Minitrucks.net | Body/glass, mirrors, accessories, U.S.-visible kei replacement supply. |
| Gold Star Parts | Mini-truck brakes, suspension, wheels/tires, lift/utility parts. |
| Online Metals | Standard sheet/tube stock for frame, bed, brackets. |
| SendCutSend | Repeatable laser-cut tab-and-slot plates and brackets. |
| Xometry | Tube laser and more advanced fabrication once CAD is stable. |
| McMaster-Carr | Hinges, latches, weatherstripping, fasteners, hose, fittings, electrical hardware. |
| Buyers Products | Truck-body hinges, latches, stake hardware, DOT lighting. |
| Auto Glass Japan | Existing JDM kei windshield sourcing. |
| Custom Glass Solutions / Metalcrafters | Custom laminated/prototype automotive glass path. |
| Freedman / Wesco / PRP | Seating and seat-belt sourcing paths. |

## Open Verification Questions

1. Which kei donor model is the reference geometry source: Acty, Carry, Hijet, or a blended cab/bed target?
2. Is the first rolling prototype intended as off-road/private-property, LSV, kit, or full road vehicle?
3. Which Fiat 500e Bosch SMG-family salvage package includes the motor, inverter, harness, reduction hardware, coolant fittings, HV connectors, and a proven controller path?
4. Should the practical prototype path pivot toward a Nissan Leaf drive unit because it includes motor, inverter, reduction drive, differential, and aftermarket VCU support?
5. What rear axle/final-drive layout gives the simplest serviceable drivetrain?
6. Which windshield is worth designing around before custom glass is considered?
7. What payload target should drive bed structure, rear springs, brakes, and tires?
8. Which lighting path is preferred: universal DOT lamps first or kei-style lamps first?
9. Which parts need CAD now: motor, battery, PDU, steering rack, seats, windshield, bed hinges/latches?

## Immediate Next Step

Use [data/component-candidates.csv](../data/component-candidates.csv) as the master checklist. For each high-priority row, collect four pieces of evidence before moving it toward `verified`:

- Supplier page or catalog diagram.
- Delivered quote or visible price.
- Dimensions, CAD, drawing, or fitment diagram.
- Integration or installation documentation.

The first supplier outreach pass should target Fiat 500e salvage sellers, EV dismantlers, Cascadia, Hypercraft, Thunderstruck, Mini4x4.ca, Honda-Acty.com, Yokohama Motors, Auto Glass Japan, Buyers Products, and one local/online metal fabrication path. Bosch should remain a reference-spec source unless a real B2B/integrator purchase path appears.
