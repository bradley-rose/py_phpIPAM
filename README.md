# py_phpIPAM
Python API Wrapper for phpIPAM

Based on the [phpIPAM REST API documentation](https://phpipam.net/api/api_documentation/). This is a Python API wrapper built around a bit of functionality so that you can automate certain pieces with Python as you please.

Two recommendations:  
1. Not all functionality is built here. Some of the functionality that I did built here is redundant or potentially confusing. This is an incredibly easy API to work with, so I highly recommend building functionality custom to your needs.
2. Security: Use read-only API tokens where appropriate. Use write-enabled API tokens **only when necessary** to perform Create, Update, or Delete functions. Do your best to encrypt your credentials within your files. 
