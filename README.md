# My Capstone Hardware Project

Here is the automated architecture diagram of my top-level module(s):
### 📄 Architecture: `barrel_shifter.v`
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

    LEGEND["<h4 style='margin:0px; padding-bottom:5px; color:black !important;'>IEC 60617 LEGEND</h4><div style='margin-bottom:4px; color:black !important;'><span style='display:inline-block; border:1px solid #333; background:#B39EB5; padding:2px 8px; border-radius:3px; width:35px; text-align:center;'><b style='color:black !important;'>MUX</b></span> MUX2X1</div>"]
    style LEGEND fill:#ffffff,stroke:#000,stroke-width:2px
    %% ----------------------------------

    ins_17["ins_17<br><b>MUX</b>"]:::MUX2X1
    in_7_(["in[7]"]) -->|in0| ins_17;
    1_b0(["1'b0"]) -->|in1| ins_17;
    ctrl_2_(["ctrl[2]"]) -->|sel| ins_17;
    ins_17 -->|out| x_7_(["x[7]"]);
    ins_16["ins_16<br><b>MUX</b>"]:::MUX2X1
    in_6_(["in[6]"]) -->|in0| ins_16;
    1_b0(["1'b0"]) -->|in1| ins_16;
    ctrl_2_(["ctrl[2]"]) -->|sel| ins_16;
    ins_16 -->|out| x_6_(["x[6]"]);
    ins_15["ins_15<br><b>MUX</b>"]:::MUX2X1
    in_5_(["in[5]"]) -->|in0| ins_15;
    1_b0(["1'b0"]) -->|in1| ins_15;
    ctrl_2_(["ctrl[2]"]) -->|sel| ins_15;
    ins_15 -->|out| x_5_(["x[5]"]);
    ins_14["ins_14<br><b>MUX</b>"]:::MUX2X1
    in_4_(["in[4]"]) -->|in0| ins_14;
    1_b0(["1'b0"]) -->|in1| ins_14;
    ctrl_2_(["ctrl[2]"]) -->|sel| ins_14;
    ins_14 -->|out| x_4_(["x[4]"]);
    ins_13["ins_13<br><b>MUX</b>"]:::MUX2X1
    in_3_(["in[3]"]) -->|in0| ins_13;
    in_7_(["in[7]"]) -->|in1| ins_13;
    ctrl_2_(["ctrl[2]"]) -->|sel| ins_13;
    ins_13 -->|out| x_3_(["x[3]"]);
    ins_12["ins_12<br><b>MUX</b>"]:::MUX2X1
    in_2_(["in[2]"]) -->|in0| ins_12;
    in_6_(["in[6]"]) -->|in1| ins_12;
    ctrl_2_(["ctrl[2]"]) -->|sel| ins_12;
    ins_12 -->|out| x_2_(["x[2]"]);
    ins_11["ins_11<br><b>MUX</b>"]:::MUX2X1
    in_1_(["in[1]"]) -->|in0| ins_11;
    in_5_(["in[5]"]) -->|in1| ins_11;
    ctrl_2_(["ctrl[2]"]) -->|sel| ins_11;
    ins_11 -->|out| x_1_(["x[1]"]);
    ins_10["ins_10<br><b>MUX</b>"]:::MUX2X1
    in_0_(["in[0]"]) -->|in0| ins_10;
    in_4_(["in[4]"]) -->|in1| ins_10;
    ctrl_2_(["ctrl[2]"]) -->|sel| ins_10;
    ins_10 -->|out| x_0_(["x[0]"]);
    ins_27["ins_27<br><b>MUX</b>"]:::MUX2X1
    x_7_(["x[7]"]) -->|in0| ins_27;
    1_b0(["1'b0"]) -->|in1| ins_27;
    ctrl_1_(["ctrl[1]"]) -->|sel| ins_27;
    ins_27 -->|out| y_7_(["y[7]"]);
    ins_26["ins_26<br><b>MUX</b>"]:::MUX2X1
    x_6_(["x[6]"]) -->|in0| ins_26;
    1_b0(["1'b0"]) -->|in1| ins_26;
    ctrl_1_(["ctrl[1]"]) -->|sel| ins_26;
    ins_26 -->|out| y_6_(["y[6]"]);
    ins_25["ins_25<br><b>MUX</b>"]:::MUX2X1
    x_5_(["x[5]"]) -->|in0| ins_25;
    x_7_(["x[7]"]) -->|in1| ins_25;
    ctrl_1_(["ctrl[1]"]) -->|sel| ins_25;
    ins_25 -->|out| y_5_(["y[5]"]);
    ins_24["ins_24<br><b>MUX</b>"]:::MUX2X1
    x_4_(["x[4]"]) -->|in0| ins_24;
    x_6_(["x[6]"]) -->|in1| ins_24;
    ctrl_1_(["ctrl[1]"]) -->|sel| ins_24;
    ins_24 -->|out| y_4_(["y[4]"]);
    ins_23["ins_23<br><b>MUX</b>"]:::MUX2X1
    x_3_(["x[3]"]) -->|in0| ins_23;
    x_5_(["x[5]"]) -->|in1| ins_23;
    ctrl_1_(["ctrl[1]"]) -->|sel| ins_23;
    ins_23 -->|out| y_3_(["y[3]"]);
    ins_22["ins_22<br><b>MUX</b>"]:::MUX2X1
    x_2_(["x[2]"]) -->|in0| ins_22;
    x_4_(["x[4]"]) -->|in1| ins_22;
    ctrl_1_(["ctrl[1]"]) -->|sel| ins_22;
    ins_22 -->|out| y_2_(["y[2]"]);
    ins_21["ins_21<br><b>MUX</b>"]:::MUX2X1
    x_1_(["x[1]"]) -->|in0| ins_21;
    x_3_(["x[3]"]) -->|in1| ins_21;
    ctrl_1_(["ctrl[1]"]) -->|sel| ins_21;
    ins_21 -->|out| y_1_(["y[1]"]);
    ins_20["ins_20<br><b>MUX</b>"]:::MUX2X1
    x_0_(["x[0]"]) -->|in0| ins_20;
    x_2_(["x[2]"]) -->|in1| ins_20;
    ctrl_1_(["ctrl[1]"]) -->|sel| ins_20;
    ins_20 -->|out| y_0_(["y[0]"]);
    ins_07["ins_07<br><b>MUX</b>"]:::MUX2X1
    y_7_(["y[7]"]) -->|in0| ins_07;
    1_b0(["1'b0"]) -->|in1| ins_07;
    ctrl_0_(["ctrl[0]"]) -->|sel| ins_07;
    ins_07 -->|out| out_7_(["out[7]"]);
    ins_06["ins_06<br><b>MUX</b>"]:::MUX2X1
    y_6_(["y[6]"]) -->|in0| ins_06;
    y_7_(["y[7]"]) -->|in1| ins_06;
    ctrl_0_(["ctrl[0]"]) -->|sel| ins_06;
    ins_06 -->|out| out_6_(["out[6]"]);
    ins_05["ins_05<br><b>MUX</b>"]:::MUX2X1
    y_5_(["y[5]"]) -->|in0| ins_05;
    y_6_(["y[6]"]) -->|in1| ins_05;
    ctrl_0_(["ctrl[0]"]) -->|sel| ins_05;
    ins_05 -->|out| out_5_(["out[5]"]);
    ins_04["ins_04<br><b>MUX</b>"]:::MUX2X1
    y_4_(["y[4]"]) -->|in0| ins_04;
    y_5_(["y[5]"]) -->|in1| ins_04;
    ctrl_0_(["ctrl[0]"]) -->|sel| ins_04;
    ins_04 -->|out| out_4_(["out[4]"]);
    ins_03["ins_03<br><b>MUX</b>"]:::MUX2X1
    y_3_(["y[3]"]) -->|in0| ins_03;
    y_4_(["y[4]"]) -->|in1| ins_03;
    ctrl_0_(["ctrl[0]"]) -->|sel| ins_03;
    ins_03 -->|out| out_3_(["out[3]"]);
    ins_02["ins_02<br><b>MUX</b>"]:::MUX2X1
    y_2_(["y[2]"]) -->|in0| ins_02;
    y_3_(["y[3]"]) -->|in1| ins_02;
    ctrl_0_(["ctrl[0]"]) -->|sel| ins_02;
    ins_02 -->|out| out_2_(["out[2]"]);
    ins_01["ins_01<br><b>MUX</b>"]:::MUX2X1
    y_1_(["y[1]"]) -->|in0| ins_01;
    y_2_(["y[2]"]) -->|in1| ins_01;
    ctrl_0_(["ctrl[0]"]) -->|sel| ins_01;
    ins_01 -->|out| out_1_(["out[1]"]);
    ins_00["ins_00<br><b>MUX</b>"]:::MUX2X1
    y_0_(["y[0]"]) -->|in0| ins_00;
    y_1_(["y[1]"]) -->|in1| ins_00;
    ctrl_0_(["ctrl[0]"]) -->|sel| ins_00;
    ins_00 -->|out| out_0_(["out[0]"]);
```

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