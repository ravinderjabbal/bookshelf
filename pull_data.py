# 1. Connect with DB. Done - line --20
# 2. Pull the content. Done - line --25
# 3. Save the content.

import pandas as pd
from multipledispatch import dispatch
import process

__SHEET_ID = "1U6Lz1sa1Xs0LQV2l9wfSA4Qe13zsqFOujPE2LjX3ngQ"
__SHEET_NAME = "books"


@dispatch()
def get_json_data():
    data = fetch_data(__SHEET_ID, __SHEET_NAME)
    data = change_to_json(data)
    return data


def fetch_data(sheet_id, sheet_name):
    # Pulling the data
    data = pull_content_from_db(sheet_id, sheet_name)
    # changing in dataframe
    data = pd.DataFrame(data)
    return data


def pull_content_from_db(sId, sName):
    # Formatting the link
    sheet_url = f"https://docs.google.com/spreadsheets/d/{sId}/gviz/tq?tqx=out:csv&sheet={sName}"
    #  Connecting the db
    #  Reading in CSV format
    the_sheet = pd.read_csv(sheet_url)
    return the_sheet


def change_to_json(data):
    data = data.to_json(orient="index")
    return data


def get_processed_data():
    data = fetch_data(__SHEET_ID,__SHEET_NAME)
    processed_data = process.processing_data(data)
    return processed_data





