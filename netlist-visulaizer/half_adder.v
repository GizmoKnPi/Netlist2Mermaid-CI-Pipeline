module half_adder (
    input wire a,
    input wire b,
    output wire sum,
    output wire carry
);

    // Structural instantiation of logic gates
    XOR_GATE U1 ( .in1(a), .in2(b), .out(sum) );
    AND_GATE U2 ( .in1(a), .in2(b), .out(carry) );

endmodule
