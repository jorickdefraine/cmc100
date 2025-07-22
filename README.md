![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)


# CMC100
Fetch the CMC100 Index composition from the CoinMarketCap api.

## Use

#### 1/ Clone the repo.
```bash
git clone https://github.com/jorickdefraine/cmc100.git
```

#### 2/ Create a local virutal env and activate it.
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3/ Install requirements.
```bash
pip install -r requirements.txt
```

#### 4/ Run the script.
```bash
python3 src/main.py
```

## Results
Results are stored in the `output` folder. The full data are available in the `cmc100_constituents.csv` file.
A pie chart with the Top 5 consitutents is generated to as `cmc100_pie_chart.png`. You can edit the number of top in the `main.py` script.
