import twint
import pandas as pd
import numpy as np
import nest_asyncio
import os

# Nest ayncio function applied for error handling
nest_asyncio.apply()

# Begin querying Tweet Data

t = twint.Config()

t.Search = 'Labour Party'

t.Store_object = True

t.Limit = 15000

t.Pandas = True
t.Hide_output= True

twint.run.Search(t)

# Store output as Pandas DataFrame

output = pd.DataFrame(data=twint.storage.panda.Tweets_df)

output.to_csv('/home/pi/Documents/Twitter Miner/Output/Labourptywed.csv')
