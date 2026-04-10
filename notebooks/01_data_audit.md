# 01 - Data Audit

## Dataset overview
- 10,000 rows
- 5 columns
- fields: User ID, Timestamp, Channel, Campaign, Conversion

## Initial quality notes
- no missing values expected in key identifiers
- conversion is binary (Yes/No)
- campaign has placeholder `-` values
- dataset is suitable for user journey modeling

## Next
- parse timestamps
- validate duplicates by user + timestamp + channel
- inspect channel and campaign distributions
