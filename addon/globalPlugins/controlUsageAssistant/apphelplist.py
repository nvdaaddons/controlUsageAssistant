# Control Usage Assistant
# An add-on for NVDA
# Copyright 2013 Joseph Lee, released under GPL.

# AppModule and process offsets: positive = appModule, negative = process.

# App offsets: lookup the appModule.
appOffsets={
	"explorer":300,
	"powerpnt":400
	}

# Process offsets: come here when we fail to obtain appModules.
procOffsets={
	"EXCEL.EXE":-300,
	"AcroRd32.exe":-400 #This is a special case - although Adobe reader uses virtual buffer, it is not a webpage, hence different message should be given for PDF's.
	}

