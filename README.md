# Potato-the-project
Potato the project or thepotato is a Python library that extracts commodity values ​​(information) from a json file and transforms them into an Excel file or to be used even in cmd/shell itself.

![ei_1654889825313-removebg-preview](https://user-images.githubusercontent.com/76263577/173142391-2a471818-28df-4d1b-af16-5f710f6fce7b.png)

# User's Guide  
These instructions illustrate all of Potato's main features, with examples. I show you what the library is for, how it works, how to use it, how to make it do what you want it to do. This document covers version 1.0.1 of Potato. The examples in this documentation should work the same in Python 2.7 and Python 3

# Index
- Installing  
- Start  
- Object Types  
- Encoding  
- Help  

# Installing:  
Potato can be easily installed within your virtual environment using pip.

On the command line, make sure your virtual environment is active, and run the following command:
```

pip install thepotato
```
This will download and install the latest version of thepotato.

Once the installation is complete, you can verify your Potato installation by running thepotato-admin --version from the command line.

# Start:  
First of all , we should clarify that the potato library creates an excel sheet automatically when you call any variable regardless of what it is .

# Object Types:  
These are the objects that you will need to know to call and see the price of a certain desired product.

- cafe - coffee  
- petroleo - Petroleum  
- tri - wheat  
- alg - cotton  
- açu - sugar  
- arro - rice  
- eth - Ethanol  
- fei - beans  
- nat - Natural Gas  
- mad - wood  
- bor - rubber  
- mil - Corn
- alu - aluminium
- ni - nickel
- znc - zinc
- tin - titanium
- cacau - cocoa

# Encoding:
Once downloaded, you must import the module: thepotato .
```

import thepotato
```
Now you must call some desired product to get the price:
```
commodities = thepotato.Thepotato()

commodities.cafe()
commodities.hora() #If you want to see the updated time
```
***Remembering that all this code can change, since it suffers from updates***   
***You need to download this .xlsx file if you want to have a complete spreadsheet : )***  

[lista_preços2.xlsx](https://github.com/dcgo15/Potato-the-project/files/8885809/lista_precos2.xlsx)

***The website has been discontinued***
