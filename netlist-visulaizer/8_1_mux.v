module mux8_1_structural(
    input [7:0] data_in, // 8-bit data input vector (D0-D7)
    input [2:0] sel,     // 3-bit select line vector (S0-S2)
    output y             // Output
);
    // Declare intermediate wires to connect the sub-modules
    wire y2, y3;

    // Instantiate two 4:1 MUXs for the first stage
    // The outputs of the first stage are y1 and y2
    // The inputs are split into two 4-bit groups
    // The select lines s[1:0] (S1 and S0) are shared
    mux4_1 stage1_mux1 (.i(data_in[3:0]), .s(sel[1:0]), .y(y1));
    mux4_1 stage1_mux2 (.i(data_in[7:4]), .s(sel[1:0]), .y(y2));

    // Instantiate one 2:1 MUX for the second stage
    // The inputs are the outputs from the first stage (y1, y2)
    // The select line s[2] (S2) controls which 4:1 MUX's output is chosen
    mux2_1 stage2_mux (.i0(y1), .i1(y2), .s(sel[2]), .y(y));

endmodule