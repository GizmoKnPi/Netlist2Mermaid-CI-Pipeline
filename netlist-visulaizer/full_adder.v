module full_adder_s (
    input wire a,
    input wire b,
    input wire cin,
    output wire sum,
    output wire carry
);
    wire w1, w2, w3, w4;

    // Strict Structural Instantiation: Gate_Type Instance_Name (.port(signal))
    XOR_GATE  xor_1 (.in1(a),  .in2(b),   .out(w1));
    XOR_GATE  xor_2 (.in1(w1), .in2(cin), .out(sum));

    AND_GATE  and_1 (.in1(a),   .in2(b), .out(w2));
    AND_GATE  and_2 (.in1(b),   .in2(cin), .out(w3));
    AND_GATE  and_3 (.in1(cin), .in2(a), .out(w4));

    // Notice we just add a third named port for the 3-input OR gate!
    OR_GATE   or_1  (.in1(w2), .in2(w3), .in3(w4), .out(carry));

endmodule