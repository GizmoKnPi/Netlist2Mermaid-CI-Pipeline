# My Capstone Hardware Project

Here is the automated architecture diagram of my top-level module(s):
### 📄 Architecture: `half_adder.v`
```mermaid
graph LR;
    %% --- COLOR CLASSES ---
    classDef AND_GATE fill:#AEC6CF,stroke:#333,stroke-width:2px,color:#000;
    classDef OR_GATE fill:#77DD77,stroke:#333,stroke-width:2px,color:#000;
    classDef XOR_GATE fill:#CFCFC4,stroke:#333,stroke-width:2px,color:#000;
    classDef NOT_GATE fill:#FDFD96,stroke:#333,stroke-width:2px,color:#000;
    classDef NAND_GATE fill:#FFB347,stroke:#333,stroke-width:2px,color:#000;
    classDef NOR_GATE fill:#FF6961,stroke:#333,stroke-width:2px,color:#000;
    classDef MUX2X1 fill:#B39EB5,stroke:#333,stroke-width:2px,color:#000;
    classDef CUSTOM_MODULE fill:#8EE1E7,stroke:#333,stroke-width:2px,color:#000;
    classDef DEFAULT_MOD fill:#f9f9f9,stroke:#333,stroke-width:2px,stroke-dasharray: 3 3,color:#000;

    LEGEND["<h4 style='margin:0px; padding-bottom:5px; color:black !important;'>IEC 60617 LEGEND</h4><div style='margin-bottom:4px; color:black !important;'><span style='display:inline-block; border:1px solid #333; background:#AEC6CF; padding:2px 8px; border-radius:3px; width:35px; text-align:center;'><b style='color:black !important;'>&amp;</b></span> AND_GATE</div><div style='margin-bottom:4px; color:black !important;'><span style='display:inline-block; border:1px solid #333; background:#CFCFC4; padding:2px 8px; border-radius:3px; width:35px; text-align:center;'><b style='color:black !important;'>=1</b></span> XOR_GATE</div>"]
    style LEGEND fill:#ffffff,stroke:#000,stroke-width:2px
    %% ----------------------------------

    U1["U1<br><b>=1</b>"]:::XOR_GATE
    a(["a"]) -->|in1| U1;
    b(["b"]) -->|in2| U1;
    U1 -->|out| sum(["sum"]);
    U2["U2<br><b>&amp;</b>"]:::AND_GATE
    a(["a"]) -->|in1| U2;
    b(["b"]) -->|in2| U2;
    U2 -->|out| carry(["carry"]);
```


## Project Details
Write your normal documentation down here.