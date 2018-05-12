### To install:

```bash
python3.6 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### To upload your data:

1. Download your 23&Me data from their website
2. Move your 23&Me data file to this directory
3. Run the upload client
```bash
python upload_23_and_me.py <23_and_me_file.txt>
```

### To get your Snip data:

1. Run the download results client
```bash
python get_snip_results.py
```
2. Open the file *23_and_me.json*
