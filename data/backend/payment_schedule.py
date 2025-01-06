# -*- coding: utf-8 -*-
from utils.preprocessor import FileIO

payment_schedule_backend = FileIO().load_csv(
    "../data/files/payment_schedule_backend_table.csv",
)

# Columns rename
payment_schedule_backend.rename(columns={"user_id": "user_uuid"}, inplace=True)
