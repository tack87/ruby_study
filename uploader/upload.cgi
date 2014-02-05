#!/usr/local/bin/ruby
require "cgi"
formData = CGI.new
print "Content-type: text/html\n\n"
print "<html><head><title>アップロード後だよ</title></head><body>"
fh = open("| chmod 666 upload.jpg")
open("./upload.jpg","w") do |fh|
fh.binmode
fh.write formData['imgData'].read
end
fh = open("| mv upload.jpg data.jpg")
print "<img src='data.jpg'></body></html>"

