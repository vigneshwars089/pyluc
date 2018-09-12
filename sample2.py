class index:
    def __init__(self, name, age):
	 def indextxt(self,search_path,fname,search_str):
         fo = open(search_path + fname)

        # Read the first line from the file
         line = fo.readline()
         #print("in")
        # Initialize counter for line number
         line_no = 1

        # Loop until EOF
         while line != '' :
                # Search for string in line
                 index = line.find(search_str)
                 if ( index != -1) :
                     print(fname, "[", line_no, ",", index, "] ", line)

                # Read next line
                 line = fo.readline()  

                # Increment line counter
                 line_no += 1
        # Close the files
         fo.close()
	 def indexpdf(self):
		print(self.data)



#Import os module
import os
import PyPDF2
import re

my=index()

# Ask the user to enter string to search
search_path = input("Enter directory path to search : ")
search_str = input("Enter the search string : ")

# Append a directory separator if not already present
if not (search_path.endswith("/") or search_path.endswith("\\") ): 
        search_path = search_path + "/"
                                                          
# If path does not exist, set search path to current directory
if not os.path.exists(search_path):
        search_path ="."

# Repeat for each file in the directory  
for fname in os.listdir(search_path):
   print(fname)
   # Apply file type filter   
   if fname.endswith(".txt"):

        # Open file for reading
        

   # Apply file type filter   
   if fname.endswith(".pdf"):
        filename=fname   
        pdfFileObj=open(filename,mode='rb')
        pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
        number_of_pages=pdfReader.numPages
         
        pages_text=[]
        words_start_pos={}
        words={}
         
        searchwords=search_str
         
            #for word in searchwords:
        for page in range(number_of_pages):
                    #print(page)
            pages_text.append(pdfReader.getPage(page).extractText())
            words_start_pos[page]=[dwg.start() for dwg in re.finditer(searchwords, 
pages_text
        [page].lower())]
            words[page]=[pages_text[page][value:value+len(searchwords)] for value in 
words_start_pos
        [page]]
        for page in words:
                    for i in range(0,len(words[page])):
                       if str(words[page][i]) != 'nan':
                            # f.write('{0},{1}\n'.format(page+1, words[page][i]))
                            print(page, words[page][i] ,fname)



 
