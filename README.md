**Snip** is a an API service to link your raw 23&Me data, with a slim version of DbSNP, to return JSON data containing:

1. **Diseases** pertaining to **your** SNPs, and their ClinVar clinical significance labels.
2. **PubMed IDs** that support DbSNP's data.
3. **Frequency Studies** (i.e. GWAS) that identify how rare the SNP in sample populations (% of study population).

Your data will be uploaded to a PostgreSQL database in AWS, and only accessible with your username, password and application secret. Requests are authenticated at the app-level with a JWT. User-sensitive information (i.e. 23&Me SNP data) is stored in a table with separate permissions from the rest of the database, and only accessible from 1 endpoint.

Open to ideas on how to build interface(s) for this API, and how to leverage the data collected in an open-source, privacy-friendly fashion!

### To install:

```bash
python3.6 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### To upload your data:

1. Download your 23&Me data from their website
2. Move your 23&Me data file to this directory
3. Edit the `upload_23_and_me.py` script to set your **username and password** (it defaults to mine!).
4. Run the upload client
```bash
python upload_23_and_me.py <23_and_me_file.txt>
```

### To get your Snip data:

1. Run the download results client
```bash
python get_snip_results.py
```
2. Open the file *23_and_me.json*
