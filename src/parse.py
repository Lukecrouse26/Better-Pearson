import re
import json

def parse_latex(latex):
    cleaned = re.sub(r"\\begin{.*?}|\\end{.*?}|\{|\}", "", latex)
    
    lines = [line.strip() for line in cleaned.split("\\\\") if line.strip()]

    equations = []
    for line in lines:
        if line:
            left, right = line.split('=', 1)
            equations.append({'left': left.strip(), 'right': right.strip()})
    
    return json.dumps({'equations': equations}, indent=2)