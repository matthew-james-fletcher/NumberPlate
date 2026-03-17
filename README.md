This project is for the following design breif

A number plate is structured as:

<img width="308" height="173" alt="image" src="https://github.com/user-attachments/assets/de2134d2-1d89-4715-aa07-224d9ae60042" />

Your task is to create a program that will generate a new number plate given: 
<br>
Memory Tag (e.g. YA) 
<br>
Date in the format dd/mm/yyyy (e.g. 01/01/2002)
<P>
Rules: <P>
The number plate must be unique and your program should not generate repeated number plates. 
<br>
The letters ‘Iʼ, ‘Qʼ and ‘Zʼ should not appear on your number plates as they are restricted as they look too similar to other letters or numbers.
<br>
The age identifier is calculated from the last two numbers of the year in which the car was made. For vehicles the year runs from March -> February. Furthermore, if the car was manufactured in the second half of the year (September - February) then 50 must be added to the age identifier. e.g. <br>
March 2002 – Aug 2002 -> 02 <br>
Sept 2002 – Feb 2003 -> 52 <br>
Examples <p>
Example 1 <p>
Input: MV, 03/04/2010 <br>
Ouput: MV10 FRH 
<p>
Example 2 <p>
Input: YA, 25/09/2001 <br>
Output: YA51 YHL


Out of my two solutions I prefer V1 because it requires less storage and is much more consistent when more and more values are added in. However, I was unsure if the further changes to my code would be more difficult so I added the second option as it didn't take long
