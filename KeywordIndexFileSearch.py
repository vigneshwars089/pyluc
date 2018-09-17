class index:
    #Definition for Indexing Txt files
    def indextxt(self,search_path,fname,search_str):
        fo = open(search_path+fname)
        #print ("File Opened")
        # Read the first line from the file
        line = fo.readline()
        #print ("Lines Red")
        # print("in")
        # Initialize counter for line number
        line_no = 1
        # Loop until EOF
        while line != '' :
            #print (line)
            # Search for string in line
            index = line.find(search_str)
            #print ("Find completed")
            if ( index != -1) :
                print("Found in : " + str(fname) + "[Line no - " + str(line_no) + ", Char Indx - " + str(index) + "] ")
            # Read next line
            line = fo.readline()  
            # Increment line counter
            line_no += 1
        # Close the files
        fo.close()
         
    #Definition for Indexing PDF files
    def indexpdf(self,filename,search_str):
        filename=fname   
        pdfFileObj=open(filename,mode='rb')
        pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
        number_of_pages=pdfReader.numPages
         
        #p_text=[]
        pages_text=[]
        words_start_pos={}
        words={}
         
        searchwords=search_str
         
        #for word in searchwords:
        for page in range(number_of_pages):
            #print(page)
            pages_text.append(pdfReader.getPage(page).extractText())
            words_start_pos[page]=[dwg.start() for dwg in re.finditer(searchwords, 
pages_text[page].lower())]
            words[page]=[pages_text[page][value:value+len(searchwords)] for value in 
words_start_pos[page]]
            #print words_start_pos
        for page in words:
            for i in range(0,len(words[page])):
                if str(words[page][i]) != 'nan':
                    # f.write('{0},{1}\n'.format(page+1, words[page][i]))
                    #print(page, words[page][i] ,fname)
                    #Varma changes for getting line no
                    #p_text= pdfReader.getPage(page).extractText()
                    #P_lines=p_text.splitlines()
                    #print P_lines
                    print("Found in : " + str(fname) + "[Page no - " + str(page) + ", Word - " + str(words[page][i]) + "] ")
    
    #Definition for extracting text from Docx files
    def indexDocs(self,path,search_str):
        """
        Take the path of a docx file as argument, return the text in unicode.
        """
        document = zipfile.ZipFile(path)
        #contentToRead = ["header2.xml", "document.xml", "footer2.xml"]
        contentToRead = ["document.xml"]
        paragraphs = []
    
        for xmlfile in contentToRead:
            xml_content = document.read('word/{}'.format(xmlfile))
            tree = XML(xml_content)
            for paragraph in tree.getiterator(PARA):
                texts = [node.text
                         for node in paragraph.getiterator(TEXT)
                         if node.text]
                if texts:
                    textData = ''.join(texts)
                    if xmlfile == "footer2.xml":
                        extractedTxt = "Footer : " + textData
                    elif xmlfile == "header2.xml":
                        extractedTxt = "Header : " + textData
                    else:
                        extractedTxt = textData
    
                    paragraphs.append(extractedTxt)
        document.close()
        #return '\n\n'.join(paragraphs)
        #print '\n\n'.join(paragraphs)
        line_no = 1
        for line in paragraphs:
            #print line
            if search_str in line: 
                 #print paragraphs[i]
                 print("Found in : " + str(fname) + "[Paragraph no - " + str(line_no) + "] ")
            line_no += 1
                 
  
#Import all required modules
import os
import PyPDF2
import re
import zipfile 
try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML

#global variables for word document extraction
WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'

# Ask the user to enter string to search
search_path = input("Enter directory path to search : ")
search_str = input("Enter the search string : ")

# Append a directory separator if not already present
if not (search_path.endswith("/") or search_path.endswith("\\") ): 
    search_path = search_path + "/"
                                                          
# If path does not exist, set search path to current directory
if not os.path.exists(search_path):
    search_path ="."
    
#Create object for class    
ind=index()

# Repeat for each file in the directory  
for fname in os.listdir(search_path):
    # Apply file type filter   
    if fname.endswith(".txt"):
        #print(fname)
        ind.indextxt(search_path,fname,search_str)
    elif fname.endswith(".pdf"):
        #print(fname)
        ind.indexpdf(fname,search_str)
    elif (fname.endswith(".docx") or fname.endswith(".doc")):
        #print(fname)
        doctext=[]
        ind.indexDocs(fname,search_str)
        #print(doctext)
        #ind.indexDocs(fname,doctext,search_str)
        
