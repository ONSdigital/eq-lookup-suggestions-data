# eQ Lookup Suggestions Data

This repository contains versioned TextField suggestion data for eq-questionnaire-runner

| Dataset | Description |
| ------- |-------|
| countries-of-birth.json | List of countries for country of birth questions |
| ethnic-groups.json | List of ethnic groups |
| languages.json | List of languages |
| national-identities.json | List of national identities |
| passport-countries.json | List of countries for passport questions |
| religions.json | List of religions |


Source data files are provided by the business as multiple column csv files. These can be manually added/updated in this repository at ./source-data

- source files to be provided by the business named for the above datasets

- files to be UTF-8 csv

- any values including commas should be double quoted

- header row to contain comma separated language_codes (i.e `en_gb`, `cy`, `ga`, `eo`)

- data rows to contain comma separated translated lookup values (as to be presented in the lookup lists)

- null values for a given language item can be provided by a non-spaced commas. This will result in that term not being presented as a suggestion for that language

json files can be generated from the source csv files using `pipenv run python scripts/convert_csv_to_json.py`

- expected source file location `./source-data`

- json file output location `./data`
