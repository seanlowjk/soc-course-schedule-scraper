# Soc Course Schedule Scraper 

This microservice builds a HTTP Server on top over the web scraper for the
[NUS SoC Course Schedule Website](https://www.comp.nus.edu.sg/cugresource/soc-sched/)

## Setup Instructions 

1. Ensure that you have `python3` installed in your machine. 

2. Run the command: `pip install -r requirements.txt` 

3. Following which, install [`redis`](https://redis.io/download) and setup your redis server 

4. Setup `config.json` with the following details to setup your connection to the redis-server. 

5. Following which, run `gunicorn -b 127.0.0.1:5000 wsgi:app` to run this in
your `localhost`. 
