#
#   Script to download bunch of articles in a given language from Wikipedia.
#
#   MAX_PAGES * MULTIPLER = acutal articles it will download
#
#   @author Gleb Promokhov gxp5819@rit.edu
#

import wikipedia
import os


MAX_PAGES = 5
MULTIPLER = 5
LANG = 'en' #'en', 'nl', 'fr', etc...

DATA_PATH = './wiki_data'
if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)

wikipedia.set_lang(LANG)

print("~~~ Download language: %s" % LANG)
print("~~~ Max number of pages to download: %s" % (MAX_PAGES * MULTIPLER))

# get a bunch of random pages
print("~~~ Downloading page titles...")
pages = []
for i in range(MAX_PAGES):
    pages += wikipedia.random(MULTIPLER) #API CALL
pages = list(set(pages))

print("~~~ Downloading pages into ./wiki_data ...")

# get content of those page
for p in pages:

    # print("~~~ Downloading content for: %s..." % p)

    data = ''
    try:
        data += wikipedia.page(p).content #API CALL
    except wikipedia.exceptions.DisambiguationError as e:
        print("!!! WARNING: ambiguous page title: %s" % p)
        continue
    except wikipedia.exceptions.PageError as e:
        print("!!! WARNING: failed to download content for: %s " % p)
        continue

    fname = p.replace(' ', '_') + '.html'
    print("~~~ Saving: %s" % fname)
    output = open( DATA_PATH + '/' + fname, 'a')
    output.write(data)


output.close()
