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

#### 2/ Create a local virtual env and activate it.
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3/ Install requirements.
```bash
pip install -r requirements.txt
```

#### 4/ Configure your environment variable
```bash
cp .env.example .env
nano .env # Paste your CMC_PRO_API_KEY. Then ctrl+q -> y -> Enter to save the file.
```
Edit the environnment variable : 
- Add your CMC_PRO_API_KEY
- Update the TIME_START and TIME_END (keep the format as shown in .env.example).

##### Apply your environment variable.
```bash
source .env
```

#### 5/ Run the script.
```bash
python3 src/main.py
```

## Results
Results are stored in the `output` folder. 

Raw data can be find as `cmc_data.json`.

A more user friendly version is available as the `cmc100_constituents.csv`. 

A pie chart with the Top 5 constituents is also generated as `cmc100_pie_chart.png`. 

You can edit the number of top in the `main.py` script.
