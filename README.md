# My Capstone Hardware Project

Here is the automated architecture diagram of my top-level module(s):
### 📄 Architecture: `full_adder.v`
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

    LEGEND["<h4 style='margin:0px; padding-bottom:5px; color:black !important;'>IEC 60617 LEGEND</h4><div style='margin-bottom:4px; color:black !important;'><span style='display:inline-block; border:1px solid #333; background:#AEC6CF; padding:2px 8px; border-radius:3px; width:35px; text-align:center;'><b style='color:black !important;'>&amp;</b></span> AND_GATE</div><div style='margin-bottom:4px; color:black !important;'><span style='display:inline-block; border:1px solid #333; background:#77DD77; padding:2px 8px; border-radius:3px; width:35px; text-align:center;'><b style='color:black !important;'>≥1</b></span> OR_GATE</div><div style='margin-bottom:4px; color:black !important;'><span style='display:inline-block; border:1px solid #333; background:#CFCFC4; padding:2px 8px; border-radius:3px; width:35px; text-align:center;'><b style='color:black !important;'>=1</b></span> XOR_GATE</div>"]
    style LEGEND fill:#ffffff,stroke:#000,stroke-width:2px
    %% ----------------------------------

    xor_1["xor_1<br><b>=1</b>"]:::XOR_GATE
    a(["a"]) -->|in1| xor_1;
    b(["b"]) -->|in2| xor_1;
    xor_1 -->|out| w1(["w1"]);
    xor_2["xor_2<br><b>=1</b>"]:::XOR_GATE
    w1(["w1"]) -->|in1| xor_2;
    cin(["cin"]) -->|in2| xor_2;
    xor_2 -->|out| sum(["sum"]);
    and_1["and_1<br><b>&amp;</b>"]:::AND_GATE
    a(["a"]) -->|in1| and_1;
    b(["b"]) -->|in2| and_1;
    and_1 -->|out| w2(["w2"]);
    and_2["and_2<br><b>&amp;</b>"]:::AND_GATE
    b(["b"]) -->|in1| and_2;
    cin(["cin"]) -->|in2| and_2;
    and_2 -->|out| w3(["w3"]);
    and_3["and_3<br><b>&amp;</b>"]:::AND_GATE
    cin(["cin"]) -->|in1| and_3;
    a(["a"]) -->|in2| and_3;
    and_3 -->|out| w4(["w4"]);
    or_1["or_1<br><b>≥1</b>"]:::OR_GATE
    w2(["w2"]) -->|in1| or_1;
    w3(["w3"]) -->|in2| or_1;
    w4(["w4"]) -->|in3| or_1;
    or_1 -->|out| carry(["carry"]);
```

### 📄 Architecture: `8_1_mux.v`
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

    LEGEND["<h4 style='margin:0px; padding-bottom:5px; color:black !important;'>IEC 60617 LEGEND</h4><div style='margin-bottom:4px; color:black !important;'><span style='display:inline-block; border:1px dashed #333; background:#f9f9f9; padding:2px 8px; border-radius:3px; width:35px; text-align:center;'><b style='color:black !important;'>⚙️</b></span> CUSTOM_MODULE</div>"]
    style LEGEND fill:#ffffff,stroke:#000,stroke-width:2px
    %% ----------------------------------

    stage1_mux1["stage1_mux1<br><b>mux4_1</b>"]:::DEFAULT_MOD
    data_in_3_0_(["data_in[3:0]"]) -->|i| stage1_mux1;
    sel_1_0_(["sel[1:0]"]) -->|s| stage1_mux1;
    stage1_mux1 -->|y| Y01(["Y01"]);
    stage1_mux2["stage1_mux2<br><b>mux4_1</b>"]:::DEFAULT_MOD
    data_in_7_4_(["data_in[7:4]"]) -->|i| stage1_mux2;
    sel_1_0_(["sel[1:0]"]) -->|s| stage1_mux2;
    stage1_mux2 -->|y| Y02(["Y02"]);
    stage2_mux["stage2_mux<br><b>mux2_1</b>"]:::DEFAULT_MOD
    Y01(["Y01"]) -->|i0| stage2_mux;
    Y02(["Y02"]) -->|i1| stage2_mux;
    sel_2_(["sel[2]"]) -->|s| stage2_mux;
    stage2_mux -->|y| y(["y"]);
```


## Project Details
Write your normal documentation down here.