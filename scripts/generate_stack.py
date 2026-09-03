from pathlib import Path

OUTPUT = Path("assets/expertise.svg")

svg = """<svg width="1000" height="520" viewBox="0 0 1000 520"
xmlns="http://www.w3.org/2000/svg">

<rect width="1000" height="520" rx="18" fill="#0d1117"/>
<rect x="1" y="1" width="998" height="518" rx="17"
      fill="none" stroke="#30363d"/>

<!-- Terminal top bar -->
<rect width="1000" height="52" rx="18" fill="#161b22"/>
<rect y="34" width="1000" height="18" fill="#161b22"/>

<circle cx="30" cy="26" r="7" fill="#ff5f56"/>
<circle cx="54" cy="26" r="7" fill="#ffbd2e"/>
<circle cx="78" cy="26" r="7" fill="#3fb950"/>

<text x="108" y="32"
      font-family="Menlo, Monaco, Consolas, monospace"
      font-size="16"
      fill="#8b949e">
$ ./expertise.sh
</text>

<!-- Title -->
<text x="55" y="105"
      font-family="Menlo, Monaco, Consolas, monospace"
      font-size="24"
      fill="#58a6ff">
TECHNICAL EXPERTISE
</text>

<!-- Backend -->
<text x="55" y="155"
      font-family="Arial, sans-serif"
      font-size="22"
      font-weight="bold"
      fill="#f0f6fc">
BACKEND DEVELOPMENT
</text>

<text x="70" y="190"
      font-family="Menlo, Monaco, Consolas, monospace"
      font-size="18"
      fill="#3fb950">
├── PHP
</text>

<text x="70" y="220"
      font-family="Menlo, Monaco, Consolas, monospace"
      font-size="18"
      fill="#3fb950">
├── Laravel
</text>

<text x="70" y="250"
      font-family="Menlo, Monaco, Consolas, monospace"
      font-size="18"
      fill="#3fb950">
└── CakePHP
</text>

<!-- Enterprise -->
<text x="520" y="155"
      font-family="Arial, sans-serif"
      font-size="22"
      font-weight="bold"
      fill="#f0f6fc">
ENTERPRISE SYSTEMS
</text>

<text x="535" y="190"
      font-family="Menlo, Monaco, Consolas, monospace"
      font-size="18"
      fill="#a371f7">
├── Custom CRM
</text>

<text x="535" y="220"
      font-family="Menlo, Monaco, Consolas, monospace"
      font-size="18"
      fill="#a371f7">
├── ERP Solutions
</text>

<text x="535" y="250"
      font-family="Menlo, Monaco, Consolas, monospace"
      font-size="18"
      fill="#a371f7">
└── ERPNext / Frappe
</text>

<!-- Mobile -->
<text x="55" y="325"
      font-family="Arial, sans-serif"
      font-size="22"
      font-weight="bold"
      fill="#f0f6fc">
MOBILE DEVELOPMENT
</text>

<text x="70" y="365"
      font-family="Menlo, Monaco, Consolas, monospace"
      font-size="18"
      fill="#58a6ff">
└── Flutter
</text>

<!-- Infrastructure -->
<text x="520" y="325"
      font-family="Arial, sans-serif"
      font-size="22"
      font-weight="bold"
      fill="#f0f6fc">
INFRASTRUCTURE
</text>

<text x="535" y="365"
      font-family="Menlo, Monaco, Consolas, monospace"
      font-size="18"
      fill="#f0883e">
├── Linux
</text>

<text x="535" y="395"
      font-family="Menlo, Monaco, Consolas, monospace"
      font-size="18"
      fill="#f0883e">
├── Git / GitHub
</text>

<text x="535" y="425"
      font-family="Menlo, Monaco, Consolas, monospace"
      font-size="18"
      fill="#f0883e">
└── VPS Deployment
</text>

<!-- Footer -->
<line x1="55" y1="465" x2="945" y2="465"
      stroke="#30363d"/>

<text x="55" y="495"
      font-family="Menlo, Monaco, Consolas, monospace"
      font-size="15"
      fill="#8b949e">
STATUS: BUILDING SCALABLE DIGITAL SOLUTIONS
</text>

</svg>
"""

OUTPUT.parent.mkdir(exist_ok=True)
OUTPUT.write_text(svg, encoding="utf-8")

print(f"Generated: {OUTPUT}")