import re
import sys
import os
import argparse

def parse_netlist_to_mermaid(netlist_text):
    
    #Pre-processing: Strip all comments
    netlist_text = re.sub(r'/\*.*?\*/', '', netlist_text, flags=re.DOTALL)
    netlist_text = re.sub(r'//.*', '', netlist_text)

    #Extract Inputs/Outputs
    inputs = set(re.findall(r'\binput\s+(?:wire\s+|reg\s+)?(?:\[.*?\]\s+)?([a-zA-Z0-9_]+)', netlist_text))
    outputs = set(re.findall(r'\boutput\s+(?:wire\s+|reg\s+)?(?:\[.*?\]\s+)?([a-zA-Z0-9_]+)', netlist_text))

    #Extract Instances
    instance_pattern = re.compile(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z_][a-zA-Z0-9_\[\]:]*)\s*\((.*?)\)\s*;', re.DOTALL)
    raw_instances = instance_pattern.findall(netlist_text)
    
    ignore_words = {'module', 'assign', 'wire', 'reg', 'always', 'initial'}
    instances = [inst for inst in raw_instances if inst[0].lower() not in ignore_words]

    used_gates = set([inst[0].upper() for inst in instances])

    gate_styles = {
        "AND_GATE":  {"symbol": "&amp;",      "color": "#AEC6CF"}, 
        "OR_GATE":   {"symbol": "≥1",         "color": "#77DD77"}, 
        "XOR_GATE":  {"symbol": "=1",         "color": "#CFCFC4"}, 
        "NOT_GATE":  {"symbol": "1 ▷○",       "color": "#FDFD96"}, 
        "NAND_GATE": {"symbol": "&amp; ▷○",   "color": "#FFB347"}, 
        "NOR_GATE":  {"symbol": "≥1 ▷○",      "color": "#FF6961"}, 
        "MUX2X1":    {"symbol": "MUX",        "color": "#B39EB5"},
        "CUSTOM_MODULE": {"symbol": "CUST_MOD",        "color": "#8EE1E7"}
    }

    print("```mermaid")
    print("graph LR;") 
    print("    %% --- COLOR CLASSES ---")
    
    for gate, style in gate_styles.items():
        print(f"    classDef {gate} fill:{style['color']},stroke:#333,stroke-width:2px,color:#000;")
    print("    classDef DEFAULT_MOD fill:#f9f9f9,stroke:#333,stroke-width:2px,stroke-dasharray: 3 3,color:#000;")
    print("")

    legend_html = "<h4 style='margin:0px; padding-bottom:5px; color:black !important;'>IEC 60617 LEGEND</h4>"
    has_legend_items = False

    for gate, style in gate_styles.items():
        if gate in used_gates:
            has_legend_items = True
            box = f"<span style='display:inline-block; border:1px solid #333; background:{style['color']}; padding:2px 8px; border-radius:3px; width:35px; text-align:center;'><b style='color:black !important;'>{style['symbol']}</b></span>"
            legend_html += f"<div style='margin-bottom:4px; color:black !important;'>{box} {gate}</div>"
    
    custom_mods = [g for g in used_gates if g not in gate_styles]
    if custom_mods:
        has_legend_items = True
        box = f"<span style='display:inline-block; border:1px dashed #333; background:#f9f9f9; padding:2px 8px; border-radius:3px; width:35px; text-align:center;'><b style='color:black !important;'>⚙️</b></span>"
        legend_html += f"<div style='margin-bottom:4px; color:black !important;'>{box} CUSTOM_MODULE</div>"

    if has_legend_items:
        print(f'    LEGEND["{legend_html}"]')
        print('    style LEGEND fill:#ffffff,stroke:#000,stroke-width:2px')
        print('    %% ----------------------------------\n')

    #Draw blocks and wires
    for inst_type, inst_name, ports_str in instances:
        
        safe_node_id = inst_name.replace('[', '_').replace(']', '_').replace(':', '_')
        
        gate_info = gate_styles.get(inst_type.upper())
        if gate_info:
            symbol = gate_info["symbol"]
            css_class = inst_type.upper()
        else:
            symbol = inst_type 
            css_class = "DEFAULT_MOD"
        
        print(f'    {safe_node_id}["{inst_name}<br><b>{symbol}</b>"]:::{css_class}')
        
        port_pattern = re.compile(r'\.([a-zA-Z0-9_]+)\s*\(\s*([^)]+)\s*\)')
        ports = port_pattern.findall(ports_str)
        
        for port_name, sig_name in ports:
            sig_name = sig_name.strip()
            
           
            safe_sig_id = sig_name.replace('[', '_').replace(']', '_').replace(':', '_').replace("'", "_")
            
            base_sig_match = re.match(r'^([a-zA-Z0-9_]+)', sig_name)
            base_sig = base_sig_match.group(1) if base_sig_match else sig_name

            is_output = False
            if base_sig in outputs:
                is_output = True
            elif 'out' in port_name.lower() or port_name.lower() == 'y':
                is_output = True
            
            if is_output:
                print(f"    {safe_node_id} -->|{port_name}| {safe_sig_id}([\"{sig_name}\"]);")
            else:
                print(f"    {safe_sig_id}([\"{sig_name}\"]) -->|{port_name}| {safe_node_id};")

    print("```")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verilog Netlist to Mermaid.js Parser")
    parser.add_argument("netlist", help="Path to the Verilog (.v) file")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.netlist):
        print(f"❌ Error: Could not find the file '{args.netlist}'.")
        sys.exit(1)
        
    with open(args.netlist, 'r') as f:
        netlist_content = f.read()
        
    parse_netlist_to_mermaid(netlist_content)