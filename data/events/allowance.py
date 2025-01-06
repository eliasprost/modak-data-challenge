# -*- coding: utf-8 -*-
from utils.preprocessor import FileIO

allowance_events_table = FileIO().load_json(
    "data/files/allowance_events.json",
    flatten=True,
)
