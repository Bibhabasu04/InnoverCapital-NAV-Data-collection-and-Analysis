import subprocess

scripts = [
    "Codes_company/NAV_lic.py",
    "Codes_company/NAV_kotak.py",
    "Codes_company/NAV_birla.py",
    "Codes_company/NAV_bajaj.py",
    "Codes_company/NAV_hdfc.py",
    "Codes_company/NAV_icici.py",
    "Codes_company/NAV_pnb.py",
    "Codes_company/NAV_tata.py",
    "Codes_company/NAV_reliance.py",
    "Codes_company/NAV_bhartiaxa.py",
    "Codes_company/NAV_maxlife.py",
    "Codes_company/NAV_sbi.py",
]

for script in scripts:
    print(f"Running: {script}")
    subprocess.run(['python', script])
