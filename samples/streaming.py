from __future__ import print_function

from samples.utils import get_service
import ast
import uuid


# [START stream_row_to_bigquery]
def stream_row_to_bigquery(service,
                           project_id,
                           dataset_id,
                           table_id,
                           row,
                           num_retries=5):
    # Generate a unique row id so retries
    # don't accidentally duplicate insert
    insert_all_data = {
            'insertId': str(uuid.uuid4()),
            'rows': [{'json': row}]
            }
    return service.tabledata().insertAll(
                    projectId=project_id,
                    datasetId=dataset_id,
                    tableId=table_id,
                    body=insert_all_data).execute(num_retries=num_retries)
# [END stream_row_to_bigquery]


# [START main]
def main():
    service = get_service()
    project_id = raw_input("Choose your project ID: ")
    dataset_id = raw_input("Choose a dataset ID: ")
    table_id = raw_input("Choose a table ID : ")

    line = raw_input("Stream a line into your bigquery table:")
    while line:
        print(stream_row_to_bigquery(service,
                                     project_id,
                                     dataset_id,
                                     table_id,
                                     ast.literal_eval(line)))
        line = raw_input(
                "Stream another line into your bigquery table \n" +
                "[hit enter to quit]:")
# [END main]