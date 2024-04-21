import ezgmail, os
from twilio.rest import Client

accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken  = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+1'
myCellPhone = '+1'

threads = ezgmail.search('has:attachment')

for i in range(len(threads)):
   threads[i].messages[0].downloadAllAttachments(downloadFolder='gmailFolder')
   threads[i].trash()

for fileName in os.listdir('gmailFolder'):
    if not fileName.endswith('.torrent'):
        continue
    try:
        qbProcess = subprocess.Popen(['/snap/bin/gbittorrent', str(os.path.join('gmailFolder', os.path.basename(fileName)))])
        qbProcess.wait()
        if qbProcess.wait() == 0:
            message = twilioCli.messages.create(body=f'Finished downloading {fileName}', from_=myTwilioNumber, to=myCellPhone)
    except Exception as err:
        print("%s doesn't work: %s" % (fileName, err))
