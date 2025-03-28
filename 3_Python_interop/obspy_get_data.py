from obspy import UTCDateTime
from obspy.clients.fdsn import Client

# Initialize the FDSN client to connect to IRIS
client = Client("IRIS")

# Define the time period for the data (one minute of data)
starttime = UTCDateTime("2020-01-01T00:00:00")
endtime = starttime + 60  # 60 seconds later

# Retrieve the waveform data
st = client.get_waveforms(network="IU", station="ANMO", location="00", channel="BHZ",
                          starttime=starttime, endtime=endtime)

data = st.traces[0].data