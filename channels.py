import csv
import urllib2

def get_channel_data(channel):

    url = 'https://docs.google.com/spreadsheets/d/1UtA_exZn515gYwv1Sfs0JBq2nOWnlR42Fb0Vw3eMpTs/pub?output=csv'
    response = urllib2.urlopen(url)
    cr = csv.reader(response)

    for row in cr:
        if row[0]==channel:
            return {
            "name": row[1],
            "link":row[4],
            "description": row[5]
            }
    # nothing was found, return None
    return None

if __name__ == '__main__':
    main()
