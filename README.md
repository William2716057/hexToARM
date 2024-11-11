
# ARM Assembly Disassembler
This Python script disassembles ARM machine code from a hexadecimal string input into human-readable assembly instructions. 
Using the Capstone disassembler library, the script interprets each hexadecimal instruction and outputs the assembly equivalent.

## Requirements
- Python 3.x
- Capstone disassembly library

### Installation
```
pip install capstone
```

### Usage
```
python hexToARM.py
```

### Sample Usage
```
Enter hex: 370301e3ba1c0ae3e51d4be3c82309e3592a4de3000060e2631f0ce3de1345e3c4220fe3e3244fe3010020e0020020e0ef1107e3ef1145e3792a03e31c214be3010020e0020020e0111e0ce3d5194ae33d2301e3122a4be3010000e0020000e0e11705e3611a47e3d32804e3b2294ee3010020e0020020e00b1f02e39f1349e31b2002e3272a45e3000060e25e1c09e33b184ae3c82707e34f234de3010040e00200c0e06d1f06e3cb1641e304290ce3b22340e3000060e2f41e0ae31e1e4ce379290de3de2842e3010080e1020080e1b7140ce31b1b46e3bb230be3e62b4be3010000e0020000e0be1006e3641846e3422b0be3e72c49e3010040e00200c0e0a51707e345164be3152d0fe31c2744e3900100e0900200e0311108e3be1841e3aa2708e3ca2d46e3010000e0020000e05e1806e3791a40e3942b03e3e62c40e3000060e2491603e3931d40e31b2e04e323234ae3000060e2b21600e3901b45e30f2507e3a4284be3010020e0020020e05a1e0ee3b41d4be30f2005e35f2b4fe3900100e0900200e0581901e3421242e34f2e07e305214de3010020e0020020e0b51a07e313144ee3472001e33f274ce3000060e2cc1008e3341349e3ab260ce37a2240e3010000e0020000e0
```

### result 
```
0x1000: movw    r0, #0x1337
0x1004: movw    r1, #0xacba
0x1008: movt    r1, #0xbde5
0x100c: movw    r2, #0x93c8
0x1010: movt    r2, #0xda59
0x1014: rsb     r0, r0, #0
0x1018: movw    r1, #0xcf63
0x101c: movt    r1, #0x53de
0x1020: movw    r2, #0xf2c4
0x1024: movt    r2, #0xf4e3
0x1028: eor     r0, r0, r1
0x102c: eor     r0, r0, r2
0x1030: movw    r1, #0x71ef
0x1034: movt    r1, #0x51ef
0x1038: movw    r2, #0x3a79
0x103c: movt    r2, #0xb11c
0x1040: eor     r0, r0, r1
0x1044: eor     r0, r0, r2
0x1048: movw    r1, #0xce11
0x104c: movt    r1, #0xa9d5
0x1050: movw    r2, #0x133d
0x1054: movt    r2, #0xba12
0x1058: and     r0, r0, r1
0x105c: and     r0, r0, r2
0x1060: movw    r1, #0x57e1
0x1064: movt    r1, #0x7a61
0x1068: movw    r2, #0x48d3
0x106c: movt    r2, #0xe9b2
0x1070: eor     r0, r0, r1
0x1074: eor     r0, r0, r2
0x1078: movw    r1, #0x2f0b
0x107c: movt    r1, #0x939f
0x1080: movw    r2, #0x201b
0x1084: movt    r2, #0x5a27
0x1088: rsb     r0, r0, #0
0x108c: movw    r1, #0x9c5e
0x1090: movt    r1, #0xa83b
0x1094: movw    r2, #0x77c8
0x1098: movt    r2, #0xd34f
0x109c: sub     r0, r0, r1
0x10a0: sbc     r0, r0, r2
0x10a4: movw    r1, #0x6f6d
0x10a8: movt    r1, #0x16cb
0x10ac: movw    r2, #0xc904
0x10b0: movt    r2, #0x3b2
0x10b4: rsb     r0, r0, #0
0x10b8: movw    r1, #0xaef4
0x10bc: movt    r1, #0xce1e
0x10c0: movw    r2, #0xd979
0x10c4: movt    r2, #0x28de
0x10c8: orr     r0, r0, r1
0x10cc: orr     r0, r0, r2
0x10d0: movw    r1, #0xc4b7
0x10d4: movt    r1, #0x6b1b
0x10d8: movw    r2, #0xb3bb
0x10dc: movt    r2, #0xbbe6
0x10e0: and     r0, r0, r1
0x10e4: and     r0, r0, r2
0x10e8: movw    r1, #0x60be
0x10ec: movt    r1, #0x6864
0x10f0: movw    r2, #0xbb42
0x10f4: movt    r2, #0x9ce7
0x10f8: sub     r0, r0, r1
0x10fc: sbc     r0, r0, r2
0x1100: movw    r1, #0x77a5
0x1104: movt    r1, #0xb645
0x1108: movw    r2, #0xfd15
0x110c: movt    r2, #0x471c
0x1110: mul     r0, r0, r1
0x1114: mul     r0, r0, r2
0x1118: movw    r1, #0x8131
0x111c: movt    r1, #0x18be
0x1120: movw    r2, #0x87aa
0x1124: movt    r2, #0x6dca
0x1128: and     r0, r0, r1
0x112c: and     r0, r0, r2
0x1130: movw    r1, #0x685e
0x1134: movt    r1, #0xa79
0x1138: movw    r2, #0x3b94
0x113c: movt    r2, #0xce6
0x1140: rsb     r0, r0, #0
0x1144: movw    r1, #0x3649
0x1148: movt    r1, #0xd93
0x114c: movw    r2, #0x4e1b
0x1150: movt    r2, #0xa323
0x1154: rsb     r0, r0, #0
0x1158: movw    r1, #0x6b2
0x115c: movt    r1, #0x5b90
0x1160: movw    r2, #0x750f
0x1164: movt    r2, #0xb8a4
0x1168: eor     r0, r0, r1
0x116c: eor     r0, r0, r2
0x1170: movw    r1, #0xee5a
0x1174: movt    r1, #0xbdb4
0x1178: movw    r2, #0x500f
0x117c: movt    r2, #0xfb5f
0x1180: mul     r0, r0, r1
0x1184: mul     r0, r0, r2
0x1188: movw    r1, #0x1958
0x118c: movt    r1, #0x2242
0x1190: movw    r2, #0x7e4f
0x1194: movt    r2, #0xd105
0x1198: eor     r0, r0, r1
0x119c: eor     r0, r0, r2
0x11a0: movw    r1, #0x7ab5
0x11a4: movt    r1, #0xe413
0x11a8: movw    r2, #0x1047
0x11ac: movt    r2, #0xc73f
0x11b0: rsb     r0, r0, #0
0x11b4: movw    r1, #0x80cc
0x11b8: movt    r1, #0x9334
0x11bc: movw    r2, #0xc6ab
0x11c0: movt    r2, #0x27a
0x11c4: and     r0, r0, r1
0x11c8: and     r0, r0, r2
```

