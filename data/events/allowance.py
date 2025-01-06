# -*- coding: utf-8 -*-
from utils.preprocessor import FileIO

allowance_events = FileIO().load_json(
    "../data/files/allowance_events.json",
    flatten=True,
)

# Columns rename
allowance_events.rename(
    columns={
        "user.id": "user_uuid",
        "event.timestamp": "event_timestamp",
        "event.name": "event_name",
        "allowance.scheduled.frequency": "allowance_scheduled_frequency",
        "allowance.scheduled.day": "allowance_scheduled_day",
        "allowance.amount": "allowance_amount",
    },
    inplace=True,
)

# Columns values standardization
allowance_events["event_name"] = allowance_events["event_name"].str.replace(
    "allowance.",
    "",
)
