
from urllib import urlopen
website_path = raw_input("\nEnter the absolute path for your website: ")
try:
    content = urlopen(website_path).read()
    print "Success, I was able to open: ", website_path 
except:
    print "Error, Unable to open: " , website_path
