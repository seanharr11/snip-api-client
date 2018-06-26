# Snip

**Snip** is a an API service to link your raw 23&Me data, with a slim version of DbSNP, to return JSON data containing:

1. **Diseases** pertaining to **your** SNPs, and their ClinVar clinical significance labels.
2. **PubMed IDs** that support DbSNP's data.
3. **Frequency Studies** (i.e. GWAS) that identify how rare the SNP in sample populations (% of study population).

> I gave Lightning talk on this API at PyCon2018...[you can find it on youtube here](https://www.youtube.com/watch?v=bTAFl8P2DkE&feature=youtu.be&t=3115)

Your data will be uploaded to a PostgreSQL database in AWS, and only accessible with your username, password and application secret. Requests are authenticated at the app-level with a JWT. User-sensitive information (i.e. 23&Me SNP data) is stored in a table with separate permissions from the rest of the database, and only accessible from 1 endpoint.

Open to ideas on how to build interface(s) for this API, and how to leverage the data collected in an open-source, privacy-friendly fashion!

### To install:

```bash
python3.6 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### To upload and get your Snip data:

1. Download your 23&Me data from their website
   * Navigate your browser here: https://you.23andme.com/tools/data/download/, login, and download the raw data file.
2. Move your 23&Me data file to this directory.
3. Set the `SNIP_API_EMAIL` and `SNIP_API_PASSWORD` **env** variables to define your credentials. (*These will be used in the script below to create an account, and to authorize when you request to get your results*)
```bash
export SNIP_API_EMAIL='<your email>'
export SNIP_API_PASSWORD='<your password>'
```
4. Run the upload client, passing the *name of your 23&me file* as the first arg:
```bash
python upload_23_and_me.py <23_and_me_file.txt>
```
5. Open the file *23_and_me.json* to see your results.
