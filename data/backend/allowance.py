# -*- coding: utf-8 -*-
from utils.preprocessor import FileIO

allowance_backend_table = FileIO().load_csv(
    "../data/files/allowance_backend_table.csv",
)

# Columns rename
allowance_backend_table.rename(columns={"uuid": "user_uuid"}, inplace=True)