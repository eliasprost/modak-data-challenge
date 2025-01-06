# -*- coding: utf-8 -*-
from utils.preprocessor import FileIO

payment_schedule_backend_table = FileIO().load_csv(
    "data/files/payment_schedule_backend_table.csv",
)
