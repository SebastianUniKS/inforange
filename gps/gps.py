from queryAPI import getGPSdata
from uploadGPSdb import uploadData

startDate = "2025-01-01 00:00:00"
endDate = "2025-01-26 23:59:59"

gpsData = getGPSdata(startDate, endDate)

uploadData (gpsData)