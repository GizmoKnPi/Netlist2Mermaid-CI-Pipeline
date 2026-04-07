module mux8_1_structural(
    input [7:0] data_in, // 8-bit data input vector (D0-D7)
    input [2:0] sel,     // 3-bit select line vector (S0-S2)
    output y             // Output
);
    wire y1, y2;

    mux4_1 stage1_mux1 (.i(data_in[3:0]), .s(sel[1:0]), .y(y1));
    mux4_1 stage1_mux2 (.i(data_in[7:4]), .s(sel[1:0]), .y(y2));

    mux2_1 stage2_mux (.i0(y1), .i1(y2), .s(sel[2]), .y(y));

endmodule