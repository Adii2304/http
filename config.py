'''Following is the file formats supported by the server'''
FORMAT = {
		".aac"	: "audio/aac",
		".abw"	: "application/x-abiword",
		".arc"	: "application/x-freearc",
		".avi"	: "video/x-msvideo",
		".azw"	: "application/vnd.amazon.ebook",
		".bin"	: "application/octet-stream",
		".bmp"	: "image/bmp",
		".bz"	: "application/x-bzip",
		".bz2"	: "application/x-bzip2",
		".csh"	: "application/x-csh",
		".css"	: "text/css",
		".csv"	: "text/csv",
		".doc"	: "application/msword",
		".docx"	: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
		".eot"	: "application/vnd.ms-fontobject",
		".epub" : "application/epub+zip",
		".gz"	: "application/gzip",
		".gif"	: "image/gif",
		".htm"	: "text/html",
		".html" : "text/html",
		".ico" 	: "image/vnd.microsoft.icon",
		".ics"	: "text/calendar",
		".jar"	: "application/java-archive",
		".jpeg"	: "image/jpeg",
		".jpg"	: "image/jpeg",
		".js"	: "text/javascript",
		".json"	: "application/json",
		".jsonld": "application/ld+json",
		".mid"	: "audio/midi",
		" .midi": "audio/midi",
		".mjs"	: "text/javascript",
		".mp3"	: "audio.mpeg",
		".mpeg"	: "video/mpeg",
		".mpkg"	: "application/vnd.apple.installer+xml",
		".odp"	: "application/vnd.oasis.opendocument.presentation",
		".ods"	: "application/vnd.oasis.opendocument.spreadsheet",
		".oga"	: "audio/ogg",
		".ogv"	: "video/ogg",
		".ogx"	: "application/ogg",
		".otf"	: "font/otf",
		".png"	: "image/png",
		".pdf"	: "application/pdf",
		".php"	: "appliction/php",
		".ppt"	: "application/vnd.ms-powerpoint",
		".pptx"	: "application/vnd.openxmlformats-officedocument.presentationml.presentation",
		".rar"	: "application/x-rar-compressed",
		".rtf"	: "application/rtf",
		".sh"	: "application/x-sh",
		".svg"	: "image/svg+xml",
		".swf"	: "application/x-shockwave-flash",
		".tar"	: "application/x-tar",
		".tif"	: "image/tiff",
		" .tiff": "image/tiff",
		".ts"	: "video/mp2t",
		".ttf"	: "font/ttf",
		".txt" 	: "text/html",
		".vsd"	: "application/vnd.visio",
		".wav"	: "audio/wav",
		".weba"	: "audio/webm",
		".webm"	: "video/webm",
		".webp"	: ".webp",
		".woff" : "font/woff",
		".woff2": "font/woff2",
		".xhtml": "application/xhtml+xml",
		".xls"	: "application/vnd.ms-excel",
		".xlsx"	: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
		".xml"	: "application/xml",
		".xul"	: "application/vnd.mozilla.xul+xml",
		".zip"	: "application/zip",
		".3gp"	: "video/3gpp",
		".3g2"	: "video/3gpp2",
		".7z"	: "application/x-7z-compressed",
	}
'''This is the html page to be returned on successfull POST'''
post_string = '''<!DOCTYPE html>
<html>
<head>
	<title>form test</title>
</head>
<body>
	<h1> Resource created! Check wr.txt</h1>
</body>
</html>'''
'''The authorization password for PUT and DELETE methods'''
auth_password = "Happy1"

'''Response status codes'''
status_codes = {
		200 : "Ok",
		201	: "Created",
		202	: "Accepted",
		204 : "No Content",
		304 : "Not Modified",
		400 : "Bad Request",
		401 : "Unauthorized",
		403 : "Forbidden",
		404 : "Not Found",
		411 : "Length required",
		412 : "Precondition Failed",
		414 : "URI too long",
		415 : "Unsupported media Type",
		501 : "Not Implemented",
		505 : "HTTP version not supported",
	}
'''Methods supported by the server'''
methods = ["GET", "POST", "HEAD", "PUT", "DELETE", "TRACE", "OPTIONS"]
'''Size of bytes to be received'''
buffer_size = 1024
MAX_URI_LEN = 100
'''Configure the IP address assigned to your interface. Default : Localhost'''
host = '127.0.0.1'
'''Configure the port number for the server to listen. Note : Do NOT use port numbers from 0 to 1023'''
port = 5671
address = (host, port)