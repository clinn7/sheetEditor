import subprocess as sp
import pandas as pd

#Make sure to edit the file path in line 65 to where you stored the downloaded csv file

#The purpose of this program is to edit a csv spreadsheet depending on user inputs.
#The program checks for all rows in the stringToCheck column matching the first input, and edits the fieldToEdit fields
#according to inputs 3 and 4 if the second input is contained in the list under itemToCheck of the same row.

def resetSheet(df):
    df['fieldToEdit1'] = ""
    df['fieldToEdit2'] = ""
    df['fieldToEdit3'] = ""
    df['fieldToEdit4'] = ""
    df['fieldToEdit5'] = ""

def message():
    print('Accepted first inputs from stringToCheck column in csv file (case sensitive): \n\n'
          'first string to check for in column to edit additional columns \n'
          'second string to check for in column to edit additional columns \n'
          'third string to check for in column to edit additional columns \n'
          'fourth string to check for in column to edit additional columns \n\n'
          'Accepted second inputs from (separated) itemToCheck column in csv file: \n\n'
          'Any combination of the following separated by "," (case sensitive):\n'
          'thing1 | thing2 | thing3 | thing4 | thing5 | thing6 | thing7 \n'
          'widget1 | widget2 | widget3 | justOneThing \n\n'
          'Third and fourth inputs will accept any value')

def defineFields(df, input1, input3, input4, itemString):
    df.loc[(df['itemToCheck'] == itemString) & (df['stringToCheck'] == input1),
           ['fieldToEdit1', 'fieldToEdit2', 'fieldToEdit3', 'fieldToEdit4']] = input3, 'edit in defineFields function', input4, 'edit in defineFields function'

def populateFields(df, input1, input2, input3, input4, itemList2, itemList3, itemList4, itemString1, itemString2, itemString3, itemString4):
    print(input1)
    for x in input1:
        if input2 in itemList2:
            defineFields(df, x, input3, input4, itemString1)
            defineFields(df, x, input3, input4, itemString2)
        elif input2 in itemList3:
            defineFields(df, x, input3, input4, itemString1)
            defineFields(df, x, input3, input4, itemString3)
        elif input2 in itemList4:
            defineFields(df, x, input3, input4, itemString1)
            defineFields(df, x, input3, input4, itemString4)
        else:
            print("Input invalid.")

def openSheet(df, filePath):
    df.to_csv(filePath, index=False)
    sp.Popen([filePath], shell=True)

def main():
    # string to check for which rows will be edited
    itemString1 = 'thing1; thing2; thing3; thing4; thing5; thing6; thing7; widget1; widget2, widget3, justOneThing'
    itemString2 = 'thing1; thing2; thing3; thing4; thing5; thing6; thing7'
    itemString3 = 'widget1; widget2; widget3'
    itemString4 = 'justOneThing'
    # list to check for input2 in itemToCheck column for if row should be edited
    itemListNotUsed = ['thing1', 'thing2', 'thing3', 'thing4', 'thing5', 'thing6', 'thing7', 'widget1', 'widget2',
                       'widget3', 'justOneThing']
    itemList2 = ['thing1', 'thing2', 'thing3', 'thing4', 'thing5', 'thing6', 'thing7']
    itemList3 = ['widget1', 'widget2', 'widget3']
    itemList4 = ['justOneThing']
    # csv file to edit
    filePath = "<yourfilepathhere>"
    df = pd.read_csv(filePath)
    message()
    input1 = input('Enter first input: \t').split(',')
    input2 = input("Enter second input:\t")
    input3 = input("Enter third input :\t")
    input4 = input("Enter fourth input :\t")
    resetSheet(df=df)
    populateFields(df=df, input1=input1, input2=input2, input3=input3, input4=input4, itemList2=itemList2, itemList3=itemList3, itemList4=itemList4,
                   itemString1=itemString1, itemString2=itemString2, itemString3=itemString3, itemString4=itemString4)
    openSheet(df=df, filePath=filePath)

main()


