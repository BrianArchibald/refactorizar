import requests
import lxml.html as lh
import pandas as pd

url='http://pokemondb.net/pokedex/all'
#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

#Check the length of the first 12 rows
[len(T) for T in tr_elements[:12]]

tr_elements = doc.xpath('//tr')

col=[]
i=0
#For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    print '%d:"%s"'%(i,name)
    col.append((name,[]))

#  //////////////////////////////
#  Step 1 for refactoring above code
#  if setting var to 0 outside loop and then incrementing, you can use enumerate

#  col=[]
#  for i, t in enumerate(tr_elements[0])

#  But appears the i is only needed for the print so we can take this out and use a list comprehension
col = [t.text_content, [], for t in tr_elements[0]]

# ////////////////////////////////

#  Anti pattern  ITM  Initialize then modify.  Avoid this!






#Since out first row is the header, data is stored on the second row onwards
for j in range(1,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]

# ///////////////////////////////////  use slice
for T in tr_elements[1:]:

    
    #If row is not of size 10, the //tr data is not from our table 
    # This was not needed and commented out ///
#    if len(T)!=10:
#        break
    
    #i is the index of our column
    # i=0  /////part of ITM pattern again
    
    #Iterate through each element of the row
    for i, t in (T.iterchildren()):
        data=t.text_content() 
        #Check if row is empty
       # if i>0: ///// not needed for pokemon db

        #Convert any numerical value to integers
        # ////// changing this try except to conditional exp
         #   try:
         #       data=int(data)
         #   except:
          #      pass
         col[i][1].append(int(data) if data.isnumeric() else data)

        #Append the data to the empty list of the i'th column
        # col[i][1].append(data) ////////// moved this append to above
        
        #Increment i for the next column
        # i+=1 ///// out due to ITM

Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)

df.head()